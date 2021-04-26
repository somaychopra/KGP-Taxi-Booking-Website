import json

from django.shortcuts import render
from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.db import IntegrityError
from . import utils
from django.template import loader
from . import models
from django.contrib.sessions.backends.db import SessionStore
import time

curr_user_email = 'null'
curr_alloted_car = None
curr_alloted_driver = None
curr_distance = 0
curr_booking_id = 0

def index(request):
    return HttpResponse("Hello, world")
# Create your views here.
def login(request):
    return render(request, "login.html",{})


@csrf_exempt
def login_req(request):
    global curr_user_email
    print(request.body)
    body = json.loads(request.body.decode('utf-8'))
    email = body.get("email", "")
    password = body.get("password", "")
    print(email)
    print(password)
    flag, result = utils.validate_password(email,password)
    print(flag,result)
    if flag:
        curr_user_email = email
        result1 = {"success": True, "message": "Badhai Ho" }
    else :
        result1 = {"success": False, "message": result}
    
   # login(request,email)
    return JsonResponse(result1)


def home(request):
    # print("Welcome!!!!!")
    # print(curr_user_email)
    obj = utils.get_user_details(curr_user_email)
    location_list = utils.get_loc_list()
    print(location_list)
    return render(request, "user/home.html",{'details' : obj,'location_list' : location_list})

def signup(request):
    return render(request, "signup.html",{})

@csrf_exempt
def route_req(request):
    global curr_alloted_car
    global curr_alloted_driver
    global curr_distance
    global curr_route
    print("Route requested")
    
    body = json.loads(request.body.decode('utf-8'))
    print(body)
    from_loc = body.get("from","")
    to_loc = body.get("to","")
    car_type = body.get("car_type","")
    flag,result,curr_alloted_car,curr_alloted_driver,curr_route, curr_distance = utils.find_route(from_loc,to_loc,car_type) 
    print(curr_alloted_car)
    if flag:
        result1 = {"success": True, "message": "Badhai Ho" }
    else :
        result1 = {"success": False, "message": result}
    
   # login(request,email)
    return JsonResponse(result1)

@csrf_exempt
def signup_req(request):
    global curr_user_email
    print("aya")
    body = json.loads(request.body.decode('utf-8'))
    email = body.get("email", "")
    name = body.get("name","")
    password = body.get("password", "")
    phone_number = body.get("phone_number")
    age = body.get("age")
    gender=body.get("gender")
    flag, result = utils.add_user(email,password,name,phone_number,age,gender)
    
    if flag:
        result1 = {"success": True, "message": "Badhai Ho" }
    else :
        result1 = {"success": False, "message": result}
    
   # login(request,email)
    return JsonResponse(result1)

@csrf_exempt
def route_accept(request):
    print("Jldi accept krle bsdk")
    global curr_alloted_car
    global curr_alloted_driver
    global curr_distance
    return render(request,"user/accept.html",{'car':curr_alloted_car, 'driver':curr_alloted_driver, 'distance':curr_distance})

@csrf_exempt
def process_accept(request):
    global curr_booking_id
    global curr_alloted_car
    global curr_alloted_driver
    global curr_route
    global curr_user_email
    print("Database me add horyasi")
    
    curr_booking_id = utils.add_booking(curr_alloted_car.number,curr_alloted_driver.email,False,str(int(time.time())),curr_route.route_id,curr_user_email)
    return JsonResponse({'success' : True})

def in_trip(request):
    print("Trip me aa gya")
    status = utils.get_status(curr_booking_id)
    global curr_alloted_car
    global curr_alloted_driver
    global curr_distance
    global curr_route
    print(status)
    if status == "waiting" :
        return render(request,"user/waiting.html",{'driver':curr_alloted_driver,'car':curr_alloted_car,'distance':curr_distance})
    if status == "in_car" :
        return render(request,"user/in_trip.html",{'driver':curr_alloted_driver,'car':curr_alloted_car,'route':curr_route})
    
    return render(request,"user/review.html",{'driver':curr_alloted_driver,'car':curr_alloted_car,'route':curr_route})

@csrf_exempt
def feedback(request):
    print("Feedback de diya")
    global curr_booking_id
    global curr_alloted_driver
    body = json.loads(request.body.decode('utf-8'))
    rating = body.get("rating", "")
    feedback_text = body.get("feedback_text","")
    success, message = utils.register_feedback(curr_booking_id,curr_alloted_driver.email,str(int(time.time())),rating,feedback_text)
    return JsonResponse({'success' : success,'message' : message})
    