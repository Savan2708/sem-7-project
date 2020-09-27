from django.shortcuts import render,redirect
from .models import UserProfile


def userprofile(request):
    if request.method == 'POST':
        if request.FILES['image'] and request.POST['username'] and request.POST['email'] and request.POST['fname'] \
                and request.POST['lname'] and request.POST['service'] and request.POST['clinic_name'] \
                and request.POST['degree'] and request.POST['years'] and request.POST['state'] \
                and request.POST['city'] and request.POST['pincode'] and request.POST['phone'] \
                and request.POST['open_time'] and request.POST['close_time'] and request.POST['break_start'] \
                and request.POST['break_end'] and request.POST['about'] and request.POST['address']:

            profile = UserProfile()

            profile.image = request.FILES['image']
            profile.username = request.POST['username']
            profile.email = request.POST['email']
            profile.fname = request.POST['fname']
            profile.lname = request.POST['lname']
            profile.service = request.POST['service']
            profile.clinic_name = request.POST['clinic_name']
            profile.degree = request.POST['degree']
            profile.years = request.POST['years']
            profile.state = request.POST['state']
            profile.city = request.POST['city']
            profile.pincode = request.POST['pincode']
            profile.phone = request.POST['phone']
            profile.open_time = request.POST['open_time']
            profile.close_time = request.POST['close_time']
            profile.break_start = request.POST['break_start']
            profile.break_end = request.POST['break_end']
            profile.about = request.POST['about']
            profile.address = request.POST['address']
            profile.save()
            return redirect('home')
        else:
            return render(request, 'userprofile/userprofile.html')

    else:
        return render(request, 'userprofile/userprofile.html')
