from django.shortcuts import render, HttpResponse, redirect
import requests
from .models import User
from django.contrib import messages
import bcrypt
from . import secret

# Create your views here.
def index(request):
    if User in request.session:
        request.session.flush()
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/')
    password = request.POST['password']
    confirm_pw = request.POST['confirm_password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    conf_hash = bcrypt.hashpw(confirm_pw.encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'], username=request.POST['username'], password=pw_hash, confirm_password=conf_hash)
    request.session['name'] = new_user.first_name + ' ' + new_user.last_name
    request.session['user_id'] = new_user.id
    return redirect('/user_home')

def login(request):
    if request.method == 'GET':
        return redirect('/')
    if not User.objects.authenticate(request.POST['username'], request.POST['password']):
        print(request.POST['username'], request.POST['password'])
        messages.error(request, 'Invalid Username or Password')
    if request.method == 'POST':
        logged_user = User.objects.filter(username=request.POST['username'])
        print(logged_user)
        if len(logged_user) > 0:
            logged_user = logged_user[0]
            print(logged_user.password)
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                print(logged_user.password)
                request.session['name'] = logged_user.first_name + ' ' + logged_user.last_name
                request.session['user_id'] = logged_user.id
                return redirect('/user_home')
    return redirect('/')

def user_home(request):
    context = {
        # 'saved': Liked.objects.all(),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'user_home.html', context)

def search(request):
    return render(request, 'index.html')

def submit(request):
    q = request.POST['ingredients'].replace(" ", "+")
    print(q)
    n = request.POST['number']
    api_response = requests.get(f'https://api.spoonacular.com/recipes/findByIngredients?apiKey={secret.api_key}&ingredients={q}&number={n}').json()
    request.session['recipes'] = api_response
    print(request.session['recipes'])
    for recipe in request.session['recipes']:
        # print(recipe['id'])
        print(recipe)
    return redirect(f'/response')

def response(request):
    context = {
        'recipes': request.session['recipes'],
    }
    return render(request, 'response.html', context)

def searchByid(request, id):
    response = requests.get(f'https://api.spoonacular.com/recipes/{id}/information?apiKey={secret.api_key}').json()
    context = {
        'response': response,
    }
    return render(request, 'one_recipe.html', context)

def similar_recipe(request, id):
    response = requests.get(f'https://api.spoonacular.com/recipes/{id}/similar?apiKey={secret.api_key}&number=10').json()
    print(response)
    context = {
        'response': response,
    }
    return render(request, 'similar_recipes.html', context)

def create(request):
    return redirect(f'https://api.spoonacular.com/users/connect?apiKey={secret.api_key}')