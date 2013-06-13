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
    else:pass
        pass

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
    elif qpsnum == "eight":
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
        sevenqps = int(request.form["sevenqps"])
        if sevenqps == 0:
            sevenprice = 0
        elif sevenqps in range(1000,500000):
            sevenprice = price_dict["range(1000,500000)"]
        elif sevenqps in range(500000,1000000):
            sevenprice = price_dict["range(500000,1000000)"]
        elif sevenqps in range(1000000,1500000):
            sevenprice = price_dict["range(1000000,1500000)"]
        elif sevenqps in range(1500000,2000000):
            sevenprice = price_dict["range(1500000,2000000)"]
        elif sevenqps in range(2000000,3000000):
            sevenprice = price_dict["range(2000000,3000000)"]
        elif sevenqps in range(3000000,5000000):
            sevenprice = price_dict["range(3000000,5000000)"]
        elif sevenqps in range(5000000,8000000):
            sevenprice = price_dict["range(5000000,8000000)"]
        elif sevenqps in range(8000000,10000000):
            sevenprice = price_dict["range(8000000,10000000)"]
        elif sevenqps in range(10000000,12000000):
            sevenprice = price_dict["range(10000000,12000000)"]
        elif sevenqps in range(12000000,15000000):
            sevenprice = price_dict["range(12000000,15000000)"]
        elif sevenqps in range(15000000,20000000):
            sevenprice = price_dict["range(15000000,20000000)"]
        else:pass
        sevenprice = int(sevenprice)
        eightqps = int(request.form["eightqps"])
        if eightqps == 0:
            eightprice = 0
        elif eightqps in range(1000,500000):
            eightprice = price_dict["range(1000,500000)"]
        elif eightqps in range(500000,1000000):
            eightprice = price_dict["range(500000,1000000)"]
        elif eightqps in range(1000000,1500000):
            eightprice = price_dict["range(1000000,1500000)"]
        elif eightqps in range(1500000,2000000):
            eightprice = price_dict["range(1500000,2000000)"]
        elif eightqps in range(2000000,3000000):
            eightprice = price_dict["range(2000000,3000000)"]
        elif eightqps in range(3000000,5000000):
            eightprice = price_dict["range(3000000,5000000)"]
        elif eightqps in range(5000000,8000000):
            eightprice = price_dict["range(5000000,8000000)"]
        elif eightqps in range(8000000,10000000):
            eightprice = price_dict["range(8000000,10000000)"]
        elif eightqps in range(10000000,12000000):
            eightprice = price_dict["range(10000000,12000000)"]
        elif eightqps in range(12000000,15000000):
            eightprice = price_dict["range(12000000,15000000)"]
        elif eightqps in range(15000000,20000000):
            eightprice = price_dict["range(15000000,20000000)"]
        else:pass
        eightprice = int(eightprice)
        eightsum = oneprice + twoprice + threeprice + fourprice + fiveprice + sixprice + sevenprice + eightprice
        return render_template("eightsum.html",oneqps=oneqps,oneprice=oneprice,twoqps=twoqps,twoprice=twoprice,threeqps=threeqps,threeprice=threeprice,fourqps=fourqps,fourprice=fourprice,fiveqps=fiveqps,fiveprice=fiveprice,sixqps=sixqps,sixprice=sixprice,sevenqps=sevenqps,sevenprice=sevenprice,eightqps=eightqps,eightprice=eightprice,eightsum=eightsum)
    else:
        
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
        sevenqps = int(request.form["sevenqps"])
        if sevenqps == 0:
            sevenprice = 0
        elif sevenqps in range(1000,500000):
            sevenprice = price_dict["range(1000,500000)"]
        elif sevenqps in range(500000,1000000):
            sevenprice = price_dict["range(500000,1000000)"]
        elif sevenqps in range(1000000,1500000):
            sevenprice = price_dict["range(1000000,1500000)"]
        elif sevenqps in range(1500000,2000000):
            sevenprice = price_dict["range(1500000,2000000)"]
        elif sevenqps in range(2000000,3000000):
            sevenprice = price_dict["range(2000000,3000000)"]
        elif sevenqps in range(3000000,5000000):
            sevenprice = price_dict["range(3000000,5000000)"]
        elif sevenqps in range(5000000,8000000):
            sevenprice = price_dict["range(5000000,8000000)"]
        elif sevenqps in range(8000000,10000000):
            sevenprice = price_dict["range(8000000,10000000)"]
        elif sevenqps in range(10000000,12000000):
            sevenprice = price_dict["range(10000000,12000000)"]
        elif sevenqps in range(12000000,15000000):
            sevenprice = price_dict["range(12000000,15000000)"]
        elif sevenqps in range(15000000,20000000):
            sevenprice = price_dict["range(15000000,20000000)"]
        else:pass
        sevenprice = int(sevenprice)
        eightqps = int(request.form["eightqps"])
        if eightqps == 0:
            eightprice = 0
        elif eightqps in range(1000,500000):
            eightprice = price_dict["range(1000,500000)"]
        elif eightqps in range(500000,1000000):
            eightprice = price_dict["range(500000,1000000)"]
        elif eightqps in range(1000000,1500000):
            eightprice = price_dict["range(1000000,1500000)"]
        elif eightqps in range(1500000,2000000):
            eightprice = price_dict["range(1500000,2000000)"]
        elif eightqps in range(2000000,3000000):
            eightprice = price_dict["range(2000000,3000000)"]
        elif eightqps in range(3000000,5000000):
            eightprice = price_dict["range(3000000,5000000)"]
        elif eightqps in range(5000000,8000000):
            eightprice = price_dict["range(5000000,8000000)"]
        elif eightqps in range(8000000,10000000):
            eightprice = price_dict["range(8000000,10000000)"]
        elif eightqps in range(10000000,12000000):
            eightprice = price_dict["range(10000000,12000000)"]
        elif eightqps in range(12000000,15000000):
            eightprice = price_dict["range(12000000,15000000)"]
        elif eightqps in range(15000000,20000000):
            eightprice = price_dict["range(15000000,20000000)"]
        else:pass
        eightprice = int(eightprice)
        
        nineqps = int(request.form["nineqps"])
        if nineqps == 0:
            nineprice = 0
        elif nineqps in range(1000,500000):
            nineprice = price_dict["range(1000,500000)"]
        elif nineqps in range(500000,1000000):
            nineprice = price_dict["range(500000,1000000)"]
        elif nineqps in range(1000000,1500000):
            nineprice = price_dict["range(1000000,1500000)"]
        elif nineqps in range(1500000,2000000):
            nineprice = price_dict["range(1500000,2000000)"]
        elif nineqps in range(2000000,3000000):
            nineprice = price_dict["range(2000000,3000000)"]
        elif nineqps in range(3000000,5000000):
            nineprice = price_dict["range(3000000,5000000)"]
        elif nineqps in range(5000000,8000000):
            nineprice = price_dict["range(5000000,8000000)"]
        elif nineqps in range(8000000,10000000):
            nineprice = price_dict["range(8000000,10000000)"]
        elif nineqps in range(10000000,12000000):
            nineprice = price_dict["range(10000000,12000000)"]
        elif nineqps in range(12000000,15000000):
            nineprice = price_dict["range(12000000,15000000)"]
        elif nineqps in range(15000000,20000000):
            nineprice = price_dict["range(15000000,20000000)"]
        else:pass
        nineprice = int(nineprice)
        tenqps = int(request.form["tenqps"])
        if tenqps == 0:
            tenprice = 0
        elif tenqps in range(1000,500000):
            tenprice = price_dict["range(1000,500000)"]
        elif tenqps in range(500000,1000000):
            tenprice = price_dict["range(500000,1000000)"]
        elif tenqps in range(1000000,1500000):
            tenprice = price_dict["range(1000000,1500000)"]
        elif tenqps in range(1500000,2000000):
            tenprice = price_dict["range(1500000,2000000)"]
        elif tenqps in range(2000000,3000000):
            tenprice = price_dict["range(2000000,3000000)"]
        elif tenqps in range(3000000,5000000):
            tenprice = price_dict["range(3000000,5000000)"]
        elif tenqps in range(5000000,8000000):
            tenprice = price_dict["range(5000000,8000000)"]
        elif tenqps in range(8000000,10000000):
            tenprice = price_dict["range(8000000,10000000)"]
        elif tenqps in range(10000000,12000000):
            tenprice = price_dict["range(10000000,12000000)"]
        elif tenqps in range(12000000,15000000):
            tenprice = price_dict["range(12000000,15000000)"]
        elif tenqps in range(15000000,20000000):
            tenprice = price_dict["range(15000000,20000000)"]
        else:pass
        tenprice = int(tenprice)
        elevenqps = int(request.form["elevenqps"])
        if elevenqps == 0:
            elevenprice = 0
        elif elevenqps in range(1000,500000):
            elevenprice = price_dict["range(1000,500000)"]
        elif elevenqps in range(500000,1000000):
            elevenprice = price_dict["range(500000,1000000)"]
        elif elevenqps in range(1000000,1500000):
            elevenprice = price_dict["range(1000000,1500000)"]
        elif elevenqps in range(1500000,2000000):
            elevenprice = price_dict["range(1500000,2000000)"]
        elif elevenqps in range(2000000,3000000):
            elevenprice = price_dict["range(2000000,3000000)"]
        elif elevenqps in range(3000000,5000000):
            elevenprice = price_dict["range(3000000,5000000)"]
        elif elevenqps in range(5000000,8000000):
            elevenprice = price_dict["range(5000000,8000000)"]
        elif elevenqps in range(8000000,10000000):
            elevenprice = price_dict["range(8000000,10000000)"]
        elif elevenqps in range(10000000,12000000):
            elevenprice = price_dict["range(10000000,12000000)"]
        elif elevenqps in range(12000000,15000000):
            elevenprice = price_dict["range(12000000,15000000)"]
        elif elevenqps in range(15000000,20000000):
            elevenprice = price_dict["range(15000000,20000000)"]
        else:pass
        elevenprice = int(elevenprice)
        twelveqps = int(request.form["twelveqps"])
        if twelveqps == 0:
            twelveprice = 0
        elif twelveqps in range(1000,500000):
            twelveprice = price_dict["range(1000,500000)"]
        elif twelveqps in range(500000,1000000):
            twelveprice = price_dict["range(500000,1000000)"]
        elif twelveqps in range(1000000,1500000):
            twelveprice = price_dict["range(1000000,1500000)"]
        elif twelveqps in range(1500000,2000000):
            twelveprice = price_dict["range(1500000,2000000)"]
        elif twelveqps in range(2000000,3000000):
            twelveprice = price_dict["range(2000000,3000000)"]
        elif twelveqps in range(3000000,5000000):
            twelveprice = price_dict["range(3000000,5000000)"]
        elif twelveqps in range(5000000,8000000):
            twelveprice = price_dict["range(5000000,8000000)"]
        elif twelveqps in range(8000000,10000000):
            twelveprice = price_dict["range(8000000,10000000)"]
        elif twelveqps in range(10000000,12000000):
            twelveprice = price_dict["range(10000000,12000000)"]
        elif twelveqps in range(12000000,15000000):
            twelveprice = price_dict["range(12000000,15000000)"]
        elif twelveqps in range(15000000,20000000):
            twelveprice = price_dict["range(15000000,20000000)"]
        else:pass
        twelveprice = int(twelveprice)
        twelvesum = oneprice + twoprice + threeprice + fourprice + fiveprice + sixprice + sevenprice + eightprice + nineprice + tenprice + elevenprice + twelveprice
        print oneqps,oneprice,twoqps,twoprice,threeqps,threeprice,fourqps,fourprice,fiveqps,fiveprice,sixqps,sixprice,sevenqps,sevenprice,eightqps,eightprice,nineqps,nineprice,tenqps,tenprice,elevenqps,elevenprice,twelveqps,twelveprice
        return render_template("twelvesum.html",oneqps=oneqps,oneprice=oneprice,twoqps=twoqps,twoprice=twoprice,threeqps=threeqps,threeprice=threeprice,fourqps=fourqps,fourprice=fourprice,fiveqps=fiveqps,fiveprice=fiveprice,sixqps=sixqps,sixprice=sixprice,sevenqps=sevenqps,sevenprice=sevenprice,eightqps=eightqps,eightprice=eightprice,nineqps=nineqps,nineprice=nineprice,tenqps=tenqps,tenprice=tenprice,elevenqps=elevenqps,elevenprice=elevenprice,twelveqps=twelveqps,twelveprice=twelveprice,twelvesum=twelvesum)

if __name__=="__main__":
    app.run(host="0.0.0.0")
    app.debug = True
