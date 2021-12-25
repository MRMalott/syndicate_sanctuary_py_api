import json
import urllib.parse
from base64 import b64encode

from exceptions import AuthTokenException


class AuthTokenService:

    def __init__(
            self,
            requests,
            auth_base_url
    ):
        self._requests = requests
        self._auth_base_url = auth_base_url

    def get_token(self, token_request):
        secret = token_request['secret']

        params = {
            'grant_type': 'client_credentials',
            'scope': ' '.join(token_request['scopes'])
        }
        encoded_params = urllib.parse.urlencode(params)

        url = f'{self._auth_base_url}/oauth2/token?{encoded_params}'

        basicAuth = b64encode(
            f"{secret['client_id']}:{secret['client_secret']}".encode()
        ).decode('ascii')

        headers = {
            'Authorization': f'Basic {basicAuth}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = self._requests.post(url, headers=headers)

        if response.status_code < 200 or response.status_code >= 300:
            raise AuthTokenException(
                f'Failed to get an API token. '
                f'Status code: {response.status_code}. '
                f'Cause: {response.text}'
            )

        return json.loads(response.text)['access_token']