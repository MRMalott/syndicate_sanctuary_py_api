import logging
import json
from response import error

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def run_safe(func, event, context):
    try:
        resp = func(event, context)
        logger.info(f'Returning response: {json.dumps(resp)}')
        return resp
    except Exception as ex:
        logger.error(f'Exception occurred: {str(ex)}')
        return error(ex)
