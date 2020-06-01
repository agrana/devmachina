import boto3
import os
# session = boto3.Session(profile_name='devmachina', region_name='us-east-1')
# Any clients created from this session will use credentials
# from the [dev] section of ~/.aws/credentials.
# print(session)

client = boto3.client('cloud9', region_name='us-east-1',
                       aws_access_key_id=os.environ['ACCESS_KEY'], 
                      aws_secret_access_key=os.environ['SECRET_KEY']
                      )

response = client.create_environment_ec2(
        name='devMachina',
        description='0 env cloud9',
        clientRequestToken='alfonsoenv1',
        instanceType='t3.micro',
        automaticStopTimeMinutes=20,
        ownerArn='arn:aws:iam::726747867029:user/alfonso'
        )
print(response)
