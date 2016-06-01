#import pymysql
import sqlite3


def _open_connection():
    #connection = pymysql.connect(host='localhost',
    #    user = 'recommender_user',
    #    db = 'implicit_recommendation_database',
    #    password = 'Kabbage'
    #    )
    connection = sqlite3.connect('galaxy.db')
    return connection

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



def initializeDatabase():
    #drop all relevant tables
    database_write('drop table if exists objects')
    #create relevant tables
    database_write('''CREATE TABLE objects (
                                           object_id int,
                                           time double,
                                           x_position float,
                                           y_position float,
                                           z_position float,
                                           mass float)''')
    database_write('''CREATE INDEX time_index on objects ( time )''')
    database_write('''CREATE UNIQUE INDEX time_object_id_index on objects ( time, object_id)''')
    
def writeStatus(positions, masses, currentTime):
    N = len(positions)
    for i in xrange(0,N):
        database_write('''INSERT INTO objects VALUES (?, ?, ?, ?, ?, ?)''',
                                 [i,
                                  currentTime,
                                  positions[i][0],
                                  positions[i][1],
                                  positions[i][2],
                                  masses[i]])