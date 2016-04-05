import tornado.web

import model
import settings


class Application(tornado.web.Application):
    def __init__(self):
        # Parse config
        settings.parse()

        # Init database
        self.session_factory = model.create_session_factory()

        # Init
        import routes
        tornado.web.Application.__init__(self, routes.load(), **settings.get_app_settings())

    @property
    def db(self):
        return self.session_factory()
    
    @classmethod
    def instance(cls):
        """Singleton like accessor to instantiate object"""
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance


def instance():
    return Application.instance()
