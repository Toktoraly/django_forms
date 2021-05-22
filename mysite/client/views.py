from django.shortcuts import render
from client.models import Client
from django.forms import ModelForm


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
# Create your views here.
def client(request):
    if request.method == "POST":   
        form = ClientForm(request.POST)
        form.save()
    #     name = request.POST.get("client_name")
    #     surname = request.POST.get("client_surname")
    #     age = request.POST.get("client_age")
    #     if name and surname and age:
    #         Client.objects.create(name=name, surname=surname, age=age)

    clients = Client.objects.all()
    return render(request,"client/client.html",{"clients":clients})

def client_detail(request,id):
    client = Client.objects.get(id=id)
    return render(request,"client/detail.html",{"client":client})