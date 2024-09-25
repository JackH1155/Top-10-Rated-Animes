from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserBio
from .forms import UserBioForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_bio_view(request, username):
    user = get_object_or_404(User, username=username)
    bio = get_object_or_404(UserBio, user=user)

    return render(request, 'userbio/user_bio.html', {'bio': bio, 'user': user})


@login_required
def edit_user_bio(request):
    # Get the logged-in user's bio, or return a 404 if not found
    user_bio = get_object_or_404(UserBio, user=request.user)

    # Handle form submission
    if request.method == 'POST':
        form = UserBioForm(request.POST, instance=user_bio)
        if form.is_valid():
            form.save()
            return redirect('user_bio', username=request.user.username) 
    else:
        form = UserBioForm(instance=user_bio)

    return render(request, 'userbio/edit_bio.html', {'form': form})