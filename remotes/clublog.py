import datetime
import gzip
import io
import logging

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
        clublog_data = xmltodict.parse(ungzipped.read().decode('utf8'))
        # data['clublog']['entities']['entity'] is a list
        with pyodbc.connect(connection_string) as conn:

            logging.warning('entities')
            conn.execute('DELETE FROM [clublog.entities]')
            entities = clublog_data['clublog']['entities']['entity']
            with conn.cursor() as cursor:
                stmt = "INSERT INTO [clublog.entities] VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                for entity in entities:
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
                    cursor.execute(stmt, to_insert)

                logging.warning('exceptions')
                conn.execute('DELETE FROM [clublog.exceptions]')
                exceptions = clublog_data['clublog']['exceptions']['exception']

                data = list()
                stmt = "INSERT INTO [clublog.exceptions] VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                for exception in exceptions:
                    to_insert = list()
                    to_insert.append(int(exception.get('@record')))
                    to_insert.append(exception.get('call'))
                    to_insert.append(exception.get('entity'))
                    to_insert.append(int(exception.get('adif')))
                    to_insert.append(int(exception.get('cqz', 0)))
                    to_insert.append(exception.get('cont'))
                    to_insert.append(float(exception.get('long', 0)))
                    to_insert.append(float(exception.get('lat', 0)))
                    start = exception.get('start')
                    to_insert.append(datetime.datetime.fromisoformat(start) if start else None)
                    end = exception.get('end')
                    to_insert.append(datetime.datetime.fromisoformat(end) if end else None)
                    data.append(to_insert)
                cursor.fast_executemany = True
                cursor.executemany(stmt, data)

                logging.warning('prefixes')
                conn.execute('DELETE FROM [clublog.prefixes]')
                prefixes = clublog_data['clublog']['prefixes']['prefix']
                data = list()
                stmt = "INSERT INTO [clublog.prefixes] VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                for prefix in prefixes:
                    to_insert = list()
                    to_insert.append(int(prefix.get('@record')))
                    to_insert.append(prefix.get('call'))
                    to_insert.append(prefix.get('entity'))
                    to_insert.append(int(prefix.get('adif')))
                    to_insert.append(int(prefix.get('cqz', 0)))
                    to_insert.append(prefix.get('cont'))
                    to_insert.append(float(prefix.get('long', 0)))
                    to_insert.append(float(prefix.get('lat', 0)))
                    start = prefix.get('start')
                    to_insert.append(datetime.datetime.fromisoformat(start) if start else None)
                    end = prefix.get('end')
                    to_insert.append(datetime.datetime.fromisoformat(end) if end else None)
                    data.append(to_insert)
                cursor.fast_executemany = True
                cursor.executemany(stmt, data)

                logging.warning('invalid')
                conn.execute('DELETE FROM [clublog.invalid]')
                invalid_operations = clublog_data['clublog']['invalid_operations']['invalid']
                data = list()
                stmt = "INSERT INTO [clublog.invalid] VALUES (?, ?, ?, ?)"
                for invalid in invalid_operations:
                    to_insert = list()
                    to_insert.append(int(invalid.get('@record')))
                    to_insert.append(invalid.get('call'))
                    start = invalid.get('start')
                    to_insert.append(datetime.datetime.fromisoformat(start) if start else None)
                    end = invalid.get('end')
                    to_insert.append(datetime.datetime.fromisoformat(end) if end else None)
                    data.append(to_insert)
                cursor.fast_executemany = True
                cursor.executemany(stmt, data)

                logging.warning('zone exceptions')
                conn.execute('DELETE FROM [clublog.zone_exceptions]')
                zone_exceptions = clublog_data['clublog']['zone_exceptions']['zone_exception']
                data = list()
                stmt = "INSERT INTO [clublog.zone_exceptions] VALUES (?, ?, ?, ?, ?)"
                for zone_exception in zone_exceptions:
                    to_insert = list()
                    to_insert.append(int(zone_exception.get('@record')))
                    to_insert.append(zone_exception.get('call'))
                    to_insert.append(int(zone_exception.get('zone', 0)))
                    start = zone_exception.get('start')
                    to_insert.append(datetime.datetime.fromisoformat(start) if start else None)
                    end = zone_exception.get('end')
                    to_insert.append(datetime.datetime.fromisoformat(end) if end else None)
                    data.append(to_insert)
                cursor.fast_executemany = True
                cursor.executemany(stmt, data)
