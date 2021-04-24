import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = event['queryStringParameters']['bucket']
    key = event['queryStringParameters']['object_key']

    url = s3.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': bucket,
            'Key': key
        },
        ExpiresIn=3600
    )

    return {
        'statusCode': 200,
        'body': json.dumps({
            "presignedUrl": url 
        })
    }