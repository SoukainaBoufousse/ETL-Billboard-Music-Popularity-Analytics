from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.postgres_operator import PostgresOperator
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from datetime import datetime
import pandas as pd
import pickle

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 6), # Change the date to the actual start date
    'retries': 1,
}
dag = DAG(
    'ML_Pipeline',
    default_args=default_args,
    description='End to end ML pipeline',
    schedule_interval='@once',
)

# Task to extract data from PostgreSQL
extract_task = PostgresOperator(
    task_id='extract_task',
    postgres_conn_id='postgres_conn',
    sql=f'SELECT * FROM music', 
    dag=dag,
)

# Task to train XGBoost model
def train_xgboost_model(**kwargs):
    # Fetch data from task instance
    ti = kwargs['ti']
    extracted_data = ti.xcom_pull(task_ids='extract_task')

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(extracted_data, columns=['Artist','Title','Label','chroma_stft','rms','spectral_centroid','spectral_bandwidth','spectral_rolloff','zero_crossing_rate','mfcc_1','mfcc_2','mfcc_3','mfcc_4','mfcc_5','mfcc_6','mfcc_7','mfcc_8','mfcc_9','mfcc_10','mfcc_11','mfcc_12','mfcc_13','mfcc_14','mfcc_15','mfcc_16','mfcc_17','mfcc_18','mfcc_19','mfcc_20'  ])  

    # Split the data into features and target
    X = df.drop(['Artist', 'Title','Label'], axis=1) 
    y = df['Label']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the XGBoost model
    model = XGBRegressor()

    # Train the model
    model.fit(X_train, y_train)
    model_filename = '/opt/airflow/dags/model.pkl'  # Provide the desired path and filename
    with open(model_filename, 'wb') as model_file:
        pickle.dump(model, model_file)




train_model_task = PythonOperator(
    task_id='train_model_task',
    python_callable=train_xgboost_model,
    provide_context=True,
    dag=dag,
)


# Set task dependencies
extract_task >> train_model_task 

