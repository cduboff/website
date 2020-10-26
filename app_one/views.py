from django.shortcuts import render, HttpResponse, redirect
import requests

# Create your views here.
def index(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'index.html')

def submit(request):
    q = request.POST['ingredients'].replace(" ", "+")
    print(q)
    n = request.POST['number']
    api_response = requests.get(f'https://api.spoonacular.com/recipes/findByIngredients?apiKey=242edaca2243437482a5374c764c9098&ingredients={q}&{n}').json()
    request.session['recipes'] = api_response
    for recipe in api_response:
        print(recipe['id'])
        # use this id to send another request to the api to retreive the actual recipe information. decide whether this is accessible immediately after submitting ingredients or if user will click image for more info about the recipe
    # for i in request.session['recipes']:
    #     requests.get(f'https://api.spoonacular.com/recipes/{i[id]}/information?apiKey=242edaca2243437482a5374c764c9098/')
    return redirect(f'/response')

def response(request):
    context = {
        'recipes': request.session['recipes'],
    }
    return render(request, 'response.html', context)

def create(request):
    return render(request, 'create_plan.html')