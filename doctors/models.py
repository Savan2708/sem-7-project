from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Appointment(models.Model):
    duname = models.CharField(max_length=25, null=False)
    pfname = models.CharField(max_length=25, null=False)
    plname = models.CharField(max_length=25, null=False)
    pemail = models.EmailField(max_length=100, null=False)
    date = models.DateField(default=timezone.now)
    pstate = models.CharField(max_length=50, null=False)
    pcity = models.CharField(max_length=50, null=False)
    ppincode = models.IntegerField(default=0)
    pphone = PhoneNumberField()
    history = models.TextField(max_length=255, null=False)
    paddress = models.TextField(max_length=255, null=False)

    def __str__(self):
        return self.pfname + self.plname
