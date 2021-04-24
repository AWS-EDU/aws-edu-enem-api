import boto3
import json
import os

def lambda_handler(event, context):
    quicksight = boto3.client('quicksight')
    response = quicksight.get_dashboard_embed_url(
        AwsAccountId=os.environ['ACCOUNTID'],
        DashboardId=os.environ['DASHBOARDID'],
        IdentityType='ANONYMOUS',
        Namespace='default'
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
