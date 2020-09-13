import boto3
from boto3.dynamodb.conditions import Key
dynamoDB = boto3.resource('dynamodb')
table = dynamoDB.Table('users')

def lambda_handler(event,context):
    blood = event['blood']
    #resp = table.get_item(Key={"blood":blood})
    response = table.scan(FilterExpression=Key('blood').eq(blood))
    return response['Items']
