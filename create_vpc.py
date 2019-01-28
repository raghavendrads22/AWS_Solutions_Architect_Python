import boto3
import sys

def create_VPC():

    ec2 = boto3.resource('ec2')
    vpc = ec2.create_vpc(
                         CidrBlock='10.100.0.0/16',
                         AmazonProvidedIpv6CidrBlock=False,
                         InstanceTenancy='default'
                        )
    return vpc

print(create_VPC())