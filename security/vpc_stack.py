from aws_cdk import core
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_iam as iam
from aws_cdk import aws_kms as kms
from aws_cdk import aws_dynamodb as dynamodb


class VpcStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, kms_key: kms.IKey,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(
            self, "cdk-test",
            cidr="10.240.0.0/20",
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(name="public", cidr_mask=24, subnet_type=ec2.SubnetType.PUBLIC),
                ec2.SubnetConfiguration(name="private", cidr_mask=24, subnet_type=ec2.SubnetType.ISOLATED)
            ]
        )

        dynamodb_endpoint = vpc.add_gateway_endpoint(
            "dynamodb-endpoint",
            service=ec2.GatewayVpcEndpointAwsService("dynamodb"),
            subnets=vpc.select_subnets(subnet_type=ec2.SubnetType.ISOLATED).subnets
        )

        person_data_table = dynamodb.Table(self, "person_data_table",
                                                 partition_key=dynamodb.Attribute(name="guid",
                                                                                  type=dynamodb.AttributeType.STRING),
                                                 encryption=dynamodb.TableEncryption.CUSTOMER_MANAGED,
                                                 encryption_key=kms_key)
        
        dynamodb_access_policy = iam.PolicyStatement(actions=["dynamodb:PutItem",
                                                              "dynamodb:GetItem",
                                                              "dynamodb:Query",
                                                              "dynamodb:Scan",
                                                              "dynamodb:Decribe*",
                                                              "dynamodb:UpdateItem",
                                                              "dynamodb:DeleteItem"],
                                                     resources=[f'person_data_table.tableArn'],
                                                     effect=iam.Effect.ALLOW,
                                                     principals=[iam.AccountPrincipal(account_id=core.Aws.ACCOUNT_ID)])

        dynamodb_endpoint.add_to_policy(dynamodb_access_policy)


