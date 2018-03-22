import boto3
import json
import datetime

def lambda_handler(event, context):

    # Set service resource
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

    # Instantiate table resource 
    table = dynamodb.Table('ftratings')

    # Set timestamp at execution
    # Get current timestamp in ISO8601 format
    timestamp = datetime.datetime.now().isoformat()
    
    #Define rating variable
    rating = json.loads(event['rating'])
    
    #  Add new item to DynamoDB table
    table.put_item(
        Item={
            'timestamp': timestamp,
            'rating': rating
        }
    )
