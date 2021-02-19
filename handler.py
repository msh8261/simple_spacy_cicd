import json
import spacy




def lambda_handler(event, context):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(event['body'])
    for token in doc:
    	results = (token.text, token.pos_, token.dep_)
    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }


event = {"body": 'Tesla is looking at buying U.S. startup for $6 million, is it ok?'}

res = lambda_handler(event, '')

print(res)