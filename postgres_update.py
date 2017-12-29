from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators import PythonOperator
from insert import main_insert

default_args = {
    'owner': 'kiwiak',
    'depends_on_past': False,
    'start_date': datetime.utcnow(),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('movie_db_update', default_args=default_args)

t1 = PythonOperator(
    task_id='api_to_db',
    python_callable=main_insert,
    op_args=['Hobbit'],
    dag=dag
)
