from django.shortcuts import render
# from app.models import Driver_Data
from app.models import terminal_admin, Driver_Data, atend

from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime,time

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# import pandas as pd
from bs4 import BeautifulSoup 
import requests

# Create your views here.
def homepage(request):
    return render(request,"homepage.html")
def terminal_signup(request):
    return render(request,"terminal_signup.html")
def terminal_login(request):
    return render(request,"terminal_login.html")

def register_admin(request):
    if(request.method=="POST"):
        name=request.POST["name"]
        id=request.POST["id"]
        email=request.POST["email"]
        contact=request.POST["contact"]
        password=request.POST["password"]
        cpassword=request.POST["cpassword"]
        tname=request.POST["tname"]
        chq=terminal_admin.objects.filter(email=email)
        if(chq):
            msg="email already exist"
            return render(request,"Terminal_signup.html",{"msg":msg})
        else:
            if not (password==cpassword):
                msg="password not match"
                return render(request,"Terminal_signup.html",{"msg":msg})
            else:
                terminal_admin(id=id,name=name,email=email,contact=contact,iterm=tname,password=password).save()
                return HttpResponseRedirect("terminal_login")
            




def login(request):
    if(request.method=="POST"):
        email=request.POST["email"]
        password=request.POST["password"]
        chq=terminal_admin.objects.get(email=email)
        if(chq):
            if(password==chq.password):
                request.session['aid']=chq.id
                request.session['aname']=chq.name
                request.session['aemail']=chq.email
                request.session['aiterm']=chq.iterm
                return render(request,"Admin.html")
            else:
                msg="password wrong"
                return render(request,"terminal_login.html",{"msg":msg})
        else:
            msg="wrong email"
            return render(request,"terminal_login.html",{"msg":msg})

#today


def admin(request):
    return render(request,"Admin.html")
#today end

def showdriver(request):
    iterm=request.GET('iterm')

def adddriver(request):
    return render(request,"adddriver.html")

def sendtodriver(request):
    if(request.method=="POST"):
        name=request.POST["name"]
        id=request.POST["id"]
        contact=request.POST["contact"]
        email=request.POST["email"]
        busno=request.POST["busno"]
        iterm=request.POST["iterm"]
        fterm=request.POST["fterm"]
        username=request.POST["username"]
        password=request.POST["password"]
        date=request.POST["date"]
        goingtime=request.POST["time"]
        reachtime=request.POST["reachtime"]
        leavetime=request.POST["leavetime"]
        finaltime=request.POST["finaltime"]
        chq=Driver_Data.objects.filter(email=email)
        if(chq):
            msg="email already registred try another"
            return render(request,'Admin.html',{"msg1":msg})
        else:

            Driver_Data.objects.create(name=name,
                        id=id,
                        contact=contact,
                        email=email,
                        busno=busno,
                        iterm=iterm,
                        fterm=fterm,
                        username=username,
                        password=password,
                        date=date,
                        goingtime=goingtime,
                        reachtime=reachtime,
                        leavetime=leavetime,
                        finaltime=finaltime,
                        ).save()
            
            is_verified=Driver_Data.objects.get(email=email)
            if(is_verified.iterm==""):
                Driver_Data.objects.filter(email=email).delete()
                return render(request,'terminal_login.html')
            else:
                Driver_Data(name=name,id=id,contact=contact,email=email,busno=busno,iterm=iterm,fterm=fterm,username=username,password=password,date=date).save()
                return render(request,"adddriver.html")
def attend(request):
    return render(request,"attend.html")


def mark_attend(request):
    if(request.method=="POST"):
        iterm=request.POST["iterm"]
        id=request.POST["id"]
        date=request.POST["date"]
        name_p=request.POST["formen"]
        bus_p=request.POST["forbus"]
        driver=Driver_Data.objects.get(id=id)
        if(driver):
            if(iterm==driver.iterm):
                atend.objects.create(
                    uid=driver.id,
                    name=driver.name,
                    name_p=name_p,
                    busno=driver.busno,
                    bus_p=bus_p,
                    iterm=iterm,
                    fterm=driver.fterm,
                    date=date,
                    goingtime=driver.goingtime,
                    reachtime=driver.reachtime,
                    leavetime=driver.leavetime,
                    finaltime=driver.finaltime,
                ).save()
                
                msg="marked attendenced"
                return render(request,"attend.html",{"msg":msg})
            else:
                msg="not belongs to these terminal"
                return render(request,"attend.html",{"msg":msg})
        else:
            msg="driver not verified"
            return render(request,"attend.html",{"msg":msg})


