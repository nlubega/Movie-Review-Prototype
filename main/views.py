from django.shortcuts import  get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(request):
    all_movies = Movie.objects.all()   # select * from movie
    context = {
        'movies': all_movies,
    }
    return render(request, 'main/index.html', context)

def detail(request, id):
    # movie = Movie.objects.get(id=id)      select * from moive where id = id
    movie = get_object_or_404(Movie, pk=id)
    context = {
        "movie": movie,
    }
    return render(request, 'main/detail.html', context)

# add movies to the database
def add_movies(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form = MovieForm(request.POST or None)
                # check if form is valid
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:home")
            else:
                form = MovieForm()
            return render(request, 'main/addmovies.html', {"form":form, "controller":"Add Movie", "btncolour":"btn btn-success"})
        # if they are not admin
        else:
            return redirect("main:home")
    # if they are not logged in
    else:
        return redirect("accounts:login")

def edit_movies(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            # get the movie linked with id
            movie = Movie.objects.get(id=id)
            # form check
            if request.method == "POST":
                form = MovieForm(request.POST or None, instance=movie)
                # check if form is valie
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:detail", id)
            else:
                form = MovieForm(instance=movie)
            return render(request, 'main/addmovies.html', {"form":form, "controller":"Edit Movie", "btncolour":"btn btn-primary"})
        # if they are not admin
        else:
            return redirect("main:home")
    # if they are not logged in
    else:
        return redirect("accounts:login")

# delete movies

def delete_movies(request, id):
    # get the movie
    movie = Movie.objects.get(id=id)
    # delete the movie
    movie.delete()
    return redirect('main:home')