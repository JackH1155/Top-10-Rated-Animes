from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
class UserBio(models.Model):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bio')
    date_of_birth = models.DateField(null=True, blank=True)
    country = CountryField(blank_label='(select country)', default='US')
    fav_anime = models.TextField(max_length=200, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Bio"
