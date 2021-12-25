import unittest
import unittest.mock
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from user_sender_email_service import UserSenderEmailService  # noqa: E402

@unittest.mock.patch.dict(os.environ, {'AWS_SECRETS_REGION': 'us-east-1', 'STRIPE_API_SECRETS': 'test/stripe', 'STRIPE_PUBLISHABLE_KEY': 'test_pub_key'})
class TestUserSenderEmailService(unittest.TestCase):    
    def test__slugify__ampersand(self):
        service = UserSenderEmailService('stagingsigma.com', 'token')
        self.assertEqual(service.slugified_email_address('heating&cooling'), 'heatingandcooling')
        
    def test__slugify__spaces(self):
        service = UserSenderEmailService('stagingsigma.com', 'token')
        self.assertEqual(service.slugified_email_address('heating and cooling'), 'heatingandcooling')
        
    def test__slugify__capitals(self):
        service = UserSenderEmailService('stagingsigma.com', 'token')
        self.assertEqual(service.slugified_email_address('Heating and Cooling'), 'heatingandcooling')
