import boto3
import datetime


# Set service resource
dynamodb = boto3.resource('dynamodb')

# Instantiate table resource 
# N.B. this is lazy-loaded; no requests are made or 
# values loaded until the table resource is accessed
table = dynamodb.Table('ftratings')

# Get current timestamp in ISO8601 format
timestamp = datetime.datetime.now().isoformat()

# Instantiate a rating value (simulating user data)
rating = 2

#  Add new item to DynamoDB table
table.put_item(
	Item={
		'timestamp': (timestamp),
		'rating': (rating)
	}
)

# Confirm access to correct table and assigned values
print "Table Name and ARN: " + (table.table_name) + " | " + (table.table_arn)
print "Timestamp: " + (timestamp)
print "Simulated rating:",(rating)
