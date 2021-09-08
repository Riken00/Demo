from email.policy import default
from tkinter.messagebox import NO
from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Other"),)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile',unique=True)

    fname = models.CharField(max_length=100,default=None)
    lname = models.CharField(max_length=100,default=None)
    dob = models.DateField(default=None)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=15,default=1)
    # email = models.EmailField(max_length=256, unique=True,default=None)
    mobile = models.CharField(max_length=10, unique=True)
    profile_pic = models.ImageField(default='default-avatar.png',upload_to='basic_app/profile_pics',blank=True)
    number = models.CharField(max_length=111,default=None,null=True)
    address = models.TextField(max_length=256,default=None)
    city = models.CharField(max_length=128,default=None)    
    zip = models.IntegerField(default=None)
    def __str__(self):
        return self.user.username
