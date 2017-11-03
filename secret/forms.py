from django import forms


class Secret(forms.Form):
    attributes = {'autofocus': 'autofocus',
                  'onblur': 'this.focus()',
                  'maxlength': '256',
                  'title': 'Enter your secret',
                  }
    secret = forms.CharField(label='', widget=forms.TextInput(attrs=attributes))
