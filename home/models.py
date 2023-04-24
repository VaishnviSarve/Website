from django.db import models

# Create your models here.
class Home(models.Model):
    firstname=models.CharField(max_length=212)
    emailid=models.EmailField

class Contact(models.Model):
    firstname=models.CharField(max_length=212)
    lastname=models.CharField(max_length=212)
    emailid=models.EmailField
    password=models.CharField(max_length=212)
    mobileno=models.CharField(max_length=212)
    address=models.CharField(max_length=212)
    city=models.CharField(max_length=212)
    state=models.CharField(max_length=212)
    pincode=models.CharField(max_length=212)