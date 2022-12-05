from urllib import request
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def tessst (request):
    return render (request, 'index.html' )

@csrf_exempt
def login_user(request):

    if request.method == 'POST': 
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request, username=username, password=password)
       if user is not None:
            login(request, user)
            return redirect ('tessst')
       else:
             messages.success(request, ('there was an error , try again'))
             return redirect ('login') 
    else:
        return render (request, 'authenticate/login.html')
 
def logout_user(request):
    logout(request)
    messages.success(request, ('logout successfully'))
    return redirect ('tessst')

    