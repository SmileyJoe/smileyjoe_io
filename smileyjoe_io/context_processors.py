from smileyjoe_io import settings


def analytics(request):
    return {'GA_TRACKING_ID': settings.GA_TRACKING_ID}
