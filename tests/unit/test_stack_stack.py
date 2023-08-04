import aws_cdk as core
import aws_cdk.assertions as assertions

from stack.stack_stack import StackStack

# example tests. To run these tests, uncomment this file along with the example
# resource in stack/stack_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StackStack(app, "stack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
