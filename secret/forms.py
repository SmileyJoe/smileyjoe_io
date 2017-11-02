from django import forms


class Secret(forms.Form):
    secret = forms.CharField(label='', widget=forms.TextInput(attrs={'autofocus': 'autofocus', 'onblur': 'this.focus()',
                                                                     'maxlength': '256'}))
