from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
   "owner":"nimas",
   "retries":5,
   "retry_delay":timedelta(minutes=2),
}

with DAG (
   dag_id="hello_airflow_v1",
   default_args=default_args,
   description="hello airflow with bash operator",
   start_date=datetime(2024, 6, 10, 14),
   schedule_interval='@daily',
) as dag:
   task1 = BashOperator(
      task_id="task_1",
      bash_command="echo hello airflow",
   )
   task2 = BashOperator(
      task_id="task_2",
      bash_command="mkdir -p /tmp/data/about_us",
   )
   task3 = BashOperator(
      task_id="task_3",
      bash_command="mkdir -p /tmp/data/our_works",
   )
   task4 = BashOperator(
      task_id="task_4",
      bash_command="touch /tmp/data/about_us/about.txt",
   )
   task5 = BashOperator(
      task_id="task_5",
      bash_command="touch /tmp/data/our_works/works.txt",
   )
   task6 = BashOperator(
      task_id="task_6",
      bash_command="echo done!"
   )
   
   task1 >> [task2, task3]
   task2 >> task4
   task3 >> task5
   [task4, task5] >> task6