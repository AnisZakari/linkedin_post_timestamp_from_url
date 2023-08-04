#!/usr/bin/env python3
import os

import aws_cdk as cdk
from stack.get_time_stack import LinkedinTime

app = cdk.App()
LinkedinTime(
    app,
    "LinkedinTimeApp",
)

app.synth()
