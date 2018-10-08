#Madison - Max Millar, Addison Huang
#SoftDev1 pd6
#k17 -- average
#2018-10-09


import sqlite3
import csv


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

def findAvg(stuId): #takes in a student id and computes the average of the student
    c.execute("SELECT mark FROM courses WHERE courses.id = '" + str(stuId) + "';")
    grades = c.fetchall()
    sum = 0
    for x in grades: #adds all of the grades together
        sum += int(x[0])
    sum = int(sum / len(grades)) #divides grades by classes
    return sum

def dispStudent(stuId): #displays the information fo a student by their id
    avg = findAvg(stuId) #average
    c.execute("SELECT name FROM peeps WHERE peeps.id = '" + str(stuId) + "';")
    name = c.fetchall() #name
    name = str(name[0]) #name pt2
    name = name[3:len(name) - 3] #Name string splice
    print("Id: " + str(stuId) + "|Name: " + name  + "|Average: " + str(avg)) 

def createTable(): #creates the table of name, id, avg
    c.execute("CREATE TABLE peeps_avg(id INTEGER, avg INTEGER)")
    for x in range(1,11):
        avg = findAvg(x)
        c.execute("INSERT INTO peeps_avg  VALUES(" + str(x) + ", " + str(avg) + ")")

def updateTable(): #updates the table
    c.execute("DROP TABLE peeps_avg")
    c.execute("CREATE TABLE peeps_avg(id INTEGER, avg INTEGER)")
    for x in range(1,11): #adds avg, id, name
        avg = findAvg(x)
        print("INSERT INTO peeps_avg(" + str(x) + ", " + str(avg) + ")")
        c.execute("INSERT INTO peeps_avg VALUES(" + str(x) + ", " + str(avg) + ")")

def addCourse(stu_id, course, grade): #adds a row to the course db
    print("INSERT INTO courses VALUES('" + course + "', " + str(stu_id) + ", '" + str(grade) + ")")
    c.execute("INSERT INTO courses VALUES('" + course + "', '" + str(stu_id) + "', '" + str(grade) + "')")
    updateTable()
    
        
dispStudent(1)
#createTable()
updateTable()
addCourse(1, "ballroom", 1000)

db.commit()
db.close()
