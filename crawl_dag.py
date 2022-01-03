from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Duongdd',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
with DAG(
        'Crawl Tinh Te',
        default_args=default_args,
        description='Crawl post, comment, author',
        schedule_interval='0 3 * * *',
        start_date=datetime(2021, 10, 20),
        catchup=False,
        tags=['test'],
) as dag:
    t1 = BashOperator(
        task_id='Crawl',
        bash_command='python crawl_post.py ',
    )

    t1
