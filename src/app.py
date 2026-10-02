# src/app.py
import json
import os
from datetime import datetime

def lambda_handler(event, context):
    """
    Main Lambda handler function.
    Returns a greeting with environment and timestamp.
    """
    environment = os.environ.get('ENVIRONMENT', 'dev')
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'message': 'Hello from DevOps Pro Big Project!',
            'environment': environment,
            'timestamp': datetime.utcnow().isoformat()
        })
    }