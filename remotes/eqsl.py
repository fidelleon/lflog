import datetime
import io

import pyodbc
import requests

from main import connection_string


class eQSL:
    eqsl_users = 'https://www.eqsl.cc/qslcard/DownloadedFiles/AGMemberList.txt'

    @staticmethod
    def update_eqsl_users():
        eqsl_csv = requests.get(eQSL.eqsl_users)
        eqsl_csv.raise_for_status()
        csvio = io.StringIO(eqsl_csv.text)

        with pyodbc.connect(connection_string) as conn:
            conn.execute('DELETE FROM eqsl_users')
            stmt = "INSERT INTO eqsl_users (callsign, date_from) VALUES (?, ?)"
            data = list()
            today = datetime.date.today()
            mylist = csvio.read().strip().splitlines()
            for row in mylist:
                data.append([row.upper(), today])
            with conn.cursor() as cursor:
                cursor.fast_executemany = True
                cursor.executemany(stmt, data)