def showattend(request):
    iterm=request.GET['iterm']
    today=atend.objects.filter(iterm=iterm).filter(date=datetime.now())
    chq=atend.objects.filter(iterm=iterm)
    return render(request,"showattend.html",{"chq":chq,"today":today})

#########################========DRIVER========##############################

def driver_login(request):
    if(request.method=="POST"):
        username=request.POST["username"]
        password=request.POST["password"]
        chq=Driver_Data.objects.get(username=username)
        if(chq):
            if(password==chq.password):
                request.session['did']=chq.id
                request.session['dname']=chq.name
                request.session['demail']=chq.email
                request.session['diterm']=chq.iterm
                request.session['dfterm']=chq.fterm
                request.session['dbusno']=chq.busno
                # request.session['goingtime']=chq.goingtime
                # request.session['reachtime']=chq.reachtime
                # request.session['leavetime']=chq.leavetime
                # request.session['finaltime']=chq.finaltime
                
                return render(request,"Driver.html")
            else:
                msg="password wrong"
                return render(request,"Driver.html",{"msg":msg})
        else:
            msg="wrong email"
            return render(request,"Driver.html",{"msg":msg})
def driverlogin(request):
    return render(request,"driver_login.html")
            
# def driverhtml(request):
#     return render(request,"Driver.html")

def driverattend(request):
    # if(request.method=="POST"):
    # uid=request.POST["did"]
    uid=request.GET["uid"]
    chq=atend.objects.filter(uid=uid)
    return render(request,"driverattend.html",{"chq":chq})

def index(request):
    return render(request,"index.html")

def showdriver(request):
    iterm=request.GET["iterm"]
    chq=Driver_Data.objects.filter(iterm=iterm)
    return render(request,"showdriver.html",{"chq":chq})
def edit_data(request):
    id=request.GET["id"]
    data1=Driver_Data.objects.filter(id=id)
    for d in data1:
        name=d.name
        contact=d.contact
        email=d.email
        busno=d.busno
        iterm=d.iterm
        fterm=d.fterm
        username=d.username
        password=d.password
        return render(request,"editdata.html",{"id":id,"name":name,"contact":contact,"email":email,"busno":busno,"iterm":iterm,"fterm":fterm,"username":username,"password":password})
def update_data(request):
    if (request.method=="POST"):
        id=request.POST["id"]
        name=request.POST["name"]
        contact=request.POST["contact"]
        email=request.POST["email"]
        busno=request.POST["busno"]
        iterm=request.POST["iterm"]
        fterm=request.POST["fterm"]
        username=request.POST["username"]
        password=request.POST["password"]
        Driver_Data.objects.filter(id=id).update(id=id,name=name,contact=contact,email=email,busno=busno,iterm=iterm,fterm=fterm,username=username,password=password)
        return HttpResponseRedirect("show_data")
def delete_data(request):
    id=request.GET["id"]
    Driver_Data.objects.filter(id=id).delete()
    return HttpResponseRedirect("show_data")
def indexshow(request):
    return render(request,"Admin.html")
def fetchstop(request):
    if(request.method=="POST"):
        i_term=request.POST["initialstop"]
        f_term=request.POST["finalstop"]
        
        iterm=i_term.replace(" ","-")
        fterm=f_term.replace(" ","-")
        url3="https://www.dtcbusroutes.in/bus/routes/from/"+iterm+"/to/"+fterm+"/"
        
        r=requests.get(url3)
        soup=BeautifulSoup(r.text)
        arr=[]
        names=soup.find_all("div",class_="data")
        for i in names:
            arr.append(i.text)
        return render(request,"findrout.html",{"names":arr})
    
#logic for login required mendatory for these page
def asign(request):
    try:
        name=request.session["did"]
        return render(request,"asign.html",{"name":name})
    except:
        return render(request,"driver_login.html")
#without passing data from url

def logoutdriver(request):
    return render(request,"homepage.html")