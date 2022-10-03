from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return HttpResponse('Homepage')
 
def login(request):
    return render(request, 'login.html')
 
@login_required
def home(request):
    return render(request, 'home.html')