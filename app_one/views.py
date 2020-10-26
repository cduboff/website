from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'index.html')

def submit(request):
    return redirect('/response')

def response(request):
    return render(request, 'response.html')

def create(request):
    return render(request, 'create_plan.html')