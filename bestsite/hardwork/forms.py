from django import forms

from .models import Worker, Contact


class WorkerNameForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ('name', 'fname', 'status',)

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('contact',)