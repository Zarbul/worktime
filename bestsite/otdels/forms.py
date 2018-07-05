from django import forms
from .models import Otdel

class OtdelsNameForm(forms.ModelForm):

    class Meta:
        model = Otdel
        fields = ('name',)

# class ContactForm(forms.ModelForm):
#
#     class Meta:
#         model = Contact
#         fields = ('type_contact', 'contact',)