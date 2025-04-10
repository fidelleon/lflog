import os
import yaml

from callsign.callsign import Callsign

with open(os.path.join(os.path.dirname(__file__), 'settings.yaml'), 'r') as f:
    settings = yaml.safe_load(f)


mssql = settings['db']['mssql']
clublog = settings['clublog']
qrz = settings['qrz']

SERVER = mssql['server']
DATABASE = mssql['database']
USERNAME = mssql['username']
PASSWORD = mssql['password']

connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=Yes'

if __name__ == "__main__":
    a = Callsign('4KR60S')
    print(a.get_callsign_info())
    a = Callsign('A975IARU')
    print(a.get_callsign_info())
