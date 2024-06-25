from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

import requests
import pandas as pd

def load_data(ti):
   url = 'https://fakestoreapi.com/products'
   df_api = pd.DataFrame(requests.get(url).json())
   ti.xcom_push(key="api_dataset", value=df_api.to_json())

def write_to_csv(ti):
   api_json = ti.xcom_pull(task_ids="get_api_dataset", key="api_dataset")
   api_df = pd.read_json(api_json)
   api_df.to_csv("~/data_api_airflow/from_api.csv", index=False)

def write_to_txt(ti):
   api_json = ti.xcom_pull(task_ids="get_api_dataset", key="api_dataset")
   api_df = pd.read_json(api_json)
   api_df.to_csv("~/data_api_airflow/from_api.txt", index=False, sep='\t')

   
default_args = {
   "owner":"nimas",
   "retries":5,
   "retry_delay":timedelta(minutes=2),
}

with DAG (
   dag_id="api_service_v1",
   default_args=default_args,
   description="getting data from API and write into csv & txt file",
   start_date=datetime(2024, 6, 10, 14),
   schedule_interval='@daily',
) as dag:
   task1 = PythonOperator(
      task_id="get_api_dataset",
      python_callable=load_data
   )
   task2 = PythonOperator(
      task_id="json_to_csv",
      python_callable=write_to_csv,
   )
   task3 = PythonOperator(
      task_id="json_to_txt",
      python_callable=write_to_txt,
   )
   task4 = BashOperator(
      task_id="task_4",
      bash_command="echo done!"
   )
   
   task1 >> [task2, task3]
   [task2, task3] >> task4