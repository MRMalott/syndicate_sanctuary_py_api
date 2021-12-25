import unittest
import unittest.mock
import requests
import sys
import os
import stripe
import json
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from payment_app import response_object, secret_service, payment_key_hanlder, payment_initiate_handler, payment_webhook_handler  # noqa: E402

@unittest.mock.patch.dict(os.environ, {'AWS_SECRETS_REGION': 'us-east-1', 'STRIPE_API_SECRETS': 'test/stripe', 'STRIPE_PUBLISHABLE_KEY': 'test_pub_key'})
class TestApp(unittest.TestCase):
    def setup(mocker):
        mocker.patch('payment_app.secret_service', return_value={'api_secret': 'test_stripe_secret', 'webhook_secret': ''})
    
    def test__payment_key__success(self):
        resp = payment_key_hanlder(None, None)
        self.assertEqual(resp['body'], '{"key": "test_pub_key"}')

    def test_response_object(self):
        status = 200
        methods = 'GET,OPTIONS'
        raw_body = '{}'
        
        resp = response_object(status, methods, raw_body)
        self.assertEqual(resp['headers'].get('Access-Control-Allow-Methods'), 'GET,OPTIONS')

    @unittest.mock.patch('stripe.Customer.create')
    @unittest.mock.patch('stripe.SetupIntent.create')
    @unittest.mock.patch('payment_app.secret_service')
    def test__payment_initiate__success(self, mock_secret, mock_setup_intent, mock_customer_create):
        mock_customer_create.return_value = {'id': 'test_id'}
        mock_setup_intent.return_value = unittest.mock.Mock(**{'client_secret':'test_secret'})
        mock_secret.return_value = unittest.mock.Mock(**{'get_secret.return_value': {'api_secret': 'test_stripe_secret', 'webhook_secret': ''}})

        test_event = {
            'body': json.dumps({'email': 'test@email.com', 'payment_plan': 'STANDARD'}),
            'headers': {'Authorization': 'jwt'}}

        resp = payment_initiate_handler(test_event, None)
        self.assertEqual(resp['body'], '{"client_secret": "test_secret"}')
