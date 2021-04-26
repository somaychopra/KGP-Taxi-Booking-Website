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
from mysite import models
from . import utils
import time

from django.template import loader

from django.contrib.sessions.backends.db import SessionStore

curr_driver_email = 'null'

def index(request):
    return HttpResponse("Hello, world")
# Create your views here.
def login(request):
    return render(request, "driver_login.html",{})


@csrf_exempt
def login_req(request):
    global curr_driver_email
    body = json.loads(request.body)
    email = body.get("email", "")
    password = body.get("password", "")
    flag, result = utils.validate_password(email,password)
    
    if flag:
        #print("Setting global "+ email)
        curr_driver_email = email
        result1 = {"success": True, "message": "Badhai Ho" }
    else :
        result1 = {"success": False, "message": result}
    
   # login(request,email)
    return JsonResponse(result1)


def welcome(request):
    time.sleep(0.1)
    global curr_driver_email
    print("    "+curr_driver_email)
    driver = utils.get_driver_details(curr_driver_email)
    car = None
    curr_loc = []
    if driver.curr_car_number != None:
        car = utils.get_car_details(driver.curr_car_number)
        curr_loc = utils.get_location_from_id(car.current_loc)
    location_list = utils.get_location_list() # add update location
    booking = utils.get_booking(curr_driver_email) # view booking status
    user = None
    loc_start = None
    loc_end = None
    if booking != None:
        loc_start,loc_end,_ = utils.get_route_details(booking.route_id)
        user = utils.get_user_details(booking.user_email)
    #previous_bookings = get_completed_trips(curr_driver_email) #previous history display
    return render(request, "driver_home.html",{'driver':driver, 'location_list':location_list, 'booking':booking, 'car':car,'user':user,'loc_start':loc_start,'loc_end':loc_end,'curr_loc':curr_loc})
    #return HttpResponse("Hello, world FRANDS" )
def set_available(request):
    global curr_driver_email
    utils.set_available(curr_driver_email)
    

def set_unavailable(request):
    global curr_driver_email
    utils.set_unavailable(curr_driver_email)
    
@csrf_exempt
def set_location(request):
    print("In func")
    global curr_driver_email
    body = json.loads(request.body)
    loc = body.get("location_id", "")
    utils.update_location(curr_driver_email,loc)
    result1 = {"success": True, "message": "location updated successfully"}
    
   # login(request,email)
    return JsonResponse(result1)
@csrf_exempt
def start_trip(request):
    global curr_driver_email
    booking = utils.get_booking(curr_driver_email)
    utils.start_trip(booking.booking_id)
    result1 = {"success": True, "message": "Trip Started successfully"}
    
   # login(request,email)
    return JsonResponse(result1)
@csrf_exempt
def end_trip(request):
    global curr_driver_email
    booking = utils.get_booking(curr_driver_email)
    utils.end_trip(booking.booking_id,curr_driver_email)
    result1 = {"success": True, "message": "Trip ended successfully"}
    
   # login(request,email)
    return JsonResponse(result1)

def signup(request):
    return render(request, "driver_signup.html",{})

@csrf_exempt
def signup_req(request):
    global curr_user_email
    #print("aya")
    obj = {}
    body = json.loads(request.body)
    obj['email'] = body.get("email")
    obj['name'] = body.get("name")
    obj['gender'] = body.get("gender")
    obj['age'] = body.get("age")
    obj['password'] = body.get("password")
    obj['phone_number'] = body.get("phone_number")
    obj['rating'] = None
    obj['is_available'] = 1
    obj['curr_car_number'] = None
    flag, result = utils.add_driver(obj)
    
    if flag:
        result1 = {"success": True, "message": "Badhai Ho" }
    else :
        result1 = {"success": False, "message": result}
    
   # login(request,email)
    return JsonResponse(result1)


