from aws_cdk import core
import aws_cdk.aws_iam as iam


class PoliciesStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
