import boto3
import os
import uuid

env_id = uuid.uuid4()
print(str(env_id)[:7])

try:
    os.environ['ACCESS_KEY']
    os.environ['SECRET_KEY']
    os.environ['OWNER_ARN']
    
except KeyError as e:
    print('Environment variable ' + e.args[0] + ' not defined')
    
client = boto3.client('cloud9', region_name='us-east-1',
                      aws_access_key_id=os.environ['ACCESS_KEY'], 
                      aws_secret_access_key=os.environ['SECRET_KEY']
                      )

response = client.create_environment_ec2(
        name=str(env_id)[:7],
        description='0 env cloud9',
        clientRequestToken=str(env_id)[:7],
        instanceType='t3.micro',
        automaticStopTimeMinutes=20,
        ownerArn= os.environ('OWNER_ARN')
        )

print(response)
