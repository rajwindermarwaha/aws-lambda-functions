import json
import boto3

client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    response = client.get_object(
      Bucket='reads3writedynamodb',
    
      Key='DynamoDB_Samplefile.json'
    
  )
   # convert streaming data to bytes
    json_data = response['Body'].read()
    # print(json_data)
    # print(type(json_data)
    
    # convert bytes to string
    
    data_string = json_data.decode('UTF-8')
    # print(data_string)
    # print(type(data_string)
    
    # convert string to dict.
    
    data_dict= json.loads(data_string)
    print(data_dict)
    print(type(data_dict)
    
    )
    
     # insert data to dynamodb
    table = dynamodb.Table('RetailSales')
    table.put_item(
      Item= data_dict
    )