from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserBio
from .forms import UserBioForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

# Create your views here.@login_required
@login_required
def user_bio_view(request, username):
    user = get_object_or_404(User, username=username)
    bio = get_object_or_404(UserBio, user=user)

    return render(request, 'userbio/user_bio.html', {'user_bio': bio, 'user': user})



@login_required
def edit_user_bio(request):
    # Get the logged-in user's bio, or return a 404 if not found
    user_bio = get_object_or_404(UserBio, user=request.user)

    # Handle form submission
    if request.method == 'POST':
        form = UserBioForm(request.POST, request.FILES, instance=user_bio)
        if form.is_valid():
            form.save()
            return redirect('user_bio', username=request.user.username) 
    else:
        form = UserBioForm(instance=user_bio)

    return render(request, 'userbio/edit_bio.html', {'form': form})



@login_required
def delete_profile_picture(request):
    user_bio = get_object_or_404(UserBio, user=request.user)
    
    if request.method == 'POST':
        # Delete Cloudinary image and reset to default
        user_bio.profile_picture.delete(save=False)
        user_bio.profile_picture = 'profile_pics/nobody.jpg'  # Reset to default image path
        user_bio.save()  # Save changes
        messages.success(request, 'Profile picture has been reset to default.')
        return redirect('edit_user_bio')

    return render(request, 'delete_profile_picture.html', {'profile': user_bio})


@login_required
def delete_user(request):
    if request.method == 'POST':
        # Delete the user and redirect to a different page, such as home
        user = request.user
        user.delete()
        return redirect('home')  # Redirect to home after account deletion

    return redirect('edit_bio')  # If not POST, redirect back to edit bio
