'''
Team ScriptKittys

'''
import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="ScriptKittys.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

def students():
    command = "CREATE TABLE students(name TEXT, age INTEGER, id INTEGER)"          #build SQL stmt, save as string
    c.execute(command)    #run SQL statement
    with open('data/peeps.csv', newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['name'],row['age'],row['id'])
            command2 = "INSERT INTO students VALUES(\""+row['name']+"\","+ row['age']+","+row['id']+")" 
            c.execute(command2)

def grades():
    command = "CREATE TABLE grades(code TEXT, mark INTEGER, id INTEGER)"          #build SQL stmt, save as string
    c.execute(command)    #run SQL statement
    with open('data/courses.csv', newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['code'],row['mark'],row['id'])
            command2 = "INSERT INTO grades VALUES(\""+row['code']+"\","+ row['mark']+","+row['id']+")" 
            c.execute(command2)

grades()    
students()
#==========================================================

db.commit() #save changes
db.close()  #close database


