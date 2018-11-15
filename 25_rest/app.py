#Addison Huang
#SoftDev1 PD6
#K25: Getting more rest
#2018-11-15

from flask import Flask, render_template
import urllib
import json

app=Flask(__name__)
apikey = "30370a68e63546a520f00a0640a999ac0e911cad"
url = "https://www.calendarindex.com/api/v1/holidays?country=US&year=2018&state=NY&api_key=" #url for new york
user_agent = "Mozilla"
headers={'User-Agent':user_agent,} 

@app.route("/")
def root():
    request=urllib.request.Request(url+apikey,None,headers)
    webURL = urllib.request.urlopen(request)
    data = webURL.read()
    print("---------------")
    print("Data:")
    print(data)
    print("---------------")
    pyth = json.loads(data)
    print("---------------")
    print("Pyth:")
    print(pyth)
    print("---------------")
    response = pyth['response']['holidays']
    print("---------------")
    print("Response:")
    print(response)
    print("---------------")
    
    return render_template("index.html", holidays=response)
    
if __name__ == "__main__":
    app.debug = True
    app.run()
