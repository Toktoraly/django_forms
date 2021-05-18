from django.db import models
from doctor.models import Doctor
from client.models import Client

# Create your models here.



class Diagnoz(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name



class Booking(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    diagnoz = models.ForeignKey(Diagnoz,on_delete=models.CASCADE,null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(self.client,self.diagnoz)
    