'''
Team ScriptKittys -- Mohammed and Addison
Addison Huang
SoftDev1 pd6
K16 -- No Trouble
2018-10-05

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
    with open('data/peeps.csv', newline = '') as csvfile: #opens peep.csv
        reader = csv.DictReader(csvfile) #csvfile stored as iterable 
        for row in reader: #iterates through file
            print(row['name'],row['age'],row['id']) #prints everything out
            command2 = "INSERT INTO students VALUES(\""+row['name']+"\","+ row['age']+","+row['id']+")" #builds table 
            c.execute(command2) #executes build table 

def grades():
    command = "CREATE TABLE grades(code TEXT, mark INTEGER, id INTEGER)"          #build SQL stmt, save as string
    c.execute(command)    #run SQL statement
    with open('data/courses.csv', newline = '') as csvfile: #opens courses.csv
        reader = csv.DictReader(csvfile) #csvfile stored as iterable
        for row in reader: #iterates through file
            print(row['code'],row['mark'],row['id']) #prints everything out
            command2 = "INSERT INTO grades VALUES(\""+row['code']+"\","+ row['mark']+","+row['id']+")"  #builds table
            c.execute(command2) 

grades()    #calls grades
students() #calls students
#==========================================================

db.commit() #save changes
db.close()  #close database


