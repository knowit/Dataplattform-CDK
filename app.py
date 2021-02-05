#!/usr/bin/env python3

from aws_cdk import core
from databases.dynamodb_stack import DynamodbStack
from databases.s3_stack import S3Stack
from pipeline.athena_stack import AthenaStack
from pipeline.glue_stack import GlueStack
from security.groups_stack import GroupsStack
from security.kms_stack import KmsStack
from security.policies_stack import PoliciesStack
from security.roles_stack import RolesStack
from security.vpc_stack import VpcStack

app = core.App()
DynamodbStack(app, "dynamo-db-stack")
S3Stack(app, "s3-stack")
AthenaStack(app, "athena-stack")
GlueStack(app, "glue-stack")
GroupsStack(app, "groups-stack")
KmsStack(app, "kms-stack")
PoliciesStack(app, "policies-stack")
RolesStack(app, "roles-stack")
VpcStack(app, "vpc-stack")

app.synth()
