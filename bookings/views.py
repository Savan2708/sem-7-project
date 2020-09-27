from django.shortcuts import render
from doctors.models import Appointment
from userprofile.models import UserProfile


def bookings(request):
    booking = Appointment.objects
    profile = UserProfile.objects
    con = {'booking': booking, 'profile': profile}
    return render(request, 'bookings/bookings.html', con)
