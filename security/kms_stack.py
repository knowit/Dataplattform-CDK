from aws_cdk import core
from aws_cdk import aws_kms as kms


class KmsStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self._dynamodb_key = kms.Key(self,
                                     "dynamodb_key",
                                     description="KMS CMK for Person data dynamo db table",
                                     enable_key_rotation=True,
                                     enabled=True)

    @property
    def dynamodb_key(self):
        return self._dynamodb_key
