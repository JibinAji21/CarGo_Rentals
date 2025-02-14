from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['shop']=uname    #--------------->creating session
                return redirect(shop_home)
            else:
                login(req,data)
                req.session['user']=uname
                return redirect(user_home)
        else:
            messages.warning(req,"Invalid username or password")
            return redirect(shop_login)
    else:
        return render(req,'login.html')
    

def shop_logout(req):
    logout(req)
    req.session.flush()
    return redirect(shop_login)
    
    

def shop_home(req):
    if 'shop' in req.session:
        car=Car_category.objects.all()
        return render(req,'shop/home.html',{'cars':car})
    else:
        return redirect(shop_login)
    

def add_car(req):
    if req.method=='POST':
        id=req.POST['car_id']
        name=req.POST['car_name']
        year=req.POST['car_year']
        place=req.POST['car_place']
        rent=req.POST['car_rent']
        fuel=req.POST['car_fuel']
        file=req.FILES['car_img']
        car_category=req.POST['car_category']
        data=Cars.objects.create(car_id=id,car_name=name,car_year=year,car_place=place,car_rent=rent,car_fuel=fuel,car_img=file,category=car_category)
        data.save()
        return redirect(shop_home)
    return render(req,'shop/addcar.html')


def budget_cars(req,id):
    category = Car_category.objects.get(id=id)
    car_details = Cars.objects.filter(category=category)
    return render(req, 'shop/car_list.html', {'category': category,'car_details':car_details})

def medium_cars(req,id):
    category = Car_category.objects.get(id=id)
    car_details = Cars.objects.filter(category=category)
    return render(req, 'shop/car_list.html', {'category': category,'car_details':car_details})