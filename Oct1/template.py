'''
Firefoxes
Addison Huang Matthew Ming 
SoftDev1 pd6
K 

'''
import os
from flask import Flask, render_template, session, request,url_for,redirect

app=Flask(__name__)
@app.route("/")
def root():
    return render_template("template.html")

@app.route("/auth", methods=["POST"])
def authenticate():
    if (request.cookies.get("username")=="user" and request.cookies.get("password")=="pass"):
        return render_template("response.html")
    else:
        return render_template("response.html",
                                   greeting= "The username and password combination didn't match."
                                   ,user=" ")

if __name__ == "__main__":
    app.debug = True
    app.run()


