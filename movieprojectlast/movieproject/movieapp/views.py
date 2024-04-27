
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth

from .filter import MovieFilter
from .forms import MovieForm
from .models import Movie


# Create your views here.
# def index(request):
#     movie = Movie.objects.all()
#     context = {'mlist': movie}
#     return render(request, 'index.html', context)
def index(request):

    movie = MovieFilter(request.GET, queryset=Movie.objects.all()).qs
    print(movie)
    return render(request, 'index.html', {'mlist': movie})


def details(request, movie_id):
    result = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': result})


def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('movieadded')
        else:
            print(form.errors)
        return redirect('/')

    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(instance=movie)
    if request.method=='POST':
        form = MovieForm(request.POST,request.FILES,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['password']
        try:
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'username taken')
                    return redirect('movieapp:register')

                else:
                    user = User.objects.create_user(username=username,
                                                    password=password)
                    user.save()
                    print("user registered")
                    messages.info(request, "user registered")
                    return redirect('movieapp:login')

            else:
                messages.info(request, 'password not matching')
                return redirect('movieapp:register')
        except:
            messages.info(request, 'username is mandatory')
            return redirect('movieapp:register')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('movieapp:index')
        else:
            messages.info(request, 'invalid')
            return redirect('movieapp:login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('movieapp:index')


def newpage(request):
    return render(request, 'new.html')


def movie_list(request):
    filter = MovieFilter(request.GET, queryset=Movie.objects.all())
    return render(request, 'filter.html', {'filter': filter})
