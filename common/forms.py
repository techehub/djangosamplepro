import django.forms as forms

class ContactForm (forms.Form) :
    name = forms.CharField(label='Your name', max_length=100)
    phone = forms.CharField(label='Your Phone', max_length=100)
    email = forms.EmailField(label='Your email', max_length=100)
    message = forms.CharField(label='Description' , max_length=250, widget=forms.Textarea())
