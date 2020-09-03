from django.shortcuts import render


def clinic(request):
    return render(request, 'clinic/clinic.html')