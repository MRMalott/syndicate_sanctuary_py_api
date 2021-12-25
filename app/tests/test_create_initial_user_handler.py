import unittest
import unittest.mock
import jwt
import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from create_initial_user_handler import create_initial_user  # noqa: E402
from auth_token_service import AuthTokenService
from aws_secret_service import AwsSecretService

@unittest.mock.patch.dict(os.environ, {'AWS_SECRETS_REGION': 'us-east-1', 'SALES_SERVICE_URL': 'http://hax.com', 'AUTH_SECRET_ID': 'secret'})
class TestApp(unittest.TestCase):
    @unittest.mock.patch('create_initial_user_handler.create_organization')
    @unittest.mock.patch('create_initial_user_handler.create_user')
    @unittest.mock.patch('create_initial_user_handler.reset_password')
    @unittest.mock.patch('create_initial_user_handler.secret_service')
    @unittest.mock.patch('create_initial_user_handler.create_auth_token')
    def test__create_initial_user__with_test(self, mock_auth, mock_secret, mock_reset, mock_create_user, mock_create_org):
        mock_create_org.return_value = {'id': 'o123' }
        mock_create_user.return_value = {'id': 'u123' }
        mock_reset.return_value = 'token123'
        mock_auth.return_value = 'auth'
        test_secrets = {'account_sid': 'sid', 'auth_token': 'token'}
        mock_secret.return_value = unittest.mock.Mock(**{'get_secret.return_value': test_secrets})


        event = {
            'body': json.dumps({
                'first_name': 'f',
                'last_name': 'l',
                'email_address': 'a@mail.com',
                'phone_number_prefix': '1',
                'phone_number': '1231234',
                'password': 'password',
                'do_slingshot': 'true',
                'test': 'true'
            }),
            'headers': {'Authorization': 'bearer jwt'}
        }
        context = ''

        response = create_initial_user(event, context)
        self.assertEqual(200, response['statusCode'])
        self.assertEqual(True, 'token123' in response['body'])
        mock_create_org.assert_called_with('auth', unittest.mock.ANY, 'skipped')
        
    @unittest.mock.patch('create_initial_user_handler.create_organization')
    @unittest.mock.patch('create_initial_user_handler.create_user')
    @unittest.mock.patch('create_initial_user_handler.reset_password')
    @unittest.mock.patch('create_initial_user_handler.secret_service')
    @unittest.mock.patch('create_initial_user_handler.create_auth_token')
    def test__create_initial_user__success(self, mock_auth, mock_secret, mock_reset, mock_create_user, mock_create_org):
        mock_create_org.return_value = {'id': 'o123' }
        mock_create_user.return_value = {'id': 'u123' }
        mock_reset.return_value = 'token123'
        mock_auth.return_value = 'auth'
        test_secrets = {'account_sid': 'sid', 'auth_token': 'token'}
        mock_secret.return_value = unittest.mock.Mock(**{'get_secret.return_value': test_secrets})


        event = {
            'body': json.dumps({
                'first_name': 'f',
                'last_name': 'l',
                'email_address': 'a@mail.com',
                'phone_number_prefix': '1',
                'phone_number': '1231234',
                'password': 'password',
                'do_slingshot': 'true'
            }),
            'headers': {'Authorization': 'bearer jwt'}
        }
        context = ''

        response = create_initial_user(event, context)
        self.assertEqual(200, response['statusCode'])
        self.assertEqual(True, 'token123' in response['body'])
        mock_create_org.assert_called_with('auth', unittest.mock.ANY, 'not_started')