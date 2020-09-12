import boto3
dynamoDB = boto3.resource('dynamodb')
table = dynamoDB.Table('users')

def lambda_handler(event,context):
    email=event['email']
    print(email)
    resp = table.get_item(Key={"email":email})
    return resp['Item']