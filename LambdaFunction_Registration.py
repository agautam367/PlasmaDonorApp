import boto3
dynamoDB = boto3.resource('dynamodb')
table = dynamoDB.Table('users')
def lambda_handler(event, context):
    # TODO implement
    print(event)
    #email = event['email']
    #data = {"email":email}
    table.put_item(Item=event)
    return {"code":200, "message":"Registration successful"}
