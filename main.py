import os
import yaml

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
    from remotes.lotw import LoTW
    from remotes.eqsl import eQSL
    from remotes.qrz import QRZ
    # from remotes.clublog import ClubLog

    # print(LoTW.is_lotw_user('EA3IEG'))
    # print(eQSL.is_eqsl_user('EA3IEGG'))
    print(QRZ.get_callsign_info('ea3iegg'))
    # ClubLog.update_clublog_database()
