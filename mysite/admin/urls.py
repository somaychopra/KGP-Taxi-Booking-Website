from django.urls import path
# from django.conf.urls import url
from . import views


urlpatterns = [
    # path('', views.index),
    path(r'login/', views.login),
    path(r'login/login_req/', views.login_req),
    path(r'add_car/',views.to_add_car),
    path(r'allocate/',views.to_allocate),
    path(r'add_route/',views.to_add_route),
    path(r'add_location/',views.to_add_location),
    path(r'home/',views.to_admin_options),
    path(r'add_car/add_car_req/',views.add_car_req),
    path(r'add_location/add_location_req/',views.add_location_req),
    path(r'add_route/add_route_req/',views.add_route_req),
    path(r'allocate/allocate_req/',views.allocate_req)
]
