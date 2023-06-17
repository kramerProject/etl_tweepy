from datetime import timedelta
from email.policy import default
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_etl import run_twitter_etl, favorite_counter


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 10, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='twitter etl'
)


run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=run_twitter_etl,
    dag=dag
)

run_counter = PythonOperator(
    task_id='favorite_counter',
    python_callable=favorite_counter,
    dag=dag
)

run_etl >> run_counter