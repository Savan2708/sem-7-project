from django.shortcuts import render
from userprofile.models import UserProfile


def viewprofile(request):
    profile = UserProfile.objects
    return render(request, 'viewprofile/viewprofile.html', {'profile': profile})
