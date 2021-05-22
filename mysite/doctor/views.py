from django.http.response import HttpResponse
from django.shortcuts import render
from doctor.models import Doctor
from django.forms import ModelForm

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
# Create your views here.
def doctor(request):
    doctor_form= DoctorForm()
    if request.method == "POST":   
        doctor_form = DoctorForm(request.POST,request.FILES)
        if doctor_form.is_valid():
            doctor_form.save()
        
        # name = request.POST.get("doctor_name")
        # surname = request.POST.get("doctor_surname")
        # age = request.POST.get("doctor_age")
        # if name and surname and age:
        #     Doctor.objects.create(name=name, surname=surname, age=age)

    doctors = Doctor.objects.all()
    return render(request,"doctor/doctor.html",{"doctors":doctors,"doctor_form":doctor_form})
    
def doctor_detail(request,id):
    doctor = Doctor.objects.get(id=id)
    return render(request,"doctor/detail.html",{"doctor":doctor})
