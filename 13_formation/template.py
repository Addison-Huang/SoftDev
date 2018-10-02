'''
Addison Huang 
SoftDev1 pd6
K13- ECHO ECHO ECHO
2018-09-28
'''

from flask import Flask, render_template, request

app=Flask(__name__)


@app.route("/")
def root():
    print(app)
    return render_template("template.html")

@app.route("/auth", methods = ["GET", "POST"])
def authenticate():
    print(request)
    print(request.method)
    print(request.args)
    if (request.method == "GET"):
        return render_template("response.html", greeting = "Why hello there",
                           method = request.method,
                           username = request.args["username"],
                           args = request.args)
    return render_template("response.html", greeting = "Why hello there",
                           method = request.method,
                           username = request.form["username"],
                           args = request.args)

if __name__ == "__main__":
    app.debug = True
    app.run()


