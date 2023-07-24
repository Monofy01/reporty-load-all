import os


class ENVS:
    DYNAMO_TABLE_REPORTS = os.environ.get('DYNAMO_TABLE_REPORTS')
    DYNAMO_TABLE_METADATA = os.environ.get('DYNAMO_TABLE_METADATA')

    def __int__(self):
        pass