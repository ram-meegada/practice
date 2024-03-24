from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.hashers import check_password, make_password

# Create your views here.
class UserDetails(TemplateView):
    template_name = 'home.html'
    def post(self,request):
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user = User(username=username,first_name=first_name, last_name=last_name, email=email)
        if password == confirm_password:
            user.set_password(password)
            user.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            HttpResponse("password not matching")
        
class LoginUser(TemplateView):
    template_name = 'login.html'
    # def get(self, request):
    #     if not request.user.is_authenticated:
    #         return render(request, self.template_name)
    #     else:
    #         return HttpResponseRedirect(reverse('login'), locals())
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("you are successfully logged in")
        else:
            messages.error(request, f"the credentials u entered r incorrect")   
            return HttpResponseRedirect(reverse('login'))        