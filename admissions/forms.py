from django import forms
from admissions.models import student


class studentmodelform(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'


class vendorform(forms.Form):
    name = forms.CharField(max_length=1000)
    address = forms.CharField(max_length=1000)
    contact = forms.CharField(max_length=1000)
    item = forms.CharField(max_length=1000)
