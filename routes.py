import handlers.main


def load():
    default = [
        # Main
        (r"/", handlers.main.MainHandler),
    ]
    return default
