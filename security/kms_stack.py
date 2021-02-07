from aws_cdk import core
from aws_cdk import aws_kms as kms
from aws_cdk import aws_iam as iam


class KmsStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self._dynamodb_key = kms.Key(self,
                                     "dynamodb_key",
                                     description="KMS CMK for Person data dynamo db table",
                                     enable_key_rotation=True,
                                     enabled=True)

        # TODO: Define appropriate policy document for KMK-CMK
        #dynamodb_key_policy_doc = iam.PolicyDocument()
        #dynamodb_key_statement = iam.PolicyStatement()
        #dynamodb_key_statement.add_actions(actions=['kms:encrypt', 'kms:decrypt'])


    @property
    def dynamodb_key(self):
        return self._dynamodb_key
