from django.contrib.auth import login,logout
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app.EmailBackEnd import EmailBackEnd
from app.models import CustomUser

def Base(request):
    return render(request, 'base.html')
def Home(request):
    return render(request, 'home.html')

def Login(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(
            request,
            username=request.POST.get('email'),
            password=request.POST.get('password'),
        )
        if user is not None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('Hod_home')
            elif user_type == '2':
                return HttpResponse('This is Staff Panel')
            elif user_type == '3':
                return HttpResponse('This is Student Panel')
            else:
                messages.error(request,'Email and Password Are Invalid !')
                return redirect('login')
        else:
            messages.error(request,'Email and Password Are Invalid !')
            return redirect('login')
def Logout(request):
    logout(request)
    return redirect('login')
def profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    context={
       " user":user
    }
    return render(request,'profile.html',context)
def profile_update(request):
    if request.method=="POST":
        profile_pic = request.FILES.get("profile_pic")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        print(profile_pic,first_name,last_name,username,email,password)
        try:
            customer=CustomUser.objects.get(id=request.user.id)
            customer.first_name=first_name
            customer.last_name=last_name
            if password!=None and password!="":
                customer.set_password(password)
            if profile_pic!=None and profile_pic!="":
                customer.profile_pic=profile_pic
            customer.save()
            messages.success(request,"your profile update suceessfully")
            redirect('profile')
        except:
            messages.error(request,"your profile  is not update ")






    return render(request,'profile.html')