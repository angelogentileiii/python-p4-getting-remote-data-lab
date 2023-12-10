import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return f'GetRequester(URL: {self.url})'
    
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, new_url):
        if not isinstance(new_url, str):
            raise ValueError ('Url must be a string')
        
        self._url = new_url

    def get_response_body(self):
        get_request = requests.get(self.url)
        print (get_request.content)
        return get_request.content

    def load_json(self):
        json_response = []
        load_json = json.loads(self.get_response_body())

        for _ in load_json:
            json_response.append(_)

        return json_response