import requests
from django.conf import settings


class ProPublicaAPI(object):
    URL = 'https://api.propublica.org/congress/v1/{rest}'

    def __init__(self, api_key=None):
        self.api_key = api_key or settings.PROPUBLICA_API_KEY
        self.auth_headers = {'X-API-Key': self.api_key}

    def search(self, query):
        if not self.api_key:
            return {}
        api_rest = 'bills/search.json?query="{query}"'.format(query=query)
        response = requests.get(self.URL.format(rest=api_rest), headers=self.auth_headers)
        response.raise_for_status()
        return response.json()

    def get_by_id(self, bill_id):
        if not self.api_key:
            return {}

        bill_id, congress = bill_id.split('-')
        api_rest = "{congress}/bills/{bill_id}.json".format(congress=congress, bill_id=bill_id)
        response = requests.get(self.URL.format(rest=api_rest), headers=self.auth_headers)
        response.raise_for_status()
        return response.json()
