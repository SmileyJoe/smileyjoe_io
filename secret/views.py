from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from secret import forms
from secret.models import Secret
import random
import string
from django.http import JsonResponse


# Create your views here.
def index(request, id=None):
    if request.method == 'POST':
        return load_link(request)
    elif id is not None:
        return load_secret(request)
    else:
        return load_form(request)


def api(request, id=None):
    if id is not None:
        return api_load_secret(request, id)


def json_success(data):
    data.update({"meta": {"success": True}})
    return JsonResponse(data)


def load_form(request):
    display_data = {'form_secret': forms.Secret(), 'GA_PAGE': '"/"'}
    return render(request, 'secret/index.html', context=display_data)


def load_link(request):
    form = forms.Secret(request.POST)

    if form.is_valid():
        saved = False

        while not saved:
            id = generate_id()
            secret = get_secret(id)

            if not secret:
                secret = Secret()
                secret.secret = form.cleaned_data['secret']
                secret.id = id
                secret.save()
                saved = True
                secret_link = request.build_absolute_uri() + id
    else:
        secret_link = "Something went wrong"

    display_data = {'secret_link': secret_link, 'GA_PAGE': '"secret_link/"'}
    return render(request, 'secret/secret_link.html', context=display_data)


def api_load_secret(request, id):
    secret = get_secret(id)

    if secret:
        secret_text = secret.secret
        secret.delete()
    else:
        secret_text = "The secret does not exist"

    json = {"data": {"secret": secret_text}}

    return json_success(json)


def load_secret(request):
    display_data = {'GA_PAGE': '"secret_display/"'}
    return render(request, 'secret/secret_display.html', context=display_data)


def generate_id():
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


def get_secret(id):
    try:
        return Secret.objects.get(id=id)
    except ObjectDoesNotExist:
        return None
