'''
Team Track -- Addison Huang and Stefan Tan
SoftDev1 pd6
K10 -- Jinja Tuning
2018-09-21
'''

from flask import Flask, render_template
from util import ants
import csv, random

app=Flask(__name__)


@app.route("/")
def link():
    return "<a href = 'http://127.0.0.1:5000/occupations'> Occupations!</a>"

@app.route("/occupations")
def occupations():
<<<<<<< HEAD
    reader = csv.reader(open('occupations.csv')) #opens and reads the csv file
    next(reader) # skips the headers
    d={} #intialized the dictionary
    for row in reader: #iterates through the csv file and updates the dictionary accordingly
        d[row[0]]=float(row[1])
    occupations = list(d.keys()) #makes a list of all the occupations
    percentages = list(d.values()) #makes a list of all the occuaption
    result = random.choices(occupations, percentages)
    #returns a list of size 1 with a random occupation choosen based on the percentages
=======
>>>>>>> 78a6947b114acd93b714f3968ac2db4f678387b8
    return render_template("template.html",
                           randomOcc = ants.randomizer(ants.occReader()),
                       title ="Occupations in the United States", #the title will be "Occupations in the United States"
                       collection = ants.occReader() #replaces collection in the html
)

if __name__ == "__main__":
    app.debug = True
    app.run()


