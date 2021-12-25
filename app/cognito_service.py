import boto3
import os
import hmac, hashlib, base64


class CognitoService:

    def __init__(self):
        self._client = boto3.client('cognito-idp')
        self._user_pool_id = os.environ['COGNITO_USER_POOL_ID']

    def create(self, username):
        response = self._client.admin_create_user(
            UserPoolId=self._user_pool_id,
            Username=username,
            TemporaryPassword='Password01!',
        )
        return response['User']['Attributes'][0]['Value']

    def login(self, client_id, client_secret, username, password):
        self._client.admin_set_user_password(
            UserPoolId=self._user_pool_id,
            Username=username,
            Password=password,
            Permanent=True,
        )

        message = bytes(username + client_id, 'utf-8')
        key = bytes(client_secret, 'utf-8')
        secret_hash = base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()

        response = self._client.admin_initiate_auth(
            UserPoolId=self._user_pool_id,
            ClientId=client_id,
            AuthFlow='ADMIN_NO_SRP_AUTH',
            AuthParameters={
                "USERNAME": username,
                "PASSWORD": password,
                "SECRET_HASH": secret_hash
            }
        )

        return response['AuthenticationResult']['IdToken']
