#!/usr/bin/env python3

from aws_cdk import core
from storage.dynamodb_stack import DynamodbStack
from security.kms_stack import KmsStack

app = core.App()
kmsStack = KmsStack(app, "kms-stack")
DynamodbStack(app, "dynamo-db-stack", kms_key=kmsStack.dynamodb_key)

app.synth()
