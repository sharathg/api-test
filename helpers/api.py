import requests


class API:

    def __init__(self, base_url):
        if not base_url.endswith("/"):
            base_url = base_url + "/"
        self.base_url = base_url

    def full_url(self, endpoint):
        endpoint = str(endpoint)
        return "{}{}".format(self.base_url[:-1] if endpoint.startswith("/") else self.base_url, endpoint)

    def get(self, endpoint="", params=None, auth=None):
        return requests.get(self.full_url(endpoint), params=params, auth=auth)

    def delete(self, endpoint="", auth=None):
        return requests.delete(self.full_url(endpoint), auth=auth)

    def post(self, endpoint="", data=None, json=None, files=None, auth=None):
        return requests.post(self.full_url(endpoint), data=data, json=json, files=files, auth=auth)

    def put(self, endpoint="", json=None, auth=None):
        return requests.put(self.full_url(endpoint), json=json, auth=auth)
