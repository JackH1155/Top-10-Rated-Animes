from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserBio
from django.shortcuts import get_object_or_404

# Create your views here.
def user_bio_view(request, username):
    user = get_object_or_404(User, username=username)
    bio = get_object_or_404(UserBio, user=user)

    return render(request, 'userbio/user_bio.html', {'bio': bio, 'user': user})