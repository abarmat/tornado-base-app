import pylibmc
from tornado.options import options, define


define("cache_servers", default=["127.0.0.1:11211"], help="Memcached servers", type=str, multiple=True)


def connect():
    client = pylibmc.Client(options.cache_servers, binary=True)
    client.behaviors = {
        "tcp_nodelay": True, 
        "no_block": True,
        "ketama": True
    }
    return client

cache = connect()
