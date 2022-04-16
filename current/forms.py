from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import Textarea
from .models import Profile,Post,NeighbourHood,Business


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class HoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)
        

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'neighbourhood','profile_pic', 'bio', 'phone_number']
        
        widgets = {
            'bio': Textarea(attrs={'cols': 20, 'rows': 5}),
        }
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('owner', 'neighbourhood')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post']
