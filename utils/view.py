from django.shortcuts import render
from smileyjoe_io import settings
from django.contrib.staticfiles.templatetags.staticfiles import static

analytics = """
        <script>
            var GA_PAGE = '{ga_page}';
            var GA_TRACKING_ID = '{ga_tracking_id}';
        </script>
        <script async src='https://www.google-analytics.com/analytics.js'></script>
        <script src='{link_analytics_js}'></script>"""


def display(request, **kwargs):
    if 'data' in kwargs:
        data = kwargs['data']
    else:
        data = {}

    if 'ga_page' in kwargs:
        ga_page = kwargs['ga_page']
    else:
        ga_page = ""

    data.update({'GA_TRACKING_ID': settings.GA_TRACKING_ID})
    data.update({'analytics': analytics.format(
        ga_tracking_id=settings.GA_TRACKING_ID,
        ga_page=ga_page,
        link_analytics_js=static('main/js/analytics.js'))})

    return render(request, kwargs['page'], context=data)
