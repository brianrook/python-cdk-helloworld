import logging
import logging.config

from pydantic import BaseModel

logger = logging.getLogger(__name__)


class MessageResponse(BaseModel):
    message: str


class HelloWorld:

    @staticmethod
    def getMessage():
        logger.info("request to helloworld.getmessage")
        msgResponse = MessageResponse(message="Hello World! with version")
        logger.debug("returning msg: %s", msgResponse.json())
        return msgResponse
