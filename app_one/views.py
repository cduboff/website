from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def submit(request):
    return HttpResponse("This is a placeholder for processing and returning the API response")