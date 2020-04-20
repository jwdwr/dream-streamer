import boto3

def lambda_handler(event, context):
    db = boto3.resource('dynamodb')
    table = db.Table('dreams')
    records = event['Records']
    for record in records:
        key = record['s3']['object']['key']
        [_, user_id, date, filename] = key.split('/')
        [dream_id, _] = filename.split('.')
        table.put_item(Item={'user_id': user_id, 'id': dream_id, 'date': date})
