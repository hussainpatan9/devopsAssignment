import boto3
import json

ec2 = boto3.client('ec2')
print("Hello World")
def lambda_handler(event, context):
    response = ec2.describe_availability_zones()
    return {"statusCode": 200, "body": json.dumps(response)}
