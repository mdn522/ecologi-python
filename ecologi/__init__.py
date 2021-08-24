from typing import Optional

import requests


class Ecologi:
    base_url = "https://public.ecologi.com"

    def __init__(self, auth_token=None):
        self.auth_token = auth_token
        self.session = requests.Session()
        pass

    def request(self, method, endpoint, data=None, idempotency_key=None, auth=False):
        headers = {}

        if idempotency_key:
            headers['Idempotency-Key'] = idempotency_key

        if auth:
            assert self.auth_token
            headers['authorization'] = "Bearer " + self.auth_token

        return self.session.request(method, self.base_url.rstrip('/') + endpoint, json=data, headers=headers).json()

    def purchase_carbon_offsets(self, number: int, units: str, test: Optional[bool] = None, idempotency_key=None):
        assert units in ['KG', 'Tonnes']

        data = {'number': number, 'units': units}

        if test:
            data['test'] = test

        method = 'POST'
        endpoint = '/impact/carbon'

        return self.request(method, endpoint, auth=True, data=data)

    def purchase_trees(self, number: int, name: Optional[str] = None, test: Optional[bool] = None, idempotency_key=None):
        data = {'number': number}

        if name:
            assert len(name) > 0
            data['name'] = name

        if test:
            data['test'] = test

        method = 'POST'
        endpoint = '/impact/trees'

        return self.request(method, endpoint, auth=True, data=data)

    def get_user_trees(self, username):
        method = 'GET'
        endpoint = f'/users/{username}/trees'

        return self.request(method, endpoint)

    def get_user_carbon_offset(self, username):
        method = 'GET'
        endpoint = f'/users/{username}/carbon-offset'

        return self.request(method, endpoint)

    def get_user_impact(self, username):
        method = 'GET'
        endpoint = f'/users/{username}/impact'

        return self.request(method, endpoint)


if __name__ == '__main__':
    ecologi = Ecologi()
