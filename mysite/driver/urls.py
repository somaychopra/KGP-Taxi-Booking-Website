from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path(r'login/', views.login),
    path(r'login/login_req/', views.login_req),
    path(r'home/', views.welcome),
    path(r'signup/', views.signup),
    path(r'signup/signup_req/', views.signup_req),
    path(r'set/available/', views.set_available),
    path(r'set/unavailable/', views.set_unavailable),
    path(r'home/set/location/', views.set_location),
    path(r'home/start/', views.start_trip),
    path(r'home/end/', views.end_trip)
]
