import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
   
    response = client.put_item(
       TableName='RetailSales',
       Item={
        'CustomerId': {
            'S': '001',
           
        },
        'Product': {
            'S': 'Mangoes',
           
        },
        'Quantity': {
            'N': '100',
           
        },
        'Address': {
            'S': 'Melbourne',
           
        },
      },
         
     )
         
    print(response)