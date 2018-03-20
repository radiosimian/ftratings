import boto3

# Initialise service resource
dynamodb = boto3.resource('dynamodb')

# Create DynamoDB table
table = dynamodb.create_table(
	TableName='ftratings',
	KeySchema=[
		{
			'AttributeName': 'timestamp',
			'KeyType': 'HASH'
		},
		{
			'AttributeName': 'rating',
			'KeyType': 'RANGE'
		}
	],
	AttributeDefinitions=[
		{
			'AttributeName': 'timestamp',
			'AttributeType': 'S'
		},
		{
			'AttributeName': 'rating',
			'AttributeType': 'N'
		}
	],
	ProvisionedThroughput={
		'ReadCapacityUnits': '1',
		'WriteCapacityUnits': '1'
	}
)

# Wait for tabkle to be created
table.meta.client.get_waiter('table_exists').wait(TableName='ftratings')

# Check that table is created by querying its properties
print(table.attribute_definitions)
print(table.key_schema)
print(table.item_count)