import json
import spacy

# nltk.data.path.append("/tmp") 

# nltk.download('tagsets', download_dir="/tmp")

nlp = spacy.load("/opt/en_core_web_sm-1.2.0/en_core_web_sm")


def lambda_handler(event, context):
    
    doc = nlp(event['body'])
    for token in doc:
    	results = (token.text, token.pos_, token.dep_)
    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }


