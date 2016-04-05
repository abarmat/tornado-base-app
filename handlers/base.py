import tornado.web

import lib.utils as utils


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        # Super charge UI
        self.ui.h = utils

    @property
    def db(self):
        return self.application.db

    def login(self, data):
        self.set_secure_cookie(AUTH_COOKIE, str(data))

    def logout(self):
        self.clear_cookie(AUTH_COOKIE)

    def get_login_url(self):
        self.require_setting("login_url", "@tornado.web.authenticated")
        return self.application.settings["login_url"]
