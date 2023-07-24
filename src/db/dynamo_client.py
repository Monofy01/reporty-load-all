import logging
import boto3

from src.config.enviroments import ENVS


class DynamoClient:
    def __init__(self):
        pass

    def get_all_metadata(self):
        dynamodb = boto3.client('dynamodb')

        try:
            response = dynamodb.scan(TableName=ENVS.DYNAMO_TABLE_REPORTS)
            items = response['Items']

            while 'LastEvaluatedKey' in response:
                response = dynamodb.scan(TableName=ENVS.DYNAMO_TABLE_REPORTS,
                                         ExclusiveStartKey=response['LastEvaluatedKey'])
                items.extend(response['Items'])

            # Transforming the DynamoDB format to a more readable Python dictionary format
            metadata_list = []
            for item in items:
                metadata_dict = {}
                if 'file_xlsx' in item:
                    for key, value in item.items():
                        metadata_dict[key] = list(value.values())[0]
                    metadata_list.append(metadata_dict)
            return metadata_list
        except Exception as e:
            logging.error('ERROR:: An error occurred while retrieving metadata from the table')
            return []

