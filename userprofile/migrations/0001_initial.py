# Generated by Django 3.0.7 on 2020-09-05 14:26

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='imgs/')),
                ('username', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=100)),
                ('fname', models.CharField(max_length=25)),
                ('lname', models.CharField(max_length=25)),
                ('service', models.CharField(choices=[('Anesthesiologists', 'Anesthesiologists'), ('Ayurvedic', 'Ayurvedic'), ('Cardiology', 'Cardiology'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons'), ('Dental', 'Dental'), ('Dermatologists', 'Dermatologists'), ('Gastroenterologists', 'Gastroenterologists'), ('General Surgeons', 'General Surgeons'), ('Homeopathic', 'Homeopathic'), ('Immunologists', 'Immunologists'), ('Neurology', 'Neurology'), ('Physiotherapist', 'Physiotherapist'), ('Radiologists', 'Radiologists'), ('Urologists', 'Urologists'), ('Other Services', 'Other Services')], max_length=30)),
                ('clinic_name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=25)),
                ('years', models.IntegerField(default=1)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField(default=0)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('break_start', models.TimeField()),
                ('break_end', models.TimeField()),
                ('about', models.TextField(max_length=255)),
                ('address', models.TextField(max_length=255)),
            ],
        ),
    ]