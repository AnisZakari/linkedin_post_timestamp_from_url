from aws_cdk import Stack
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class LinkedinTime(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define the Lambda function
        lambda_ = _lambda.DockerImageFunction(
            self,
            "LinkedinTimeLambda",
            function_name="linkedin_time_lambda",
            code=_lambda.DockerImageCode.from_image_asset("stack/lambda_"),
            architecture=_lambda.Architecture.X86_64,
        )

        # Define the REST API Gateway with Lambda proxy integration
        api = apigw.LambdaRestApi(self, "linkedin_get_time", handler=lambda_, proxy=True)

        # Define a resource for the API
        resource = api.root.add_resource("resource")

        # Add a POST method to the resource
        resource.add_method("POST", apigw.LambdaIntegration(lambda_))

        # Define an API key
        api_key = api.add_api_key("ApiKey")

        # Define a usage plan
        # Define a usage plan
        plan = api.add_usage_plan(
            "UsagePlanLinkedinAPI",
            name="UsagePlanLinkedinAPI",
            throttle=apigw.ThrottleSettings(burst_limit=100, rate_limit=10),
        )

        # Associate the usage plan with a deployment stage
        plan.add_api_stage(stage=api.deployment_stage)
