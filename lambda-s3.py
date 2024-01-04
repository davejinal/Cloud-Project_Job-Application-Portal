import json
import base64
import boto3 # AWS SDK for Python, used to access S3
import random
import string
def lambda_handler(event, context):
 s3 = boto3.client("s3")
 get_file_content = event.get('body')
 decode_content = base64.b64decode(get_file_content)
 filename = event['queryStringParameters']['filename']  # Get the filename from queryStringParameters
 s3_upload = s3.put_object(Bucket="my-test-bucket-cloud-lamda2", Key=filename, Body=decode_content)  # Append filename to the Key
 return {
    'statusCode': 200,
    'headers': {
     'Access-Control-Allow-Origin': '*',
     'Access-Control-Allow-Methods': 'POST, PUT, PATCH, GET, DELETE, OPTIONS',
     'Access-Control-Allow-Headers': '*'
    },
    'body': json.dumps(event)
  }
