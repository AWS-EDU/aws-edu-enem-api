import boto3
import json
import os

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb')
    table = os.environ['TABLE']

    response = dynamodb.execute_statement(
            Statement = f'SELECT object_key, bucket_name, exam_area, page_number, question_num FROM {table};'
        )

    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": "*"
        },
        'body': json.dumps({
            'items': response['Items'],
            'count': len(response['Items']) 
        })
    }