from aws_cdk import core
from aws_cdk import aws_dynamodb as dynamodb
import aws_cdk.aws_kms as kms


class DynamodbStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, kms_key: kms.IKey, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self._person_data_table = dynamodb.Table(self, "person_data_table",
                                                 partition_key=dynamodb.Attribute(name="guid",
                                                                                  type=dynamodb.AttributeType.STRING),
                                                 encryption=dynamodb.TableEncryption.CUSTOMER_MANAGED,
                                                 encryption_key=kms_key)

        @property
        def person_data_table(self):
            return self._person_data_table