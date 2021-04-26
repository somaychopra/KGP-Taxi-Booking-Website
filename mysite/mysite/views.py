import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.contrib.sessions.backends.db import SessionStore

def index(request):
    return HttpResponse("Driver aya nahi abhi bhadwe!")
# Create your views here.
def to_login(request):
    return render(request, "welcome.html",{})
