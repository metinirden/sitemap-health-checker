class Response(object):
    def __init__(self, url, status_code, elapsed):
        self.url=url
        self.status_code = status_code
        self.elapsed=elapsed