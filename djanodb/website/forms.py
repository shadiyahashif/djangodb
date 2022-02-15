from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [ 'f_name', 'l_name' , 'email' , 'password' , 'age']