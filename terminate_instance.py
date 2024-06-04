import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    response = ec2.terminate_instances(
    InstanceIds=[
        'i-02b0e0ebe13de6981',
    ])