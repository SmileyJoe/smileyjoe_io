from smileyjoe_io import settings


def analytics(request):
    ga_code = """
            <!-- Google Analytics -->
            window.ga=window.ga||function(){{(ga.q=ga.q||[]).push(arguments)}};ga.l=+new Date;
            ga('create', '{ga_tracking_id}');
            <!-- End Google Analytics -->
        """.format(ga_tracking_id=settings.GA_TRACKING_ID)
    return {'GA_JS_CODE': ga_code}
