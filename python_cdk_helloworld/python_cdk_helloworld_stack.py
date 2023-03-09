from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway, CfnParameter,
)
import os
from aws_cdk.aws_ecr import Repository
from constructs import Construct


class PythonCdkHelloworldStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.build_lambda_func()

    def build_lambda_func(self):
        image_tag = os.getenv("IMAGE_TAG", "latest")zz
        self.ecr_image = _lambda.DockerImageCode.from_ecr(
            repository=Repository.from_repository_name(self, "helloWorld-cdk-repository", "python-cdk-helloworld"),
            tag_or_digest=image_tag
        )
        self.prediction_lambda = _lambda.DockerImageFunction(
            scope=self,
            id="helloWorld-cdk",
            # Function name on AWS
            function_name="helloWorld-cdk",
            # Use aws_cdk.aws_lambda.DockerImageCode.from_image_asset to build
            # a docker image on deployment
            code=self.ecr_image,
        )

        api = apigateway.RestApi(self, "helloworld-cdk-api",
                                 rest_api_name="Hello World CDK Service",
                                 description="This service fronts helloworld with CDK.")

        get_helloworld_integration = apigateway.LambdaIntegration(
            self.prediction_lambda,
            request_templates={"application/json": '{ "statusCode": "200" }'})

        api.root.add_method("GET", get_helloworld_integration)
