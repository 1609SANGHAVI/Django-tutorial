from django.contrib import admin
from django.urls import path
# from home import views
# from home.views import custom_login
from . import views




urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path('api/', views.api_index, name='api_index'),
    path('login/', views.login, name='login'),
    path('user_details',views.user_details,name='user_details'),
    path('custom-login/',views.custom_login, name='custom_login'),
    path('my_blog_view/', views.my_blog_view, name='blog_view'),
    path('success_page/', views.success_page, name='success_page'),
    path('create-customer/',views.create_customer_account_view),

  
    


]
