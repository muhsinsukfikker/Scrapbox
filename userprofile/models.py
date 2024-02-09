from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics',blank=True)
    phone_number = models.CharField(max_length=20, blank=True)  # Add this line


    def __str__(self):
        return self.user.username