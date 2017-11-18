from smileyjoe_io import settings


def analytics(request):
    ga_code = """
            <!-- Google Analytics -->
            <script>
            window.ga=window.ga||function(){{(ga.q=ga.q||[]).push(arguments)}};ga.l=+new Date;
            ga('create', '{ga_tracking_id}');
            ga('send', 'pageview');
            </script>
            <script async src='https://www.google-analytics.com/analytics.js'></script>
            <!-- End Google Analytics -->
        """.format(ga_tracking_id=settings.GA_TRACKING_ID)
    return {'GA_JS_CODE': ga_code}
