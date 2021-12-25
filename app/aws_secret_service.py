import json


class AwsSecretService:

    def __init__(self, boto3, region):
        self._boto3 = boto3
        self._region_name = region

    def get_secret(self, secret_name):
        # Create a Secrets Manager client
        session = self._boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=self._region_name
        )

        secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )

        return json.loads(secret_value_response['SecretString'])