import boto3
import os

client = boto3.client('cloud9', region_name='us-east-1', aws_access_key_id=os.environ['ACCESS_KEY'], aws_secret_access_key=os.environ['SECRET_KEY'])

response = client.describe_environments()

print(response)

ec2_client = boto3.client('ec2', region_name='us-east-1', aws_access_key_id=os.environ['ACCESS_KEY'], aws_secret_access_key=os.environ['SECRET_KEY'])

ec2_response = ec2_client.describe_instances()

print(ec2_response)
