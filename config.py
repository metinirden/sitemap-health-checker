class Config(object):
    def __init__(self, url, **kwargs):
        if not url or url.isspace():
            raise ValueError('url cannot be null or empty.')
        self.url = url
        kwargs.setdefault('debug', False)
        kwargs.setdefault('delay', 1)
        kwargs.setdefault('output', 'json')
        kwargs.setdefault('headers', {'User-Agent': 'sitemap-health-checker'})
        self.__dict__.update(kwargs)