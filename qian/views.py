from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import data
# Create your views here.
print('页面')
def index(request):
    
     return HttpResponse('666')
 