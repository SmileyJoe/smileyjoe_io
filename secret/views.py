from django.core.exceptions import ObjectDoesNotExist
from secret import forms
from secret.models import Secret
import random
import string
from django.http import JsonResponse
from utils.analytics import Analytics
from utils import view

analytics = Analytics()


# Create your views here.
def index(request, id=None):
    global analytics
    analytics.set_request(request)
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
    display_data = {'form_secret': forms.Secret()}
    return view.display_secret(request, page='index.html', data=display_data, ga_page='/')


def load_link(request):
    global analytics
    form = forms.Secret(request.POST)

    if form.is_valid():
        analytics.secret(Analytics.ACTION_FORM_SECRET, Analytics.LABEL_VALID)
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
                analytics.secret(Analytics.ACTION_VIEW, Analytics.LABEL_LINK)
    else:
        analytics.secret(Analytics.ACTION_FORM_SECRET, Analytics.LABEL_INVALID)
        secret_link = "Something went wrong"

    display_data = {'secret_link': secret_link}
    return view.display_secret(request, page='secret_link.html', data=display_data, ga_page='secret_link/')


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
    return view.display_secret(request, page='secret_display.html', ga_page='secret_display/')


def generate_id():
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


def get_secret(id):
    global analytics
    try:
        secret = Secret.objects.get(id=id)
        analytics.secret(Analytics.ACTION_VIEW, Analytics.LABEL_SECRET)
        return secret
    except ObjectDoesNotExist:
        analytics.secret(Analytics.ACTION_VIEW, Analytics.LABEL_UNKNOWN)
        return None
