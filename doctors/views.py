from django.shortcuts import render


def doctors(request):
    return render(request, 'doctors/doctors.html')