import boto3
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
        'EmbedUrl': response['EmbedUrl']
    }
