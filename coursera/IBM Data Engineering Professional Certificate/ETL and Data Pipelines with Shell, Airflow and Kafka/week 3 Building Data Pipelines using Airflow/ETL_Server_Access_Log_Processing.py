# Import library
from datetime import timedelta # calculate different between dates
from airflow import DAG # The DAG object to instantiate a DAG obj
from airflow.operators.bash_operator import BashOperator # operator to write bash tasks
from airflow.utils.dates import days_ago # to make schedule

# DAG args
default_args = {
    'owner': 'ersa',
    'start_date': days_ago(0), # it means, start date from today
    'email': ['ersa@email.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1, # retry once if tasks fail when executed
    'retry_delay': timedelta(minutes=5), # do retry tasks if fail after
}

# Definition DAG 
dag = DAG(
    'ETL_Server_Access_Log_Processing',
    default_args=default_args,
    description='ETL_Server_Access_Log_Processing',
    schedule_interval=timedelta(days=1),
)

# Defining tasks 
# first task
# in this task, we scheduled to download the data source from cloud storage
download = BashOperator(
    task_id='download',
    bash_command='wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt',
    dag=dag,
)

# second task
# in this task, we only extract timestamp and visitorid only and redirect the output into a file
extract = BashOperator(
    task_id='extract',
    bash_command='cut -f1,4 -d"#" web-server-access-log.txt > /home/project/airflow/dags/extracted.txt',
    dag=dag,
)

# third task
# in this task, we capitalize every value in column visitorid
transform = BashOperator(
    task_id='transform',
    bash_command='tr "[a-z]" "[A-Z]" < /home/project/airflow/dags/extracted.txt > /home/project/airflow/dags/capitalize.txt',
    dag=dag,
)

# third task
# in this task, we load the file into selected file 
load = BashOperator(
    task_id='load',
    bash_command='zip log.zip capitalized.txt' ,
    dag=dag,
)

download >> extract >> transform >> load