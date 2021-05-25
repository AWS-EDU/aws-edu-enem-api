import boto3
import json
import os

def lambda_handler(event, context):
    quicksight = boto3.client('quicksight')
    dashboard_url = event['queryStringParameters']['dashboard_url']
    
    response = quicksight.get_dashboard_embed_url(
        AwsAccountId=os.environ['ACCOUNTID'],
        DashboardId=dashboard_url,
        IdentityType='ANONYMOUS',
        Namespace='default',
        SessionLifetimeInMinutes = 600
    )
    
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": "*"
        },
        'body': json.dumps({
            'EmbedUrl': response['EmbedUrl'] 
        })
    }
