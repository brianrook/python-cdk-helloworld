import logging
import logging.config

logging.config.fileConfig('logging.conf')

from helloworld.helloworld import HelloWorld
from datadog_lambda.wrapper import datadog_lambda_wrapper


logger = logging.getLogger(__name__)


@datadog_lambda_wrapper
def handler(event, context):
    logger.info("handler request in")
    return {
        'statusCode': 200,
        'body': HelloWorld.getMessage().json()
    }
