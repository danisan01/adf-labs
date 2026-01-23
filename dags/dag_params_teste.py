# dags/dag_params_teste.py
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dag_params_teste",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["teste", "params"],
    params={
        "p_date": "2024-01-01",
        "p_filename": "arquivo.csv",
        "p_folder": "/tmp",
    },
) as dag:

    print_ds = BashOperator(
        task_id="print_ds",
        bash_command="echo 'Data de execução: {{ ds }}'"
    )

    print_params = BashOperator(
        task_id="print_params",
        bash_command="""
echo "Parâmetro p_date: {{ params.p_date }}"
echo "Parâmetro p_filename: {{ params.p_filename }}"
echo "Parâmetro p_folder: {{ params.p_folder }}"
"""
    )

    print_ds >> print_params
