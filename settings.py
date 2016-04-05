import os.path

from tornado.options import define, options, parse_config_file, parse_command_line

import uimodules


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

define("debug", default=False, help="run for debug", type=bool)
define("daemon", default=False, help="run as daemon", type=bool)
define("config", default=None, help="config file", type=str)

define("template_path", default=None, help="templates path", type=str)
define("static_path", default=None, help="static files path", type=str)

define("xsrf_cookies", default=True, help="use xsrf cookies", type=bool)
define("cookie_secret", default=None, help="cookie secret string", type=str)


class ConfigNotFoundException(Exception):
    pass


def parse():
    parse_command_line()
    if not options.config:
        raise ConfigNotFoundException()
    parse_config_file(options.config)


def get_app_settings():
    return {
        'cookie_secret': options.cookie_secret,
        'xsrf_cookies': options.xsrf_cookies,
        'debug': options.debug,
        'template_path': os.path.join(APP_ROOT, options.template_path),
        'static_path': os.path.join(APP_ROOT, options.static_path),
        'login_url': '/account/login',
        'ui_modules': uimodules        
    }
