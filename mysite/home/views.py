from django.shortcuts import render
from client.views import ClientForm

# Create your views here.
def index(request):
    client_form = ClientForm()
    return render(request,"home/home.html",{"client_form":client_form})