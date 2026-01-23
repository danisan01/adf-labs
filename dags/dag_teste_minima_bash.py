# dags/dag_teste_bash.py
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dag_teste_minima_bash",
    start_date=datetime(2024, 1, 1),
    schedule=None,  # execução manual
    catchup=False,
    tags=["teste", "minima"]
) as dag:
    tarefa_a = BashOperator(
        task_id="tarefa_a",
        bash_command="echo 'Executando tarefa A'"
    )

    tarefa_b = BashOperator(
        task_id="tarefa_b",
        bash_command="echo 'Executando tarefa B'"
    )

    tarefa_a >> tarefa_b
