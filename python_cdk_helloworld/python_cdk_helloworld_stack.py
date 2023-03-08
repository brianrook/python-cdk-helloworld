from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda
)
from constructs import Construct

class PythonCdkHelloworldStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.build_lambda_func()

    def build_lambda_func(self):
        self.prediction_lambda = _lambda.DockerImageFunction(
            scope=self,
            id="helloWorld-cdk",
            # Function name on AWS
            function_name="helloWorld-cdk",
            # Use aws_cdk.aws_lambda.DockerImageCode.from_image_asset to build
            # a docker image on deployment
            code=_lambda.DockerImageCode.from_ecr(
                # Directory relative to where you execute cdk deploy
                # contains a Dockerfile with build instructions
                repository="python-cdk-helloworld"
            ),
        )