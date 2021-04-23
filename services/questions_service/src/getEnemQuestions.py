import boto3
import os

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb')

    response = dynamodb.execute_statement(
            Statement = 'SELECT object_key, bucket_name, exam_area, page_number, question_num FROM exam_question_files;'
        )

    return {
        'statusCode': 200,
        'items': response['Items'],
        'count': len(response['Items']),
    }