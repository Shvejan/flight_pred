from flask import Flask, render_template, request
import pandas as pd
import pickle
app = Flask(__name__)

model = pickle.load(open("flight_rf.pkl", "rb"))

@app.route('/', methods=["GET", "POST"])
def home():

    if request.method == "POST":
        date_dep = request.form["dep"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)
        Dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)


        date_arr = request.form["ariv"]
        Arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)





        airline = request.form.get("airline")
        stopage = int(request.form.get("stopage"))
        source = request.form.get("source")
        des = request.form.get("des")


        print(dur_hour)
        print(dur_min)
        print(Arrival_hour)
        print(Arrival_min)
        print(Journey_day)
        print(Dep_hour)


        flights = [0,0,0,0,0,0,0,0,0,0,0]
        src = [0,0,0,0]
        dst = [0,0,0,0,0]


        if(des=="Cochin"):
            dst[0]=1
        elif(des=="Delhi"):
            dst[1]=1
        elif(des=="NDelhi"):
            dst[2]=1
        elif(des=="Hyderabad"):
            dst[3]=1
        elif(des=="Kolkatta"):
            dst[4]=1



        if(source=="Delhi"):
            src[0]=1
        elif(source=="Mumbai"):
            src[1]=1
        elif(source=="Chennia"):
            src[2]=1
        elif(source=="Kolkatta"):
            src[3]=1



        if(airline=="Jet Airways"):
            flights[0]=1
        elif(airline=="IndiGo"):
            flights[1]=1
        elif(airline=="Air India"):
            flights[2]=1
        elif(airline=="Multiple carriers"):
            flights[3]=1
        elif(airline=="SpiceJet"):
            flights[4]=1
        elif(airline=="Vistara"):
            flights[5]=1
        elif(airline=="GoAir"):
            flights[6]=1
        elif(airline=="Multiple carriers Premium economy"):
            flights[7]=1
        elif(airline=="Jet Airways Business"):
            flights[8]=1
        elif(airline=="Vistara Premium economy"):
            flights[9]=1
        elif(airline=="Trujet"):
            flights[10]=1


        answer=model.predict([[
            stopage,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            flights[2],
            flights[6],
            flights[1],
            flights[0],
            flights[8],
            flights[3],
            flights[7],
            flights[4],
            flights[10],
            flights[5],
            flights[9],
            src[2],
            src[0],
            src[3],
            src[1],
            dst[0],
            dst[1],
            dst[3],
            dst[4],
            dst[2]
        ]])


        return render_template('home.html', price=round(answer[0],2))

    return render_template('home.html')
