from handlers.base import BaseHandler
from model.user import User


class MainHandler(BaseHandler):
    def get(self):
        self.render("base.html")
