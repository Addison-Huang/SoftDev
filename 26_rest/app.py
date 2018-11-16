'''
Addison Huang 
SoftDev1 pd6
K26

'''

from flask import Flask, render_template
import urllib
import json

app=Flask(__name__)


@app.route("/")
def root():
    dogURL = "https://dog.ceo/api/breed/dhole/images/random"
    webURL = urllib.request.urlopen(dogURL)
    data = webURL.read()
    #print("---------------")
    #print("Data:")
    #print(data)
    #print("---------------")
    dic = json.loads(data)
    #print("---------------")
    #print("Dic:")
    #print(dic)
    #print("---------------")
    img = dic["message"]
    #print("---------------")
    #print("Img:")
    #print(img)
    #print("---------------")
    adviceURL = "https://api.adviceslip.com/advice"
    advURL = urllib.request.urlopen(adviceURL)
    data1 = advURL.read()
    #print("---------------")
    #print("Data:")
    #print(data1)
    #print("---------------")
    dic1 = json.loads(data1)
    #print("---------------")
    #print("Dic:")
    #print(dic1)
    #print("---------------")
    advice = dic1["slip"]["advice"]
    poemURL = "https://www.poemist.com/api/v1/randompoems"
    poeURL = urllib.request.urlopen(poemURL)
    data2 = poeURL.read()
    print("---------------")
    print("Data:")
    print(data2)
    print("---------------")
    dic2 = json.loads(data2)
    print("---------------")
    print("Dic:")
    print(dic2)
    print("---------------")
    poem= dic2[0]["content"]
    return render_template("index.html", dog = img, adv = advice, poe = poem)
    

if __name__ == "__main__":
    app.debug = True
    app.run()


