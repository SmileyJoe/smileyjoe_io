from smileyjoe_io import settings
import requests


class Analytics:

    KEY_VERSION = 'v'
    KEY_TRACKING_ID = 'tid'
    KEY_CLIENT_ID = 'cid'
    KEY_HIT_TYPE = 't'
    KEY_CATEGORY = 'ec'
    KEY_ACTION = 'ea'
    KEY_LABEL = 'el'

    CATEGORY_SECRET = 'secret'

    HIT_EVENT = 'event'

    ACTION_VIEW = 'view'
    ACTION_FORM_SECRET = 'form_secret'

    LABEL_SECRET = 'secret'
    LABEL_LINK = 'link'
    LABEL_UNKNOWN = 'unknown'
    LABEL_VALID = 'valid'
    LABEL_INVALID = 'invalid'

    __url = "http://www.google-analytics.com/collect"
    __args = {KEY_VERSION: 1
              , KEY_TRACKING_ID: settings.GA_TRACKING_ID}

    def set_request(self, request):
        cookie_vars = request.COOKIES.get('_ga').split('.')
        cid = cookie_vars[2] + '.' + cookie_vars[3]
        self.__args.update({self.KEY_CLIENT_ID: cid})

    def event(self):
        self.__args.update({self.KEY_HIT_TYPE: self.HIT_EVENT})

    def category(self, category):
        self.__args.update({self.KEY_CATEGORY: category})

    def action(self, action):
        self.__args.update({self.KEY_ACTION: action})

    def label(self, label):
        self.__args.update({self.KEY_LABEL: label})

    def post(self):
        print(self.__args)
        requests.post(self.__url, data=self.__args)

    def secret(self, action, label):
        self.event()
        self.category(Analytics.CATEGORY_SECRET)
        self.action(action)
        self.label(label)

        self.post()
