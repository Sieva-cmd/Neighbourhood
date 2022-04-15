from . import views
from django.urls import path, re_path

urlpatterns =[
    path('',views.home ,name='home'),
    re_path(r'register/',views.register_request, name="register"),
    re_path(r'login/', views.login_request, name="login"),
    re_path(r'logout', views.logout_request, name= "logout"),
]