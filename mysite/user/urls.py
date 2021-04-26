from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    # path('', views.index),
    url(r'login/login_req/', csrf_exempt(views.login_req)),
    url(r'login/', views.login),
    url(r'home/route_accept/process_accept', views.process_accept),
    url(r'home/route_accept', views.route_accept),
    url(r'home/route_req', views.route_req),
    url(r'home/', views.home),
    url(r'signup/signup_req/', views.signup_req),
    url(r'signup/', views.signup),
    url(r'in_trip/review/', views.feedback),
    url(r'in_trip/', views.in_trip)

]
