import boto3

client = boto3.client('s3')

def lambda_handler(event, context):
    
  response = client.list_buckets()
  
  print(response['Buckets'])


