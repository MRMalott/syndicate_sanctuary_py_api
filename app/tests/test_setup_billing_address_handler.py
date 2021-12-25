import unittest
import unittest.mock
import requests
import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
import jwt
from auth_token_service import AuthTokenService
from aws_secret_service import AwsSecretService
from setup_billing_address_handler import setup_billing_address  # noqa: E402
from user_service import UserService

@unittest.mock.patch.dict(os.environ, {
    'AWS_SECRETS_REGION': 'us-east-1', 'MESSAGING_SERVICE_URL': 'http://hax.com',
    'AUTH_SECRET_ID': 'secret', 'SALES_SERVICE_URL': 'http://foo.com', 'AUTH_SERVICE_URL': 'http://bar.com'
})
class TestApp(unittest.TestCase):
    
    @unittest.mock.patch.object(AwsSecretService, 'get_secret')
    @unittest.mock.patch.object(AuthTokenService, 'get_token')
    @unittest.mock.patch.object(UserService, 'get_by_cognito_id')
    @unittest.mock.patch.object(requests, 'post')
    @unittest.mock.patch.object(jwt, 'decode')
    def test__setup_billing_address__success(
        self, mock_jwt, mock_post, mock_get_user, mock_get_token, mock_get_secret
    ):
        mock_post.return_value = unittest.mock.Mock(**{'ok.return_value': True, 'text.return_value': ''})
        mock_get_secret.return_value = 'secret'
        mock_get_token.return_value = 'token'
        mock_get_user.return_value ={'organization_id': '123'}
        mock_jwt.return_value = {'sub': '123'}

        event = {
            'body': json.dumps({
                "address_line_one": "1234 St",
                "address_line_two": "Ste 1",
                "city": "Lenexa",
                'region': 'Kansas',
                'postal_code': '12345',
                'country': 'US'
            }),
            'headers': {'Authorization': 'bearer jwt'}
        }
        context = ''

        response = setup_billing_address(event, context)
        mock_post.assert_called_once()
        
        self.assertEqual(200, response['statusCode'])
