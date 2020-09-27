from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    image = models.ImageField(upload_to='imgs/')
    username = models.CharField(max_length=25, null=False)
    email = models.EmailField(max_length=100, null=False)
    fname = models.CharField(max_length=25, null=False)
    lname = models.CharField(max_length=25, null=False)
    service_fields = (
        ('Anesthesiologists', 'Anesthesiologists'),
        ('Ayurvedic', 'Ayurvedic'),
        ('Cardiology', 'Cardiology'),
        ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons'),
        ('Dental', 'Dental'),
        ('Dermatologists', 'Dermatologists'),
        ('Gastroenterologists', 'Gastroenterologists'),
        ('General Surgeons', 'General Surgeons'),
        ('Homeopathic', 'Homeopathic'),
        ('Immunologists', 'Immunologists'),
        ('Neurology', 'Neurology'),
        ('Physiotherapist', 'Physiotherapist'),
        ('Radiologists', 'Radiologists'),
        ('Urologists', 'Urologists'),
        ('Other Services', 'Other Services'),
    )
    service = models.CharField(max_length=30, blank=False, choices=service_fields)
    clinic_name = models.CharField(max_length=100, null=False)
    degree = models.CharField(max_length=25, null=False)
    years = models.IntegerField(null=False, default=1)
    state = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    pincode = models.IntegerField(default=0)
    phone = PhoneNumberField()
    open_time = models.TimeField(blank=False)
    close_time = models.TimeField(blank=False)
    break_start = models.TimeField(blank=False)
    break_end = models.TimeField(blank=False)
    about = models.TextField(max_length=255, null=False)
    address = models.TextField(max_length=255, null=False)

    def __str__(self):
        return self.fname + self.lname
