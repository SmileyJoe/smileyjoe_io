from django.shortcuts import render
from secret import forms


# Create your views here.
def index(request, id=None):

    if request.method == 'POST':
        return load_link(request)
    elif id is not None:
        return load_secret(request, id)
    else:
        return load_form(request)


def load_form(request):
    display_data = {'form_secret': forms.Secret()}
    return render(request, 'secret/index.html', context=display_data)


def load_link(request):
    form = forms.Secret(request.POST)

    if form.is_valid():
        display_data = {'secret_link': form.cleaned_data['secret']}
        return render(request, 'secret/secret_link.html', context=display_data)


def load_secret(request, id):
    display_data = {'secret' : id}
    return render(request, 'secret/secret_display.html', context=display_data)