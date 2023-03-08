import logging

from helloworld.helloworld import HelloWorld

logger = logging.getLogger("main")


def handler(event, context):
    logger.info("handler request in")
    return {
        'statusCode': 200,
        'body': HelloWorld.getMessage().json()
    }
