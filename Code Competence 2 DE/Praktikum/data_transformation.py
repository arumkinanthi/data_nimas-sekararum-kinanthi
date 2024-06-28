import pandas as pd
from datetime import datetime
from google.cloud import storage

import google.oauth2
import google.oauth2.service_account

import io
import json

class DataWarehouseLoader:
   
   def __init__(self, bucket_name):
      
      self.bucket_name = bucket_name
      self.storage_client = storage.Client()         
      self.bucket = self.storage_client.bucket(bucket_name)
      
   def load_data(self, file_path):
      
      self.dataframe = pd.read_parquet(file_path)
      print("success read parquet")
      
   def transform_data(self, events_df, tickets_df, transactions_df, customer_feedback_df):
      
      merged_df = transactions_df.merge(tickets_df, on='ticket_id').merge(events_df, on='event_id')

      tickets_sold_per_event = merged_df.groupby(['event_id', 'name'])['quantity'].sum().reset_index()
      tickets_sold_per_event.rename(columns={'quantity': 'tickets_sold'}, inplace=True)

      revenue_per_event = merged_df.groupby(['event_id', 'name'])['total_amount'].sum().reset_index()
      revenue_per_event.rename(columns={'total_amount': 'total_revenue'}, inplace=True)

      feedback_df = customer_feedback_df.merge(transactions_df, on='transaction_id')
      feedback_analysis = feedback_df.groupby(['event_id', 'name'])['rating'].mean().reset_index()
      feedback_analysis.rename(columns={'rating': 'average_rating'}, inplace=True)

      print("success transforming data")
      return tickets_sold_per_event, revenue_per_event, feedback_analysis
      
   def save_to_warehouse(self, df, table_name):
      
      date_path = datetime.now().strftime('%Y/%m/%d')
      blob = self.bucket.blob(f'{date_path}/{table_name}')

      buffer = io.BytesIO()
      df.to_parquet(buffer)
      buffer.seek(0)

      blob.upload_from_file(buffer, content_type='application/octet-stream')
      print("success saving data to warehouse")
      
if __name__ == "__main___":
   
   with open("accountKey.json") as f:
         service_account_info = json.load(f)
      
   credentials = google.oauth2.service_account.Credentials.from_service_account_info(service_account_info)
   storage_client = google.cloud.storage.Client(credentials=credentials)
   
   bucket_name = "code-competence2"
   loader = DataWarehouseLoader(bucket_name)

   customer_feedback_df = loader.load_data("data_dest/customer_feedback.parquet")
   customers_df = loader.load_data("data_dest/customers.parquet")
   events_df = loader.load_data("data_dest/events.parquet")
   tickets_df = loader.load_data("data_dest/tickets.parquet")
   transactions_df = loader.load_data("data_dest/transactions.parquet")

   if all([events_df, customers_df, tickets_df, transactions_df, customer_feedback_df]):
      tickets_sold_per_event, revenue_per_event, feedback_analysis = loader.transform_data(events_df, customers_df, tickets_df, transactions_df, customer_feedback_df)
        
      if all([tickets_sold_per_event, revenue_per_event, feedback_analysis]):
         loader.save_to_warehouse(tickets_sold_per_event, "Tickets_sold_per_event.parquet")
         loader.save_to_warehouse(revenue_per_event, "Revenue_per_event.parquet")
         loader.save_to_warehouse(feedback_analysis, "Feedback_analysis.parquet")