import logging
from exceptions import AgentCreateException

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class AgentService:

    def __init__(self, requests, base_url, auth_token):
        self._requests = requests
        self._base_url = base_url
        self._auth_token = auth_token

    def create(self, organization_id, team_id, first_name, last_name, phone):
        logger.info(
            f'Creating agent. Org ID: {organization_id}. '
            f'Team ID: {team_id}. '
            f'First name: {first_name}. '
            f'Last name: {last_name}. '
            f'Phone: {phone}'
        )

        headers = {
            'Authorization': f'Bearer {self._auth_token}'
        }

        url = f'{self._base_url}/agents'
        data = {
            'organization_id': organization_id,
            'team_id': team_id,
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'order': 1
        }
        response = self._requests.post(url, headers=headers, json=data)

        if response.status_code != 201:
            raise AgentCreateException(
                f'Failed to create agent: {first_name}. '
                f'Response status code: {response.status_code}'
            )

        return response.json()
