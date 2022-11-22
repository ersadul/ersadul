# Import library
from datetime import timedelta # calculate different between dates
from airflow import DAG # The DAG object to instantiate a DAG obj
from airflow.operators.bash_operator import BashOperator # operator to write bash tasks
from airflow.utils.dates import days_ago # to make schedule

# Defining DAG args
default_args = {
    'owner': 'ersa',
    'start_date': days_ago(0), # it means, start date from today
    'email': ['ersa@email.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1, # retry once if tasks fail when executed
    'retry_delay': timedelta(minutes=5), # do retry tasks if fail after
}

# Defining DAG
dag = DAG(
    'my-first-dag',
    default_args=default_args,
    description='My first DAG',
    schedule_interval=timedelta(days=1),
)

# Defining tasks 
# first task
extract = BashOperator(
    task_id='extract',
    bash_command='cut -d":" -f1,3,6 /etc/passwd > /home/project/airflow/dags/extracted-data.txt',
    dag=dag,
)

# second task
transform_and_load = BashOperator(
    task_id='transform',
    bash_command='tr ":" "," < /home/project/airflow/dags/extracted-data.txt > /home/project/airflow/dags/transformed-data.csv',
    dag=dag,
)

# task pipeline/dependency
extract >> transform_and_load