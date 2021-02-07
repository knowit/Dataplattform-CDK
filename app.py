#!/usr/bin/env python3

from aws_cdk import core
from security.kms_stack import KmsStack
from security.vpc_stack import VpcStack

app = core.App()
kmsStack = KmsStack(app, "kms-stack")
VpcStack = VpcStack(app, "vpc-stack", kms_key=kmsStack.dynamodb_key)


app.synth()
