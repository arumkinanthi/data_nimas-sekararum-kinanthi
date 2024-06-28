import pandas as pd
from datetime import datetime
from google.cloud import storage

import google.oauth2.service_account
import io
import os
from dotenv import load_dotenv

class DataWarehouseLoader:
    def __init__(self, bucket_name, credentials):
        self.bucket_name = bucket_name
        self.storage_client = storage.Client(credentials=credentials)
        self.bucket = self.storage_client.bucket(bucket_name)
    
    def load_data(self, file_path):
        try:
            df = pd.read_parquet(file_path)
            print(f"Success reading parquet from {file_path}")
            return df
        except Exception as e:
            print(f"Error reading parquet from {file_path}: {e}")
            return None
    
    def transform_data(self, events_df, tickets_df, transactions_df, customer_feedback_df):
        try:
            # Ensure required columns are present
            required_columns = {
                "events_df": ["event_id", "name"],
                "tickets_df": ["ticket_id", "event_id"],
                "transactions_df": ["transaction_id", "ticket_id", "total_amount"],
                "customer_feedback_df": ["transaction_id", "rating"]
            }

            for df_name, columns in required_columns.items():
                df = locals()[df_name]
                for col in columns:
                    if col not in df.columns:
                        raise ValueError(f"Missing column '{col}' in {df_name}")

            # Merge DataFrames
            merged_df = transactions_df.merge(tickets_df, on='ticket_id').merge(events_df, on='event_id')

            # Menghitung Jumlah Tiket yang Terjual per Acara
            tickets_sold_per_event = merged_df.groupby(['event_id', 'name'])['quantity'].sum().reset_index()
            tickets_sold_per_event.rename(columns={'quantity': 'tickets_sold'}, inplace=True)

            # Menghitung Total Pendapatan dari Setiap Acara
            revenue_per_event = merged_df.groupby(['event_id', 'name'])['total_amount'].sum().reset_index()
            revenue_per_event.rename(columns={'total_amount': 'total_revenue'}, inplace=True)

            # Analisis Feedback Pelanggan
            feedback_df = customer_feedback_df.merge(transactions_df, on='transaction_id')
            feedback_analysis = feedback_df.groupby(['event_id', 'name'])['rating'].mean().reset_index()
            feedback_analysis.rename(columns={'rating': 'average_rating'}, inplace=True)

            print("Success transforming data")
            return tickets_sold_per_event, revenue_per_event, feedback_analysis
        except Exception as e:
            print(f"Error during data transformation: {e}")
            return None, None, None
    
    def save_to_warehouse(self, df, table_name):
        try:
            date_path = datetime.now().strftime('%Y/%m/%d')
            blob = self.bucket.blob(f'{date_path}/{table_name}')

            buffer = io.BytesIO()
            df.to_parquet(buffer)
            buffer.seek(0)

            blob.upload_from_file(buffer, content_type='application/octet-stream')
            print(f"Success saving data to {date_path}/{table_name} in warehouse")
        except Exception as e:
            print(f"Error saving data to warehouse: {e}")

if __name__ == "__main__":
    try:
        # Load environment variables from .env file
        load_dotenv()

        # Load path to Google credentials from environment variable
        credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        if not credentials_path:
            raise ValueError("No GOOGLE_APPLICATION_CREDENTIALS found in environment variables")

        credentials = google.oauth2.service_account.Credentials.from_service_account_file(credentials_path)
        
        bucket_name = "code-competence2"
        loader = DataWarehouseLoader(bucket_name, credentials)

        # Load data dari Data Lake
        customer_feedback_df = loader.load_data("Praktikum/data_dest/customer_feedback.parquet")
        events_df = loader.load_data("Praktikum/data_dest/events.parquet")
        tickets_df = loader.load_data("Praktikum/data_dest/tickets.parquet")
        transactions_df = loader.load_data("Praktikum/data_dest/transactions.parquet")

        if all(df is not None and not df.empty for df in [events_df, tickets_df, transactions_df, customer_feedback_df]):
            tickets_sold_per_event, revenue_per_event, feedback_analysis = loader.transform_data(events_df, tickets_df, transactions_df, customer_feedback_df)
            
            if all(df is not None and not df.empty for df in [tickets_sold_per_event, revenue_per_event, feedback_analysis]):
                loader.save_to_warehouse(tickets_sold_per_event, "Tickets_sold_per_event.parquet")
                loader.save_to_warehouse(revenue_per_event, "Revenue_per_event.parquet")
                loader.save_to_warehouse(feedback_analysis, "Feedback_analysis.parquet")
    except Exception as e:
        print(f"Error in main execution: {e}")
