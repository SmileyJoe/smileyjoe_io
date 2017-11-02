from django import forms


class Secret(forms.Form):
    secret = forms.CharField(widget=forms.Textarea)
