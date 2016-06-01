#import pymysql
import sqlite3

def database_read(query, arguments = None):
    connection = _open_connection()
    cursor = connection.cursor()
    if arguments != None:
        cursor.execute(query, arguments)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result

def database_write(query, arguments = []):
    connection = _open_connection()
    cursor = connection.cursor()
    if arguments == []:
        result = cursor.execute(query)
    elif type(arguments[0]) is not list:
        result = cursor.execute(query,arguments)
    else:
        result = cursor.executemany(query,arguments)
    connection.commit()
    connection.close()
    return result

def _open_connection():
    #connection = pymysql.connect(host='localhost',
    #    user = 'recommender_user',
    #    db = 'implicit_recommendation_database',
    #    password = 'Kabbage'
    #    )
    connection = sqlite3.connect('galaxy.db')
    return connection

