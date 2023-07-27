from requests import Session, Response


class CustomSession(Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    def request(self, method, url, *args, **kwargs) -> Response:
        return super(CustomSession, self).request(method=method, url=self.base_url + url, *args, **kwargs)


reqres_session = CustomSession('https://api-crs.vodohod.com')
