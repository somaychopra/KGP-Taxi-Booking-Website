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

from django.contrib.sessions.backends.db import SessionStore

curr_user_email = 'null'

def index(request):
    return HttpResponse("Hello, world")
# Create your views here.
def login(request):
    return render(request, "admin_login.html",{})
def to_admin_options(request):
    return render(request, "admin_home.html",{})
def to_add_car(request):
    return render(request, "admin_add_car.html",{})
def to_add_route(request):
    loc_list = utils.get_loc_list()
    return render(request, "admin_add_route.html",{'loc_list':loc_list})
def to_add_location(request):
    return render(request, "admin_add_location.html",{})
def to_allocate(request):
    driver_list,car_list = utils.get_driver_car_list()
    return render(request, "admin_allocate.html",{'driver_list':driver_list, 'car_list':car_list})



@csrf_exempt
def login_req(request):
    global curr_user_email
    body = json.loads(request.body)
    print("aya")
    email = body.get("email", "")
    password = body.get("password", "")
    print(email,password)
    flag, result = utils.validate_password(email,password)
    
    if flag:
        curr_user_email = email
        result1 = {"success": True, "message": "Badhai Ho" }
    else :
        result1 = {"success": False, "message": result}
    return JsonResponse(result1)

@csrf_exempt
def add_car_req(request):
    global curr_user_email
    #print("aya")
    body = json.loads(request.body)
    number = body.get("number", "")
    number_seats = body.get("number_seats","")
    model = body.get("model", "")
    flag, result = utils.add_car(number,number_seats,model)
    if flag:
        result1 = {"success": True, "message": "Cab added successfully" }
    else :
        result1 = {"success": False, "message": result}
    return JsonResponse(result1)

@csrf_exempt
def add_location_req(request):
    global curr_user_email
    body = json.loads(request.body)
    location_id = body.get("location_id", "")
    location_name = body.get("location_name","")
    is_outstation = body.get("is_outstation", "")
    flag, result = utils.add_location(location_id,location_name,is_outstation)
    if flag:
        result1 = {"success": True, "message": "Location added successfully" }
    else :
        result1 = {"success": False, "message": result}
    return JsonResponse(result1)

@csrf_exempt
def add_route_req(request):
    global curr_user_email
    body = json.loads(request.body)
    route_id = body.get("route_id", "")
    loc_start = body.get("loc_start","")
    loc_end = body.get("loc_end","")
    distance = body.get("distance", "")
    print(body)
    flag, result = utils.add_route(route_id,loc_start,loc_end,distance)
    if flag:
        result1 = {"success": True, "message": "Route added successfully" }
    else :
        result1 = {"success": False, "message": result}
    return JsonResponse(result1)

@csrf_exempt
def allocate_req(request):
    global curr_user_email
    body = json.loads(request.body.decode('utf-8'))
    driver_email = body.get("driver_email", "")
    car_number = body.get("car_number","")
    flag, result = utils.allocate(driver_email,car_number)
    print("Done")
    if flag:
        result1 = {"success": True, "message": "Car allocated successfully" }
    else :
        result1 = {"success": False, "message": result}
    return JsonResponse(result1)