import boto3
import os
# session = boto3.Session(profile_name='devmachina', region_name='us-east-1')
# Any clients created from this session will use credentials
# from the [dev] section of ~/.aws/credentials.
# print(session)
client = boto3.client('cloud9', region_name='us-east-1', aws_access_key_id=os.environ['ACCESS_KEY'], aws_secret_access_key=os.environ['SECRET_KEY'])

response = client.describe_environments(
        environmentIds=[
            '2f57c4e89940494a85fe2b883ac4776e'
        ]
        )
print(response)

print('***********************************************************************************')
ec2_client = boto3.client('ec2', region_name='us-east-1', aws_access_key_id=os.environ['ACCESS_KEY'], aws_secret_access_key=os.environ['SECRET_KEY'])

ec2_response = ec2_client.describe_instances()

print(ec2_response)
