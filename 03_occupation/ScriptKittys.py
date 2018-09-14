'''
Team ScriptKittys -- Addison Huang and Daniel Gelfand
SoftDev1 pd6
K#06 -- StI/O: Divine your Destiny!
2018-09-14
'''

import csv #imports csv module
with open('occupations.csv','r') as csvfile: #opens occupations.csv as a readable file saved as variable csvfile
    csvreader = csv.reader(csvfile) #reads the whole file
    next(csvreader) # doesn't read the header
    dict = {rows[0]:float(rows[1]) for rows in csvreader} #creates a dictionary where every even row is a key and every odd is a value    
    
from random import randint

def randJob():

    #select an integer from a range of 1-1000
    rand = randint(1,1000)

    lower = 0
    upper = 0
    #loop through the jobs
    for key in dict:
        #update the upper limit
        upper += (dict[key]*10 + lower)

        #check if random int is within that job percentage range
        if(rand > lower and rand <= upper):
            return key
        else:
        #update the lower limit(placed here bc for first iteration lower should stay 0)
            lower += (dict[key]*10)
