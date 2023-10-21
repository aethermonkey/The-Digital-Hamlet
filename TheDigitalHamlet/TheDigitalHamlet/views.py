from django.shortcuts import render


# Create your views here.
# define the index view
def index(request):
    return render(request, "index.html")