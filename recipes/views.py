from django.shortcuts import render
from .models import recipe

recipes = recipe.objects

def home(request):
    return render(request,'recipes/index.html',{'recipes':recipes})

def instruction(request,ID):
    recipe = recipes.get(id = ID)
    return render(request, 'recipes/instructions.html', {'recipe':recipe} )