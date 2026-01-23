# dags/dag_trigger_params_simple.py
from datetime import datetime
from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

with DAG(
    dag_id="dag_trigger_params_simple",
    start_date=datetime(2024, 1, 1),
    schedule=None,   # execução manual
    catchup=False,
    tags=["teste", "trigger"]
) as dag:

    trigger_params = TriggerDagRunOperator(
        task_id="trigger_dag_params_teste",
        trigger_dag_id="dag_params_teste"  # DAG alvo
    )
