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


