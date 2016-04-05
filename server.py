#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
from app import Application


define('addr', default='0.0.0.0', help='run on the given address', type=str)
define('port', default=8000, help='run on the given port', type=int)

def main():
    try:
        # Start server
        http_server = tornado.httpserver.HTTPServer(Application.instance(), xheaders=True)
        http_server.bind(options.port, address=options.addr)
        http_server.start()

    	# Attach handlers to IOLoop
        ioloop = tornado.ioloop.IOLoop.instance()
        ioloop.start()

    except:
        tornado.options.print_help()
        raise

if __name__ == '__main__':
    main()
