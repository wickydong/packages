#!/usr/bin/env python2.7  
# -*- coding: utf-8 -*-  

from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hi():
    return render_template("index.html")
@app.route("/plus",methods=["POST"])
def plus():
    request_form = request.form["packages"]
    if request_form  == "D_Plus":
        return render_template("sixip.html")
    elif request_form == "D_Extra":
        return render_template("sixip.html")
    elif request_form == "D_Expert":
        return render_template("eightip.html")
    elif request_form == "D_Ultra":
        return render_template("twelveip.html")
    elif request_form == "DP_Plus":
        return render_template("sixip.html")
    elif request_form == "DP_Extra":
        return render_template("sixip.html")
    elif request_form == "DP_Expert":
        return render_template("eightip.html")
    elif request_form == "DP_Ultra":
        return render_template("twelveip.html")
    else:
        return render_template("erro.html")



if __name__=="__main__":
    app.run(host="0.0.0.0")
