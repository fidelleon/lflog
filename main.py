import os
import pyodbc
import yaml

with open(os.path.join(os.path.dirname(__file__), 'settings.yaml'), 'r') as f:
    settings = yaml.safe_load(f)
    print(settings)


mssql = settings['db']['mssql']

SERVER = mssql['server']
DATABASE = mssql['database']
USERNAME = mssql['username']
PASSWORD = mssql['password']


connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=Yes'

with pyodbc.connect(connection_string) as conn:
    SQL_QUERY = """
    SELECT
    TOP 5 *
    FROM Test
    """

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()
    for r in records:
        print(f"{r.id}\t{r.test}")
