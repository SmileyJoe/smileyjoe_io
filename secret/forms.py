from django import forms


class Secret(forms.Form):
    attributes = {'autofocus': 'autofocus',
                  'onblur': 'this.focus()',
                  'maxlength': '256',
                  'title': 'Enter your secret',
                  'class': 'expand_input input_text'
                  }
    secret = forms.CharField(label='', widget=forms.Textarea(attrs=attributes))
