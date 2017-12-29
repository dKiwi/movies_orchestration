import json

from classes.apicaller import ApiCaller
from classes.postgresconnector import PostgresInserter


def main_insert(film):
    conn_data = json.load(open(r'classes/conn_data.json'))
    host = conn_data['host']
    user = conn_data['user']
    password = conn_data['password']
    database = conn_data['db']
    key = conn_data['api_key']

    caller = ApiCaller(film, key)
    qry = "INSERT INTO movies VALUES ('{}', {}, '{}', '{}')".format(caller.json.get('Title'),
                                                                    caller.json.get('Year'),
                                                                    caller.json.get('Director'),
                                                                    caller.json.get('Country'))

    inserter = PostgresInserter(host,
                                user,
                                password,
                                database,
                                qry)
    inserter.insert()
