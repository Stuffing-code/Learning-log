from django.shortcuts import render

# Create your views here.

def index(request):
    """Home page application Learning lof"""
    return render(request, 'learning_logs/index.html')
    