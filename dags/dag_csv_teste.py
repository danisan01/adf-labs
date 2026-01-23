# dags/dag_csv_teste.py
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

# Definição da DAG
with DAG(
    dag_id="dag_csv_teste",
    start_date=datetime(2024, 1, 1),
    schedule=None,   # execução manual
    catchup=False,
    tags=["teste", "csv"]
) as dag:

    # 1 - Baixar CSV
    baixar_csv = BashOperator(
        task_id="baixar_csv",
        bash_command="curl -o /tmp/arquivo.csv https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv"
    )

    # 2 - Salvar local (já está salvo em /tmp, mas simulamos outro passo)
    salvar_local = BashOperator(
        task_id="salvar_local",
        bash_command="cp /tmp/arquivo.csv /tmp/arquivo_local.csv"
    )

    # 3 - Transformar (simulado)
    transformar = BashOperator(
        task_id="transformar",
        bash_command="echo 'Transformando arquivo_local.csv... (simulação)'"
    )

    # Dependências: baixar -> salvar -> transformar
    baixar_csv >> salvar_local >> transformar
