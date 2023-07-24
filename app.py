import json

from src.db.dynamo_client import DynamoClient


def handler(event, context):
    print(f'REQUEST :: {event}')
    metadata_all = DynamoClient().get_all_metadata()
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(metadata_all)
    }
