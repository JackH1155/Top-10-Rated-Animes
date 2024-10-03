from django import forms
from allauth.account.forms import SignupForm
from .models import UserBio

class CustomSignupForm(SignupForm):
    date_of_birth = forms.DateField(
        required=False, 
        widget=forms.SelectDateWidget(
            years=range(1900, 2025), 
            attrs={'class': 'form-control dob', 'placeholder': 'Select Date of Birth'}
        )
    )
    
    country = forms.CharField(
        required=False, 
        widget=forms.TextInput(
            attrs={'class': 'form-control country', 'placeholder': 'Enter Country'}
        )
    )
    
    fav_anime = forms.CharField(
        max_length=200, 
        required=False, 
        widget=forms.TextInput(
            attrs={'class': 'form-control fav_anime', 'placeholder': 'Enter Favourite Anime'}
        )
    )
    
    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control bio', 'rows': 4, 'placeholder': 'Tell us about yourself'}
        ), 
        max_length=300, 
        required=False
    )

    profile_picture = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file',
            'accept': 'image/*',
        })
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        # Save UserBio data
        UserBio.objects.create(
            user=user,
            date_of_birth=self.cleaned_data.get('date_of_birth'),
            country=self.cleaned_data.get('country'),
            fav_anime=self.cleaned_data.get('fav_anime'),
            bio=self.cleaned_data.get('bio'),
            profile_picture=self.cleaned_data.get('profile_picture')
        )
        return user


from django import forms
from .models import UserBio

class UserBioForm(forms.ModelForm):
    # Customizing the ImageField widget to remove "currently" file name
    profile_picture = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control', 
            'style': 'max-width: 250px;', 
            'initial-text': '',  # Removes the "Currently" text
            'input-text': 'Change',  # Text for "Choose file"
            'clearable': False,  # Optional: to disable "Clear" checkbox if needed
        })
    )

    class Meta:
        model = UserBio
        fields = ['profile_picture', 'date_of_birth', 'country', 'fav_anime', 'bio']
        widgets = {
            'date_of_birth': forms.SelectDateWidget(years=range(1900, 2025)),
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
