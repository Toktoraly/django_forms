from django.shortcuts import render
from booking.models import Booking
# Create your views here.
def booking(request):
    bookings = Booking.objects.filter(active=True)
    return render(request, "booking/booking.html",{"bookings":bookings})

def booking_detail(request,id):
    booking = Booking.objects.get(active=True, id=id)
    return render(request, "booking/booking_detail.html",{"booking":booking})