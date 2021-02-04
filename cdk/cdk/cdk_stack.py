from aws_cdk import (
    core,
    aws_ec2 as ec2
)


class CdkStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(
            self, "cdk-test",
            cidr="10.240.0.0/20",
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(name="public", cidr_mask=24, subnet_type=ec2.SubnetType.PUBLIC),
                #ec2.SubnetConfiguration(name="private", cidr_mask=24, subnet_type=ec2.SubnetType.PRIVATE)
                ec2.SubnetConfiguration(name="private", cidr_mask=24, subnet_type=ec2.SubnetType.ISOLATED)
            ] 
        )

        dynamodb_endpoint = vpc.add_gateway_endpoint(
            "dynamodb-endpoint",
            service=ec2.GatewayVpcEndpointAwsService("dynamodb"),
            subnets = vpc.select_subnets(subnet_type=ec2.SubnetType.ISOLATED).subnets
        )