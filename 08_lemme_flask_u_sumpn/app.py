'''
Addison Huang
SoftDev1 pd6
#K08: Fill Yer Flask
2018-09-20
'''

from flask import Flask

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def hello_world():
    print("about to print __name__...") #prints when you refresh
    print(__name__) #prints this in the terminal
    return("No hablo queso!")

@app.route("/home")
def name():
    return("Suh dude. This is Addison here")

@app.route("/cool")
def cool():
    print("I don't like Apple")
    print("apple is a scam")
    print("apple is overhypeddd")
    return("fun factz")

@app.route("/zoo")
def animals():
    print("cats are animals")
    print("dogs are animals")
    return("Dogs are cool. <br> Cats are cooler")

if __name__ == "__main__":
    app.debug = True
    app.run()
