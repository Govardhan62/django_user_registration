from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def home(request):
    return render(request,'home.html')

def table(request):
    return render(request,'table.html')

def inside(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('table')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('inside')

    return render(request,'inside.html')

def enter(request):
    if request.method == 'POST':
        first_name =request.POST['first_name']
        last_name=request.POST['last_name']
        username =request.POST['username']
        email =request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']

        if password1 ==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is already taken")
                return redirect('enter')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is already taken")
                return redirect('enter')
            else:  
              user =User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1,email=email)
              user.save()
              return redirect('inside')
        else:
            messages.success(request,"Password does not match")
            return redirect('enter')
    
    return render(request,'enter.html')


def logout(request):
    return redirect('home')
