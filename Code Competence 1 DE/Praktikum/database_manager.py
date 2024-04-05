from pymysql import connect
import pandas as pd

class DatabaseManager:
   def __init__(self, host, user, password, database):
      self.host = host
      self.user = user
      self.password = password
      self.database = database
      self.connection = None

   def connect(self):
      self.connection = connect( host=self.host,
                                 db=self.database,
                                 user=self.user,
                                 password=self.password,
                               )
      self.cursor = self.connection.cursor()

   def create_tables(self):
      with self.connection.cursor() as cursor:
         # Definisi tabel sentiments
         cursor.execute("""
                        CREATE TABLE IF NOT EXISTS sentiments (
                        sentiment_id INT AUTO_INCREMENT PRIMARY KEY,
                        sentiment_label VARCHAR(255) NOT NULL)
                        """)

         # Definisi tabel tweets
         cursor.execute("""
                        CREATE TABLE IF NOT EXISTS tweets (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        text TEXT,
                        sentiment_id INT,
                        FOREIGN KEY (sentiment_id) REFERENCES sentiments(sentiment_id))
                        """)
      self.connection.commit()


   def insert_from_csv(self):
      
      csv_file2 = "Praktikum/data_dest/sentiment_counts.csv"
      original_df2 = pd.read_csv(csv_file2)
      sentiment_labels_df = original_df2.drop('count', axis=1)
      sentiment_df = sentiment_labels_df.drop('Unnamed: 0', axis=1)
      sentiment_df.rename(columns = {'labels':'sentiment_label'}, inplace = True)

      try:
         with self.connection.cursor() as cursor:
            for index, row in sentiment_df.iterrows():
               values = tuple(row)
               placeholders = ', '.join(['%s'] * len(values))
               columns = ', '.join(sentiment_df.columns)
               sql = f"INSERT INTO sentiments ({columns}) VALUES ({placeholders})"
               cursor.execute(sql, values)
         self.connection.commit()
         print(f"Data berhasil dimasukkan ke dalam tabel sentiments.")
      except Exception as e:
         print(f"Error: {e}")

      csv_file = "Praktikum/data_source/file.csv"
      original_df = pd.read_csv(csv_file)
      original_df['labels'].replace('good', '1', inplace=True)
      original_df['labels'].replace('bad', '2', inplace=True)
      original_df['labels'].replace('neutral', '3', inplace=True)
      tweets_df = original_df.drop('Unnamed: 0', axis=1)
      tweets_df.rename(columns = {'tweets':'text'}, inplace = True)
      tweets_df.rename(columns = {'labels':'sentiment_id'}, inplace = True)
      
      try:
         with self.connection.cursor() as cursor:
            for index, row in tweets_df.iterrows():
               values = tuple(row)
               placeholders = ', '.join(['%s'] * len(values))
               columns = ', '.join(tweets_df.columns)
               sql = f"INSERT INTO tweets ({columns}) VALUES ({placeholders})"
               cursor.execute(sql, values)
         self.connection.commit()
         print(f"Data berhasil dimasukkan ke dalam tabel tweets.")
      except Exception as e:
         print(f"Error: {e}")
         
         
   def close(self):
      if self.connection:
         self.connection.close()


host = 'localhost'
user = 'root'
password = '@Kinan673'
database = 'sentiment_classifier'

manager = DatabaseManager(host, user, password, database)
manager.connect()
manager.create_tables()
manager.insert_from_csv()
manager.close()
