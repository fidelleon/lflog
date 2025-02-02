import datetime
import io

import pyodbc
import requests
import csv


from main import connection_string


class LoTW:
    lotw_users = 'https://lotw.arrl.org/lotw-user-activity.csv'

    @staticmethod
    def update_lotw_users():
        lotw_csv = requests.get(LoTW.lotw_users)
        lotw_csv.raise_for_status()
        csvio = io.StringIO(lotw_csv.text)

        with pyodbc.connect(connection_string) as conn:
            conn.execute('DELETE FROM lotw_users')
            stmt = "INSERT INTO lotw_users (callsign, date_from) VALUES (?, ?)"
            data = list()
            for row in csv.reader(csvio):
                # print(row[0], row[1], row[2])
                data.append([row[0], datetime.datetime.fromisoformat(row[1] + ' ' + row[2])])
            with conn.cursor() as cursor:
                cursor.fast_executemany = True
                cursor.executemany(stmt, data)

    @staticmethod
    def is_lotw_user(callsign: str) -> bool:
        """

        :param callsign: desired callsign
        :return: whether the user is in the list
        """
        with pyodbc.connect(connection_string) as conn:
            answer = conn.execute('SELECT TOP 1 callsign FROM lotw_users WHERE callsign = ?', (callsign,)).fetchval()
            return answer is not None


# LoTW.update_lotw_users()
print(LoTW.is_lotw_user('EA3IEG'))
print(LoTW.is_lotw_user('EA3IEGG'))
