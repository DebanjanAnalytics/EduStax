from django.db import models

class Destination(models.Model):
    subject = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    start = models.DateField()
    duration = models.IntegerField()
    started = models.BooleanField(default=False)

class User_Register(models.Model):
    reg_type = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    img = models.ImageField(upload_to='pics')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    guardian_name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    dob = models.DateField()
    course = models.CharField(max_length=40)
    primary_num = models.CharField(max_length=40)
    secondary_num = models.CharField(max_length=40)
