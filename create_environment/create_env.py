import boto3
client = boto3.client('cloud9')

response = client.create_environment_ec2(
        name='devMachina',
        description='0 env cloud9',
        clientRequestToken='string',
        instanceType='string',
        subnetId='string',
        automaticStopTimeMinutes=30,
        ownerArn='string'
        )
print(response)
