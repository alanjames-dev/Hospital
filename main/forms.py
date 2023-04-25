from django import forms
from main.models import *
from captcha.fields import CaptchaField

class MyForm(forms.Form):
   captcha=CaptchaField()
   print(captcha)




# class PrescriptionUploadForm(forms.ModelForm):
#     class Meta:
#         model = doctor_prescription
#         fields = ('image',)