'''
Addison Huang 
SoftDev1 pd6
K 

'''

from flask import Flask, render_template

app=Flask(__name__)


@app.route("/")
def root():
    print(app)
    return render_template("template.html")

if __name__ == "__main__":
    app.debug = True
    app.run()


