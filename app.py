from flask import Flask, render_template
app = Flask(__name__) #create instance of class Flask

coll = [0,1,1,2,3,5,8]

@app.route("/") #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__) #where will this go?
    return "No hablo queso!"

@app.route("/my_foist_template")
def func():
    return render_template(
        'template.html',
        foo = "best title",
        collection = coll)

if __name__ == "__main__":
    app.debug = True
    app.run()
