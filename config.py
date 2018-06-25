class Config(object):
    def __init__(self, url, *args, **kwargs):
        if not url or url.isspace():
            raise ValueError('url cannot be null or empty.')
        self.url = url
        kwargs.setdefault('debug',False)
        kwargs.setdefault('verbose',False)
        kwargs.setdefault('delay',1000)
        self.__dict__.update(kwargs)
