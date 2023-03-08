import logging

from pydantic import BaseModel

logger = logging.getLogger("helloworld")


class MessageResponse(BaseModel):
    message: str


class HelloWorld:

    @staticmethod
    def getMessage():
        logger.info("request to helloworld.getmessage")
        msgResponse = MessageResponse(message="Hello World!!")
        logger.debug("returning msg: %s", msgResponse.json())
        return msgResponse
