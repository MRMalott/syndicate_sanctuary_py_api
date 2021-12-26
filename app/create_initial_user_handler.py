import json
import os
import boto3
import botocore
import requests
import uuid
import logging

from aws_secret_service import AwsSecretService
from auth_token_service import AuthTokenService
from cognito_service import CognitoService
from response import okay
from run_safe import run_safe

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def create_initial_user(event, context):
    return run_safe(do_create_initial_user, event, context)

def do_create_initial_user(event, context):
    body = json.loads(event['body'])

    # Get lead properties
    # first_name = body['first_name']
    # last_name = body['last_name']
    # email_address = body['email_address']
    # phone_number_prefix = body['phone_number_prefix']
    # phone_number = body['phone_number']
    # phone_number_full = f'{phone_number_prefix}{phone_number}'
    # password = body['password']
    # do_slingshot = body['do_slingshot']
    # test = body.get('test')
    # a2p_status = 'skipped' if test == 'true' else 'not_started'

    # # Log request
    # request_info = {
    #     'first_name': first_name,
    #     'last_name': last_name,
    #     'email_address': email_address,
    #     'phone_number': phone_number_full,
    #     'do_slingshot': do_slingshot,
    #     'test': test
    # }
    # logger.info(f'Create user request: {json.dumps(request_info)}')

    # # Get auth token
    # auth_secret = secret_service().get_secret(os.environ['AUTH_SECRET_ID'])
    # auth_token = create_auth_token(auth_secret)

    # # Create organization (with random name, will rename in next workflow step)
    # organization = create_organization(
    #     auth_token,
    #     str(uuid.uuid4()),
    #     a2p_status
    # )
    # organization_id = organization['id']
    # logger.info(f'Created organization {organization_id} for user {email_address}')

    # # Create user
    # user = create_user(
    #     auth_token=auth_token,
    #     first_name=first_name,
    #     last_name=last_name,
    #     email_address=email_address,
    #     phone_number=phone_number_full,
    #     organization_id=organization_id
    # )
    # user_id = user['id']
    # logger.info(f'Created user {user_id}')

    # # Set user password
    # access_token = reset_password(auth_secret, email_address, password)

    # Return access token to frontend
    return okay({'access_token': 'access_token'})

def secret_service():
    return AwsSecretService(
        boto3,
        os.environ['AWS_SECRETS_REGION']
    )


def create_auth_token(auth_secret):
    return AuthTokenService(
        requests,
        os.environ['AUTH_SERVICE_URL']
    ).get_token({
        'secret': auth_secret,
        'scopes': [
            f"{os.environ['MESSAGING_SERVICE_URL']}/teams"
        ]
    })
