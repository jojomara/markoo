from django import forms
from .models import Member

class Member(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'country', 'photo']
   