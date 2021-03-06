from . import views
from django.urls import path, re_path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',views.home ,name='home'),
    path('hoods/',views.neighborhood,name='hoods'),
    path('newhood/', views.new_neighborhood, name='newhood'),
    path('profile/<username>/', views.profile, name='profile'),
    path('my_hood/<id>', views.user_hood, name='my_hood'),
    path('leave-hood/<id>', views.leave_hood, name='leave_hood'),
    path('update_hood/<id>/', views.update_hood, name='update_hood'),
    path('newbusiness/<id>/', views.new_business, name='newbusiness'),
    path('delete_business/<id>/<bus_id>/', views.delete_business, name='delete_business'),
    path('newpost/<id>/', views.new_post, name='newpost'),
    path('update_post/<id>/<post_id>/post/', views.update_post, name='update_post'),
    path('delete_post/<id>/<post_id>/', views.delete_post, name='delete_post'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    re_path(r'^search/', views.search_hood, name='search_hood'),
    path('update_business/<id>/<bus_id>/business/', views.update_business, name='update_business'),
    re_path(r'register/',views.register_request, name="register"),
    re_path(r'login/', views.login_request, name="login"),
    re_path(r'logout', views.logout_request, name= "logout"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)