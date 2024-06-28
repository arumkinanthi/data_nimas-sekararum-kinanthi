import pandas as pd

class DataLakeBuilder:
   
   def __init__(self, path):
      
      self.path = path
      
   def read_csv_data(self):
      
      self.dataframe = pd.read_csv(self.path)
      print("success read csv")
   
   def handle_missing_values(self):
      
      missing_values = self.dataframe.isnull().sum()
      num_of_rows = int(len(self.dataframe)/4)
      for column, missing_count in missing_values.items():
         if missing_count >= num_of_rows:
            # menghapus kolom jika memiliki missing values >= 25%
            self.dataframe.drop(column, axis=1, inplace=True)
         
      # menghapus baris yang memiliki nilai NaN lebih dari 1, tetapi mempertahankan baris yang memiliki minimal dua nilai non-NaN
      self.dataframe.dropna(thresh=len(self.dataframe.columns) - 1, inplace=True)

      self.dataframe = self.dataframe.reset_index(drop=True)
      print("success handling missing values")
      
   def handle_outliers(self):
      
      numerical_df = self.dataframe.select_dtypes(include=['number'])
      if numerical_df.empty:
         print("Tidak ada kolom numerik yang bisa diidentifikasi outliernya.")
         return self.dataframe

      Q1 = numerical_df.quantile(0.25)
      Q3 = numerical_df.quantile(0.75)
      IQR = Q3 - Q1

      lower_bound = Q1 - 1.5 * IQR
      upper_bound = Q3 + 1.5 * IQR

      outlier_filter = (numerical_df >= lower_bound) & (numerical_df <= upper_bound)
      self.dataframe = self.dataframe[outlier_filter.all(axis=1)]
      print("success to handling outliers")
      
   def save_to_parquet(self, file_name):
      
      self.dataframe.to_parquet(f"Praktikum/data_dest/{file_name}")
      print(f"{file_name} success to parquet")
      
   def validate_data(self, file_path):
      self.df = pd.read_parquet(file_path)
      print(self.df.head(10))
      
if __name__ == "__main__":
   
   path = 'Praktikum/data_source/customer_feedback.csv'
   customer_feedback_df = DataLakeBuilder(path)
   customer_feedback_df.read_csv_data()
   customer_feedback_df.handle_missing_values()
   customer_feedback_df.handle_outliers()
   customer_feedback_df.save_to_parquet("customer_feedback.parquet")
   customer_feedback_df.validate_data("Praktikum/data_dest/customer_feedback.parquet")
   
   path = 'Praktikum/data_source/customers.csv'
   customers_df = DataLakeBuilder(path)
   customers_df.read_csv_data()
   customers_df.handle_missing_values()
   customers_df.handle_outliers()
   customers_df.save_to_parquet("customers.parquet")
   customers_df.validate_data("Praktikum/data_dest/customers.parquet")
   
   path = 'Praktikum/data_source/events.csv'
   events_df = DataLakeBuilder(path)
   events_df.read_csv_data()
   events_df.handle_missing_values()
   events_df.handle_outliers()
   events_df.save_to_parquet("events.parquet")
   events_df.validate_data("Praktikum/data_dest/events.parquet")
   
   path = 'Praktikum/data_source/tickets.csv'
   tickets_df = DataLakeBuilder(path)
   tickets_df.read_csv_data()
   tickets_df.handle_missing_values()
   tickets_df.handle_outliers()
   tickets_df.save_to_parquet("tickets.parquet")
   tickets_df.validate_data("Praktikum/data_dest/tickets.parquet")
   
   path = 'Praktikum/data_source/transactions.csv'
   transactions_df = DataLakeBuilder(path)
   transactions_df.read_csv_data()
   transactions_df.handle_missing_values()
   transactions_df.handle_outliers()
   transactions_df.save_to_parquet("transactions.parquet")
   transactions_df.validate_data("Praktikum/data_dest/transactions.parquet")
      