from django.shortcuts import render, HttpResponse, redirect
import requests

# Create your views here.
def index(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'index.html')

def submit(request):
    q = request.POST['ingredients']
    print(request.POST['ingredients'])
    api_response = requests.get(f'https://api.spoonacular.com/recipes/findByIngredients?apiKey=242edaca2243437482a5374c764c9098&ingredients={q}').json()
    request.session['recipes'] = api_response
    return redirect(f'/response')

def response(request):
    context = {
        'recipes': request.session['recipes'],
    }
    return render(request, 'response.html', context)

def create(request):
    return render(request, 'create_plan.html')