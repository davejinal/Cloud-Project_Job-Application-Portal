import boto3
import json
from botocore.exceptions import ClientError
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user_data_table')
s3 = boto3.client('s3')
def lambda_handler(event, context):
  try:
   content = json.loads(event.get('body'))
   username = content.get('name') 
   email = content.get('email')
   phone_number=content.get('phone')
   designation = content.get('designation')
   years_of_exp = content.get('yearOfExperience')
   gender = content.get('gender')
   current_location = content.get('currentLocation')
   preferred_location = content.get('preferredLocation')
   table.put_item(Item={
   'ID': email,
   'username': username,
   'PhoneNumber': phone_number,
   'email': email,
   'Designation': designation,
   'YearsOfExp': years_of_exp,
   'Gender': gender,
   'CurrentLocation': current_location,
   'PreferredLocation': preferred_location
    })
   return {          
     'statusCode': 200,
     'headers': {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, PUT, PATCH, GET, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': '*'
      },
      'body': json.dumps({'message': 'Successfully submitted '}),
    }
  except ClientError as e:
   return {
    'statusCode': 500,
    'body': json.dumps({'error': str(e)}),
  }
