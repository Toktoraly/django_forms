"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from doctor.views import doctor,doctor_detail
from client.views import client,client_detail
from home.views import index
from django.conf import settings
from django.conf.urls.static import static
from booking.views import booking, booking_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path('doctor/', doctor),
    path('client/', client),
    path('doctor/<int:id>/',doctor_detail),
    path('client/<int:id>/',client_detail),
    path ("booking/", booking),
    path ("booking/<int:id>",booking_detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
