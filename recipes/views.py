from django.shortcuts import render
from .models import recipe

def home(request):
    recipes = recipe.objects
    return render(request,'recipes/home.html',{'recipes':recipes})