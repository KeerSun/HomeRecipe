from django.shortcuts import render
from .models import recipe

recipes = recipe.objects

def home(request):
    return render(request,'recipes/home.html',{'recipes':recipes})

def instruction(request):
    return render(request, 'recipes/instructions.html', {'recipes':recipes} )