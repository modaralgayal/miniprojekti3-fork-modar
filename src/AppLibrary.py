import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"

        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")

    def create_user(self, title, author,year,publisher,url):
        data = {
            "title": title,
            "author": author,
            "year": year,
            "publisher": publisher,
            "url": url
        }

        requests.post(f"{self._base_url}/book", data=data)
