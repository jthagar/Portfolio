from django.shortcuts import render
from django.http import HttpResponse
# add items up here


# create context for items here
items = [
    # add items/models here to show on a page
]

# Create your views here.
def home(request):
    context = {
        'items' : items
    }
    return render(request, 'base/index.html')  # add context at the end here

def about(request):
   return render(request, 'base/about.html')

def hireme(request):
    return render(request, 'base/hire-me.html')

def ceevee(request):
    return render(request, 'base/cv.html')

def projects(request):
    return render(request, 'base/projects-grid-cards.html')