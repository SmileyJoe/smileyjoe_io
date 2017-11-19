from django.shortcuts import render
from smileyjoe_io import settings


def display(request, **kwargs):
    if 'data' in kwargs:
        data = kwargs['data']
    else:
        data = {}

    if 'ga_page' in kwargs:
        data.update({'GA_PAGE': kwargs['ga_page']})

    data.update({'GA_TRACKING_ID': settings.GA_TRACKING_ID})

    return render(request, kwargs['page'], context=data)
