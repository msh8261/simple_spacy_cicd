import json
import spacy



nlp = spacy.load("/opt/en_core_web_sm-2.2.5/en_core_web_sm/en_core_web_sm-2.2.5")


def lambda_handler(event, context):
    
    doc = nlp(event['body'])
    for token in doc:
    	results = (token.text, token.pos_, token.dep_)
    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }


