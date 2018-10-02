'''
Firefoxes
Addison Huang Matthew Ming 
SoftDev1 pd6
K15 Oh yes, perhaps I do...
2018-10-03
'''
import os
from flask import Flask, render_template, session, request,url_for,redirect,flash

app=Flask(__name__)
app.secret_key=os.urandom(32)

@app.route("/", methods=["POST","GET"])
def root():
  #checks if you tried logging out
  try:
    if request.form["submit"] == "logout":
      session.pop("username")
      redirect(url_for(root()))
  except:
    #if there is a logged in session
    if (("username" in session)):
      print(session["username"])
      return render_template("welcome.html",
                           greeting = "Successful login,",
                           username = session["username"])
    #if there is no logged in session
    else: 
      return render_template("login.html")
    
@app.route("/auth", methods=["POST"])
def authenticate():
  username = request.form["username"] #username the user gave
  password = request.form["password"] #password the user gave
  if username != "username": #checks if the username is correct
     print("incorrect username")
     flash("incorrect username") #username error if the username is incorrect
     return redirect("/")
  elif password != "password": #checks if the password is correct
     print("incorrect password")
     flash("incorrect password") #password error if the password is incorrect
     return redirect("/")
  else:
    session["username"] = username
    return render_template("welcome.html",
                           greeting = "Successful login,",
                           username = username) #login if the user and password match

if __name__ == "__main__":
  app.debug = True
  app.run()
