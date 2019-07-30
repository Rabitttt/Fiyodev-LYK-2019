from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from users.models import UserTable
from django import forms
from team.models import Team


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserTable

        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','telephone','birthday','location','profile_picture','biography','social_media','skills')
        #fields = UserCreationForm.Meta.fields + ('username',)



class UserLoginForm(AuthenticationForm):
        username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'username'}))
        password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'password'}))

        class Meta:
            model = AuthenticationForm
            AuthenticationFormFields = ('username', 'password')
