'''
Addison Huang 
SoftDev1 pd6
K 

'''

from flask import Flask, render_template

app=Flask(__name__)


@app.route("/")
def hello_world():
    print (x) #500 and 200 error
    return "<a href= lol> hi </a>" #gives a 404 error if previous line is commented out

if __name__ == "__main__":
    app.debug = True
    app.run()


