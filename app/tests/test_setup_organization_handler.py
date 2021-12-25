import unittest
import unittest.mock
import requests
import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from source_service import SourceService
from setup_organization_handler import create_default_sources  # noqa: E402

@unittest.mock.patch.dict(os.environ, {'AWS_SECRETS_REGION': 'us-east-1', 'SALES_SERVICE_URL': 'http://hax.com', })
class TestApp(unittest.TestCase):
    def setup(mocker):
        mocker.patch('payment_app.secret_service', return_value={'api_secret': 'test_stripe_secret', 'webhook_secret': ''})

    @unittest.mock.patch.object(SourceService, 'create')
    @unittest.mock.patch.object(SourceService, 'update')
    def test__payment_initiate__success(self, mock_update, mock_create):
        mock_update.return_value = {'id': '123'}
        mock_create.return_value = {'id': '123' }

        test_token = 'token'
        test_org = 'org1'

        create_default_sources(test_token, test_org)
        mock_update.assert_called_once()
        mock_create.assert_has_calls([
            unittest.mock.call('org1', 'Unspecified'), unittest.mock.call('org1', 'Website Form'),
            unittest.mock.call('org1', 'Facebook Ad'), unittest.mock.call('org1', 'Google Ad'),
            unittest.mock.call('org1', 'Call In')
        ], any_order=True)
