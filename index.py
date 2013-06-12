#!/usr/bin/env python2.7  
# -*- coding: utf-8 -*-  

price_dict = {"range(1000,500000)": "90",
              "range(500000,1000000)": "180",
              "range(1000000,1500000)": "270",
              "range(1500000,2000000)": "360",
              "range(2000000,3000000)": "550",
              "range(3000000,5000000)": "990",
              "range(5000000,8000000)": "1750",
              "range(8000000,10000000)": "2550",
              "range(10000000,12000000)": "3250",
              "range(12000000,15000000)": "4860",
              "range(15000000,20000000)": "7200"}

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

@app.route("/qps",methods=["POST"])
def qps():
    qpsnum = request.form["qpsnum"]
    if qpsnum == "six":
        oneqps = int(request.form["oneqps"])
        if oneqps == 0:
            oneprice = 0
        elif oneqps in range(1000,500000):
            oneprice = price_dict["range(1000,500000)"]
        elif oneqps in range(500000,1000000):
            oneprice = price_dict["range(500000,1000000)"]
        elif oneqps in range(1000000,1500000):
            oneprice = price_dict["range(1000000,1500000)"]
        elif oneqps in range(1500000,2000000):
            oneprice = price_dict["range(1500000,2000000)"]
        elif oneqps in range(2000000,3000000):
            oneprice = price_dict["range(2000000,3000000)"]
        elif oneqps in range(3000000,5000000):
            oneprice = price_dict["range(3000000,5000000)"]
        elif oneqps in range(5000000,8000000):
            oneprice = price_dict["range(5000000,8000000)"]
        elif oneqps in range(8000000,10000000):
            oneprice = price_dict["range(8000000,10000000)"]
        elif oneqps in range(10000000,12000000):
            oneprice = price_dict["range(10000000,12000000)"]
        elif oneqps in range(12000000,15000000):
            oneprice = price_dict["range(12000000,15000000)"]
        elif oneqps in range(15000000,20000000):
            oneprice = price_dict["range(15000000,20000000)"]
        else:pass
        oneprice = int(oneprice)
        twoqps = int(request.form["twoqps"])
        if twoqps == 0:
            twoprice = 0
        elif twoqps in range(1000,500000):
            twoprice = price_dict["range(1000,500000)"]
        elif twoqps in range(500000,1000000):
            twoprice = price_dict["range(500000,1000000)"]
        elif twoqps in range(1000000,1500000):
            twoprice = price_dict["range(1000000,1500000)"]
        elif twoqps in range(1500000,2000000):
            twoprice = price_dict["range(1500000,2000000)"]
        elif twoqps in range(2000000,3000000):
            twoprice = price_dict["range(2000000,3000000)"]
        elif twoqps in range(3000000,5000000):
            twoprice = price_dict["range(3000000,5000000)"]
        elif twoqps in range(5000000,8000000):
            twoprice = price_dict["range(5000000,8000000)"]
        elif twoqps in range(8000000,10000000):
            twoprice = price_dict["range(8000000,10000000)"]
        elif twoqps in range(10000000,12000000):
            twoprice = price_dict["range(10000000,12000000)"]
        elif twoqps in range(12000000,15000000):
            twoprice = price_dict["range(12000000,15000000)"]
        elif twoqps in range(15000000,20000000):
            twoprice = price_dict["range(15000000,20000000)"]
        else:pass
        twoprice = int(twoprice) 
        threeqps = int(request.form["threeqps"])
        if threeqps == 0:
            threeprice = 0
        elif threeqps in range(1000,500000):
            threeprice = price_dict["range(1000,500000)"]
        elif threeqps in range(500000,1000000):
            threeprice = price_dict["range(500000,1000000)"]
        elif threeqps in range(1000000,1500000):
            threeprice = price_dict["range(1000000,1500000)"]
        elif threeqps in range(1500000,2000000):
            threeprice = price_dict["range(1500000,2000000)"]
        elif threeqps in range(2000000,3000000):
            threeprice = price_dict["range(2000000,3000000)"]
        elif threeqps in range(3000000,5000000):
            threeprice = price_dict["range(3000000,5000000)"]
        elif threeqps in range(5000000,8000000):
            threeprice = price_dict["range(5000000,8000000)"]
        elif threeqps in range(8000000,10000000):
            threeprice = price_dict["range(8000000,10000000)"]
        elif threeqps in range(10000000,12000000):
            threeprice = price_dict["range(10000000,12000000)"]
        elif threeqps in range(12000000,15000000):
            threeprice = price_dict["range(12000000,15000000)"]
        elif threeqps in range(15000000,20000000):
            threeprice = price_dict["range(15000000,20000000)"]
        else:pass
        threeprice = int(threeprice)
        fourqps = int(request.form["fourqps"])
        if fourqps == 0:
            fourprice = 0
        elif fourqps in range(1000,500000):
            fourprice = price_dict["range(1000,500000)"]
        elif fourqps in range(500000,1000000):
            fourprice = price_dict["range(500000,1000000)"]
        elif fourqps in range(1000000,1500000):
            fourprice = price_dict["range(1000000,1500000)"]
        elif fourqps in range(1500000,2000000):
            fourprice = price_dict["range(1500000,2000000)"]
        elif fourqps in range(2000000,3000000):
            fourprice = price_dict["range(2000000,3000000)"]
        elif fourqps in range(3000000,5000000):
            fourprice = price_dict["range(3000000,5000000)"]
        elif fourqps in range(5000000,8000000):
            fourprice = price_dict["range(5000000,8000000)"]
        elif fourqps in range(8000000,10000000):
            fourprice = price_dict["range(8000000,10000000)"]
        elif fourqps in range(10000000,12000000):
            fourprice = price_dict["range(10000000,12000000)"]
        elif fourqps in range(12000000,15000000):
            fourprice = price_dict["range(12000000,15000000)"]
        elif fourqps in range(15000000,20000000):
            fourprice = price_dict["range(15000000,20000000)"]
        else:pass
        fourprice = int(fourprice)
        fiveqps = int(request.form["fiveqps"])
        if fiveqps == 0:
            fiveprice = 0
        elif fiveqps in range(1000,500000):
            fiveprice = price_dict["range(1000,500000)"]
        elif fiveqps in range(500000,1000000):
            fiveprice = price_dict["range(500000,1000000)"]
        elif fiveqps in range(1000000,1500000):
            fiveprice = price_dict["range(1000000,1500000)"]
        elif fiveqps in range(1500000,2000000):
            fiveprice = price_dict["range(1500000,2000000)"]
        elif fiveqps in range(2000000,3000000):
            fiveprice = price_dict["range(2000000,3000000)"]
        elif fiveqps in range(3000000,5000000):
            fiveprice = price_dict["range(3000000,5000000)"]
        elif fiveqps in range(5000000,8000000):
            fiveprice = price_dict["range(5000000,8000000)"]
        elif fiveqps in range(8000000,10000000):
            fiveprice = price_dict["range(8000000,10000000)"]
        elif fiveqps in range(10000000,12000000):
            fiveprice = price_dict["range(10000000,12000000)"]
        elif fiveqps in range(12000000,15000000):
            fiveprice = price_dict["range(12000000,15000000)"]
        elif fiveqps in range(15000000,20000000):
            fiveprice = price_dict["range(15000000,20000000)"]
        else:pass
        fiveprice = int(fiveprice)
        sixqps = int(request.form["sixqps"])
        if sixqps == 0:
            sixprice = 0
        elif sixqps in range(1000,500000):
            sixprice = price_dict["range(1000,500000)"]
        elif sixqps in range(500000,1000000):
            sixprice = price_dict["range(500000,1000000)"]
        elif sixqps in range(1000000,1500000):
            sixprice = price_dict["range(1000000,1500000)"]
        elif sixqps in range(1500000,2000000):
            sixprice = price_dict["range(1500000,2000000)"]
        elif sixqps in range(2000000,3000000):
            sixprice = price_dict["range(2000000,3000000)"]
        elif sixqps in range(3000000,5000000):
            sixprice = price_dict["range(3000000,5000000)"]
        elif sixqps in range(5000000,8000000):
            sixprice = price_dict["range(5000000,8000000)"]
        elif sixqps in range(8000000,10000000):
            sixprice = price_dict["range(8000000,10000000)"]
        elif sixqps in range(10000000,12000000):
            sixprice = price_dict["range(10000000,12000000)"]
        elif sixqps in range(12000000,15000000):
            sixprice = price_dict["range(12000000,15000000)"]
        elif sixqps in range(15000000,20000000):
            sixprice = price_dict["range(15000000,20000000)"]
        else:pass
        sixprice = int(sixprice)
        sixsum = oneprice + twoprice + threeprice + fourprice + fiveprice +sixprice
        print oneqps,twoqps,threeqps,fourqps,fiveqps,sixqps,oneprice,twoprice,threeprice,fourprice,fiveprice,sixprice,type(sixprice),sixsum
        
        return render_template("sixsum.html",oneqps=oneqps,oneprice=oneprice,twoqps=twoqps,twoprice=twoprice,threeqps=threeqps,threeprice=threeprice,fourqps=fourqps,fourprice=fourprice,fiveqps=fiveqps,fiveprice=fiveprice,sixqps=sixqps,sixprice=sixprice,sixsum=sixsum)
if __name__=="__main__":
    app.run(host="0.0.0.0")
    app.debug = True
