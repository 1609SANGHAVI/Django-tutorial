from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from home.serializers import PeopleSerializer
# from .models import UserDetails
from .models import UserDetails
from .serializers import PeopleSerializer
from .serializers import LoginSerializer
from rest_framework import status
from home.utils import send_customer_login_email 
from django.contrib.auth.models import User 
# Create your views here.
def index(request):
    likes=[
        {"color":"green"},
        {"color":"blue"},
        {"flavors":"chocolate"},
        {"welecome to news world!"}
    
    ]
    return render(request,'index.html',context={'likes':likes})
    # return HttpResponse("Welcome to the homepage to learn more about django")
    
def about(request):
    return HttpResponse("this about page tell us the services provided by us to get more valuable information move to contact page")
def services(request):
    return HttpResponse("These are the features provided in django")
def contact(request):
    return HttpResponse("To Know more information in detial contact us")


#backend
@api_view(['GET','POST','PUT'])
def api_index(request):
    user_details = {
        "name": "jimin",
        "age": "29",
        "working": "South Korean singer, songwriter",
        "passion": "dance"
    }
    if request.method=='GET':
        print("You been in hit by GET Method")
        return Response({
        "message": "This is a user details in DRF response (GET)",
        "data": user_details
            })
           
    elif request.method=='POST':
        print("You been in hit by POST Method")
        return Response({
        "message": "This is a user details in DRF response (POST)",
        "data": user_details
        })
    elif request.method=='PUT':
        print("You been in hit by PUT Method")
        return Response({
        "message": "This is a user details in DRF response (PUT)",
        "data": user_details
        })
    

@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)

    if serializer.is_valid():
        validated_data = serializer.validated_data
        return Response({'message': 'Login Success'}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST','PUT','PATCH','DELETE'])
def user_details(request):
    if request.method == 'GET':
        objs = UserDetails.objects.all()
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'PUT':
        obj = UserDetails.objects.get(id=request.data.get('id'))
        serializer = PeopleSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'PATCH':
        obj = UserDetails.objects.get(id=request.data.get('id'))
        serializer = PeopleSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    # elif request.method == 'DELETE':
    #     try:
    #        obj = UserDetails.objects.get(id=request.data.get('id'))
    #        obj.delete()
    #        return Response({'message': 'User deleted successfully'}, status=204)
    #     except UserDetails.DoesNotExist:
    #         return Response({'error': 'User not found'}, status=404)

    else:
         obj = UserDetails.objects.get(id=request.data.get('id'))
         obj.delete()
         return Response({'message': 'User deleted successfully'}, status=204)

def custom_login(request):
    return render(request, 'login.html')

def my_blog_view(request):
    return render(request, 'blog.html', {'message': 'Hello from custom view!'})

def success_page(request):
    return HttpResponse("<h1>Hi this is success page for how to learn django</h1>")


def create_customer_account_view(request):
    username = 'San1'
    email = 'san1@mailinator.com'
    mobile = '1234567896'
    password = '12345'

    # Check if user already exists
    if User.objects.filter(username=username).exists():
        return HttpResponse("User already exists.")

    # Create user
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    print("✅ Creating user and sending email...")  # DEBUG log

    try:
        send_customer_login_email(user, password, mobile)
    except Exception as e:
        return HttpResponse("User created, but email sending failed.")

    return HttpResponse("Customer account created and email sent!")
