# from django import forms
# from .models import User

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['name']
from django import forms
from .models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'center', 'fathername', 'mothername', 'email', 'phone', 'medium']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add a field for the center selection
        self.fields['center'] = forms.ModelChoiceField(queryset=Center.objects.all(), empty_label=None)
        
        # Customize field labels
        self.fields['name'].label = "Candidate's Name"
        self.fields['fathername'].label = "Father's Name"
        self.fields['mothername'].label = "Mother's Name"
        self.fields['center'].label = "Select Center"
        self.fields['email'].label = "Email ID"
        self.fields['phone'].label = "Contact Number"
        self.fields['medium'].label = "Medium"
class RegistrationNumberForm(forms.Form):
    registration_number = forms.CharField(label='Registration Number', max_length=100)
