import requests


class ApiCaller:
    """Retrieve JSON from OMDB API"""

    def __init__(self, title, key):
        self.title = '+'.join(title.lower().split())
        self.key = key

    @property
    def full_url(self):
        return "http://www.omdbapi.com/?t={}&apikey={}".format(self.title, self.key)

    @property
    def json(self):
        response = requests.get(self.full_url)
        if response.status_code == 200:
            return response.json()
