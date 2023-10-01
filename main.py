from mylib.crud import *
import os

def main():
    if os.path.exists("mydb.db"):
        os.remove("mydb.db")
    
    conn, cursor = connectDB("mydb.db")

    #create
    createDB(cursor)
    insertDB(cursor, 1, "jakhsd", "Michael", 19)
    insertDB(cursor, 2, "ad", "Michael", 23)
    insertDB(cursor, 3, "efge", "James", 18)
    insertDB(cursor, 4, "efth", "Hugo", 18)
    insertDB(cursor, 5, "efym", "skj", 18)
    info = readDB(cursor)
    print(info)

    #query1
    age = queryAge(cursor)
    print(age)

    #query2
    first_name = queryFirst_name(cursor)
    print(first_name)

    firstname = "ad"
    person = queryPerson(cursor, firstname)
    print(person)

    #update
    updateDB(cursor, 1, "Ethan", "Q", 33)
    info = readDB(cursor)
    print(info)

    # D
    deleteDB(cursor, 1)
    info = readDB(cursor)
    print(info)


    conn.commit()
    conn.close()

main()