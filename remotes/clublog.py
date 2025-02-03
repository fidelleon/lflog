import datetime
import gzip
import io

import pyodbc
import requests
import xmltodict

from main import clublog, connection_string


class ClubLog:
    clublog_xml = f"https://cdn.clublog.org/cty.php?api={clublog['api_key']}"

    @staticmethod
    def update_clublog_database():
        answer = requests.get(ClubLog.clublog_xml)
        answer.raise_for_status()
        ungzipped = gzip.GzipFile(fileobj=io.BytesIO(answer.content))
        f = open('my.xml', 'w')
        f.write(ungzipped.read().decode('utf8'))
        ungzipped.seek(0)
        entities = xmltodict.parse(ungzipped.read().decode('utf8'))
        # data['clublog']['entities']['entity'] is a list
        with pyodbc.connect(connection_string) as conn:
            conn.execute('DELETE FROM [clublog.entities]')
            stmt = "INSERT INTO [clublog.entities] VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

            data = list()
            with conn.cursor() as cursor:
                for entity in entities['clublog']['entities']['entity']:
                    to_insert = list()
                    to_insert.append(int(entity.get('adif')))
                    to_insert.append(entity.get('name'))
                    to_insert.append(entity.get('prefix'))
                    to_insert.append(entity.get('deleted'))
                    to_insert.append(int(entity.get('cqz', 0)))
                    to_insert.append(entity.get('cont'))
                    to_insert.append(float(entity.get('long', 0)))
                    to_insert.append(float(entity.get('lat', 0)))
                    start = entity.get('start')
                    to_insert.append(datetime.datetime.fromisoformat(start) if start else None)
                    end = entity.get('end')
                    to_insert.append(datetime.datetime.fromisoformat(end) if end else None)
                    to_insert.append(entity.get('whitelisted', True))
                    whitelist_start = entity.get('whitelist_start')
                    to_insert.append(datetime.datetime.fromisoformat(whitelist_start) if whitelist_start else None)
                    whitelist_end = entity.get('whitelist_end')
                    to_insert.append(datetime.datetime.fromisoformat(whitelist_end) if whitelist_end else None)
                    data.append(to_insert)
                    cursor.execute(stmt, to_insert)
