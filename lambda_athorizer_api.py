def lambda_handler(event, context):
   
   # Log the event
   print("The event data is below:")
   print(event)
   
   # Put default value for authorization
   authorization = 'Deny'
   
   # Validate the token
   if event['authorizationToken'] == "12345":
       authorization = 'Allow'
   else:
       authorization = 'Deny'
       
    # Generate IAM Policy
    
   authorizationpolicy = { "principalId": "authorizerpolicy", 
      "policyDocument": {
      "Version": "2012-10-17",
      "Statement": [
        {
        "Action": "execute-api:Invoke",
        "Effect": authorization,
        "Resource": ["arn:aws:execute-api:ap-southeast-2:411848967072:cqmqyf6iaj/dev/GET/students"]
       }
     ]
    }}
   
      
   return authorizationpolicy