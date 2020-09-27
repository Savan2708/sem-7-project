from userprofile.models import UserProfile
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from .models import Appointment


def doctors(request):
    profile = UserProfile.objects
    return render(request, 'doctors/doctors.html', {'profile': profile})


def appointment(request, list_id):
    if request.method == 'POST':

        if request.POST['duname'] and request.POST['pfname'] and request.POST['plname'] and request.POST['pemail'] \
                and request.POST['date'] and request.POST['pstate'] and request.POST['pcity'] and request.POST['ppincode'] \
                and request.POST['pphone'] and request.POST['history'] and request.POST['paddress']:

            booking = Appointment()

            booking.duname = request.POST['duname']
            booking.pfname = request.POST['pfname']
            booking.plname = request.POST['plname']
            booking.pemail = request.POST['pemail']
            booking.date = request.POST['date']
            booking.pstate = request.POST['pstate']
            booking.pcity = request.POST['pcity']
            booking.ppincode = request.POST['ppincode']
            booking.pphone = request.POST['pphone']
            booking.history = request.POST['history']
            booking.paddress = request.POST['paddress']
            booking.save()
            return redirect('home')

            profile = UserProfile.objects.get(pk=list_id)

            form = BookForm(request.POST or None, instance=profile)
        else:
            return render(request, 'doctors/appointment.html')

    else:
        profile = UserProfile.objects.get(pk=list_id)
        return render(request, 'doctors/appointment.html', {'profile': profile})
