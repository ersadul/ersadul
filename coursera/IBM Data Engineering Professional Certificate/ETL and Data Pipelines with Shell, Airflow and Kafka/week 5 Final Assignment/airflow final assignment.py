# import library
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# DAG args
default_args = {
    'owner': 'ersa',
    'start_date': days_ago(0), # it means, start date from today
    'email': ['ersa@email.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1, # retry once if tasks fail when executed
    'retry_delay': timedelta(minutes=5), # do retry tasks if fail after
}

# define DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)

# Defining tasks 
# unzip data task
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz; sudo tar -xzvf tolldata.tgz',
    dag=dag,
)

# extract_data_from_csv task
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='sudo chmod 777 /home/project/airflow/dags/finalassignment; cut -d"," -f1-4 vehicle-data.csv > /home/project/airflow/dags/finalassignment/csv_data.csv',
    dag=dag,
)

# extract_data_from_tsv task
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command='tr "\t" "," < tollplaza-data.tsv | cut -d"," -f5-7 > tsv_data.csv',
    dag=dag,
)

# extract_data_from_fixed_width task
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command='awk \'{print $10,$11}\' payment-data.txt | tr " " "," > fixed_width_data.csv',
    dag=dag,
)

# consolidate_data task
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command='paste -d "," csv_data.csv fixed_width_data.csv tsv_data.csv > extracted_data.csv',
    dag=dag,
)

# transform_data task# import library
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# DAG args
default_args = {
    'owner': 'ersa',
    'start_date': days_ago(0), # it means, start date from today
    'email': ['ersa@email.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1, # retry once if tasks fail when executed
    'retry_delay': timedelta(minutes=5), # do retry tasks if fail after
}

# define DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)

# Defining tasks 
# unzip data task
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz; sudo tar -xzvf tolldata.tgz',
    dag=dag,
)

# extract_data_from_csv task
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='sudo chmod 777 /home/project/airflow/dags/finalassignment; cut -d"," -f1-4 vehicle-data.csv > /home/project/airflow/dags/finalassignment/csv_data.csv',
    dag=dag,
)

# extract_data_from_tsv task
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command='tr "\t" "," < tollplaza-data.tsv | cut -d"," -f5-7 > tsv_data.csv',
    dag=dag,
)

# extract_data_from_fixed_width task
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command='awk \'{print $10,$11}\' payment-data.txt | tr " " "," > fixed_width_data.csv',
    dag=dag,
)

# consolidate_data task
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command='paste -d "," csv_data.csv fixed_width_data.csv tsv_data.csv > extracted_data.csv',
    dag=dag,
)

# transform_data task
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='sudo chmod 777 staging/; awk \'BEGIN{FS=","; OFS=","} {$4=toupper($4)} {print}\' extracted_data.csv > staging/transformed_data.csv',
    dag=dag,
)

unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data