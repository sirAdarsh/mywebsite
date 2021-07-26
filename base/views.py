from django.shortcuts import render
from .forms import QueryForm
import sqlite3

# Create your views here.


def home(request):
    form = QueryForm()
    html_page = 'base/home.html'

    if request.method == 'POST':
        
        try:
            print(request.POST)
            form = QueryForm(request.POST)
            if form.is_valid():
                form.save()
                print(request.POST)
                html_page = 'base/success.html'
                
        except:
            html_page = 'base/failure.html'

    context = {'form':form}
    return render(request, html_page, context)

def ed(request):
    return render(request, 'base/education.html')