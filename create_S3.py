import boto3

client = boto3.client('s3')


def lambda_handler(event, context):
    
    response = client.create_bucket(
       
      Bucket = 'cathasabucket009900',
      CreateBucketConfiguration={
        'LocationConstraint': 'ap-southeast-2'}
        )
        
    print(response)