from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    username = "Sean"
    return HttpResponse(f"Welcome to {username}'s Tea Shelf")
