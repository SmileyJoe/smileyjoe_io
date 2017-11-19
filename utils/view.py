from django.shortcuts import render
from smileyjoe_io import settings, constant
from utils.analytics import Analytics
from django.contrib.staticfiles.templatetags.staticfiles import static

analytics = """
        <script>
            var GA_PAGE = '{ga_page}';
            var GA_TRACKING_ID = '{ga_tracking_id}';
            var GA_CATEGORY = '{ga_category}';
        </script>
        <script async src='https://www.google-analytics.com/analytics.js'></script>
        <script src='{link_analytics_js}'></script>"""


def display_secret(request, **kwargs):
    return __display(request, constant.SUB_SECRET, **kwargs)


def display_main(request, **kwargs):
    return __display(request, constant.SUB_MAIN, **kwargs)


def __display(request, category, **kwargs):
    if 'data' in kwargs:
        data = kwargs['data']
    else:
        data = {}

    if 'ga_page' in kwargs:
        ga_page = kwargs['ga_page']
    else:
        ga_page = ""

    data.update({'analytics': analytics.format(
        ga_tracking_id=settings.GA_TRACKING_ID,
        ga_page=ga_page,
        ga_category=category,
        link_analytics_js=static('main/js/analytics.js'))})

    data.update({'ga_category_secret': Analytics.CATEGORY_SECRET,
                 'ga_category_main': Analytics.CATEGORY_MAIN})

    page = category + "/" + kwargs['page']

    return render(request, page, context=data)
