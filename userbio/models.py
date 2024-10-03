from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from cloudinary.models import CloudinaryField

# Create your models here.
class UserBio(models.Model):
    profile_picture = CloudinaryField('image', default='profile_pics/nobody.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bio')
    date_of_birth = models.DateField(null=True, blank=True)
    country = CountryField(blank_label='(select country)', default='US')
    fav_anime = models.TextField(max_length=200, blank=True)
    bio = models.TextField(max_length=300, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Bio"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image', default='default_image_url')

    def reset_profile_picture(self):
        self.profile_picture = 'default_image_url'  # Set this to your default image path
        self.save()