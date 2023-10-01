import sqlite3

def connectDB(name):
    # connect to a SQLite data base
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    return conn,cursor


def createDB(cursor):
    # create a table
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS people(
                    id INTEGER PRIMARY KEY,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    age INTEGER
                ) 
                   ''')
def readDB(cursor):
    # read all data from table
    
    cursor.execute('SELECT * FROM people')
    return cursor.fetchall()

def queryAge(cursor):
    cursor.execute('SELECT age FROM people')
    return cursor.fetchall()

def queryFirst_name(cursor):
    cursor.execute('SELECT first_name FROM people')
    return cursor.fetchall()


def queryPerson(cursor, name):
    query_string = '''
        SELECT * FROM people where first_name = '{}'
    '''.format(name)
    cursor.execute(query_string)
    return cursor.fetchall()

def updateDB(cursor,id,first_name,last_name,age):
    # update student info
    updatequery = '''
    UPDATE people 
    SET first_name= '{}',
    last_name = '{}',
    age = '{}' 
    WHERE id = '{}'
    '''.format(first_name,last_name,age,id)
    cursor.execute(updatequery)


def deleteDB(cursor,id):
    # delete a data from table
    cursor.execute('DELETE FROM people WHERE id = ?',(id,))
    
def insertDB(cursor,id,first_name,last_name,age):
     cursor.execute('''INSERT INTO people VALUES (?,?,?,?)''',(id,first_name,last_name,age))
    