import boto3

def upload_model(model_path='', s3_bucket='', key_prefix='', aws_profile='default'):
    s3 = boto3.session.Session(profile_name=aws_profile)
    client = s3.client('s3')
    client.upload_file(model_path, s3_bucket, key_prefix)


s3_bucket = 'my-spacy-layer'
model_path = './layers/spacy_lambda.zip'
key_prefix = 'spacy_lambda.zip'
upload_model(model_path, s3_bucket, key_prefix)