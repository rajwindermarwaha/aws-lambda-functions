import boto3

client = boto3.client('s3')

def lambda_handler(event, context):
    
    response = client.delete_bucket(
       
      Bucket = 'cathasabucket009900'
      ) 
        
    print(response)