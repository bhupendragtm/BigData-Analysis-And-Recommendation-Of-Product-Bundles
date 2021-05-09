from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UserCreationForm,UserLoginForm
import json

# Create your views here.
def Register(request):
    if request.method == "POST":
        result = request.body
        #decode the byte into string
        result = result.decode("utf-8")
        #convert string into python dict
        result = json.loads(result)
        form = UserCreationForm(result)
        if form.is_valid():
            user = form.save(commit=False)
            user.username=result["email"]
            user.set_password(form.cleaned_data["password1"]) #or , user.set_password(result["password1"])
            user.save()
            auth.login(request,user)
            return JsonResponse({'success':True})
    
    else:
        form = UserCreationForm()
    
    context = {'form':form}
    html_form = render_to_string('account/partial_user_registration.html',context,request=request)
    return JsonResponse({'html_form':html_form})

def Login(request):
    if request.method == "POST":
        result = request.body 
        result = result.decode("utf-8")
        result = json.loads(result)
        form = UserLoginForm(result)
        if form.is_valid():
            user = User.objects.get(username = form.cleaned_data["email"])
            auth.login(request,user)
            return JsonResponse({'success':True})
    else:
        form = UserLoginForm()

    context = {'form':form}
    html_form = render_to_string('account/partial_user_login.html',context,request=request)
    return JsonResponse({'html_form':html_form})


def Logout(request):
    auth.logout(request)
    return redirect('homepage')