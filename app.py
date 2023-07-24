import json

from src.db.dynamo_client import DynamoClient


def handler(event, context):
    print(f'REQUEST :: {event}')
    data_response = None
    if json.loads(event['body'])['metadata']:
        data_response = DynamoClient().get_all_metadata()

    else:
        data_response = DynamoClient().get_all_reports()
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(data_response)
    }
