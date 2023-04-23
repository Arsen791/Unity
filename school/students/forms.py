from django.forms import Form
from django import forms


class CreateNameForm(Form):
    firstname = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}))
    secondname = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter your second name'}))  
class CreateBirthForm(Form):
    date_of_birth = forms.DateField(required=True,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter your date of birth', 'type': 'date'}))
    place_of_birth = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter your place of birth'}))
    
class CreateInfoForm(Form):
    specialization = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}))
    orga_of_education = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}))
    
    year_of_graduation = forms.IntegerField(required=True,
                               widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter your second name', 'type':'number'}))
    
class CreateWorkForm(Form):
    organization = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your organization '}))
    address = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter your place of birth'}))
    
