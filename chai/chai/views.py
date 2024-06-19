# The Controller File
# This File talks to the data base

from django.http import HttpResponse
from django.shortcuts import render
# methods
def home(request):
    # return HttpResponse("HEllo Chai,Yor are at chai baby")
    return render(request,'index.html')
def about(request):
    return HttpResponse("Hey chai,You are at about page")
def chai(request):
    return HttpResponse("Hey there you are on chai")