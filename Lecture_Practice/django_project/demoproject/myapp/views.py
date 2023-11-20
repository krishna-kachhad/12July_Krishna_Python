from django.shortcuts import render
import random

# Create your views here.
n=0
def index(request):
    global n
    n+=1

    name = 'krishna' #static
    #num = random.randint(111,999)
    return render(request, 'index.html', {'nm':name, 'n':n})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')