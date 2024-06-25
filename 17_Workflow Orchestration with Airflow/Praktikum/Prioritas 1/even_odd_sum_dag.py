from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

import random

def rand(ti, ranges, start, end):
   randinteger = [random.randint(start, end) for _ in range(ranges)]
   ti.xcom_push(key="random_integer", value=randinteger)

def count_summarize(ti):
   randinteger = ti.xcom_pull(task_ids="generate_randint", key="random_integer")
   total_sum = sum(randinteger)
   ti.xcom_push(key="sum", value=total_sum)

def checker(ti):
   total_sum = ti.xcom_pull(task_ids="sum_count", key="sum")
   if total_sum % 2 == 0:
      print("Even Sum")
   else:
      print("Odd Sum")

default_args = {
   "owner":"nimas",
   "retries":5,
   "retry_delay":timedelta(minutes=2),
}

with DAG (
   dag_id="even_odd_sum_v1",
   default_args=default_args,
   description="a DAG to generate random integers, sum them, and check if the sum is even or odd",
   start_date=datetime(2024, 6, 10, 14),
   schedule_interval='@daily',
) as dag:
   task1 = PythonOperator(
      task_id="generate_randint",
      python_callable=rand,
      op_kwargs={"ranges": 25, "start": 1, "end": 50},
   )
   task2 = PythonOperator(
      task_id="sum_count",
      python_callable=count_summarize,
   )
   task3 = PythonOperator(
      task_id="checking_sum",
      python_callable=checker,
   )
   
   task1 >> task2
   task2 >> task3