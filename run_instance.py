import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instances = ec2.run_instances(
    ImageId='ami-0ec0514235185af79',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    SubnetId='subnet-058b18a40195f1d2d'
    )

       
       
    print(instances['Instances'][0]['InstanceId'])
  

