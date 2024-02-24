from django.shortcuts import render

# Create your views here.

def home_page(request):
    context = {}
    return render(request, "home.html", context)

def ongoing_page(request):
    context = {}
    return render(request, "ongoing.html", context)

def upcoming_page(request):
    context = {}
    return render(request, "upcoming.html", context)

def game_page(request,id):
    context = {}
    return render(request, "game.html", context)

def player_info_page(request,id):
    context = {}
    return render(request, "player.html", context)