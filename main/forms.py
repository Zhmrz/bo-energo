from django import forms


class CalcForm(forms.Form):
    a = forms.CharField(max_length=10)
    b = forms.CharField(max_length=10)
    c = forms.CharField(max_length=10)


class RandForm(forms.Form):
    num = forms.IntegerField(min_value=0, max_value=100)