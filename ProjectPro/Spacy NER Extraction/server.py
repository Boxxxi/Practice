'''
Featurization api server handler
'''
import re
import uvicorn
import fastapi

import pandas as pd
import spacy # 3.7.5

nlp = spacy.load('custom_ner_model')


def preprocess_sms1(text):
    # Add a space after 'Rs.' or 'INR' followed by numbers
    pattern = r'(Rs\.|Rs:|INR\.|INR:|Rs|INR|I@NR|:|\(|\))'
    # Substituting by adding a space after the decimal number
    processed_sms = re.sub(pattern, r' \1 ', text)
    return processed_sms

def preprocess_sms2(text):
    # Add a space after 'Rs.' or 'INR' followed by numbers
    pattern = r'(?i)(account|acc\.|ac\.|acct\.|a/c\.|account\.|acc|ac|acct|a/c)(\s*)(no\.:|number\.:|num\.:|no\.|number\.|numbr\.|num\.|no:|number:|num:|No|number|numbr|num)(\s*)([X\d\*]+)(\d{2}-\d{2}-\d{2})'
    # Substituting by adding a space after the decimal number
    processed_sms = re.sub(pattern, r'\1\2\3\4 \5 \6', text)
    return processed_sms

def preprocess_sms3(text):
    # Add a space after 'Rs.' or 'INR' followed by numbers
    pattern = r'(?i)(Rs\.|Rs:|INR\.|INR:|Rs|INR|I@NR)(\s+)([\d\.\,]+)(\d{2}-\d{2}-\d{2})'
    # Substituting by adding a space after the decimal number
    processed_sms = re.sub(pattern, r'\1\2\3 \4', text)
    return processed_sms

def preprocess_sms4(text):
    # Add a space after 'Rs.' or 'INR' followed by numbers
    pattern = r'(?i)(Rs\.|Rs:|INR\.|INR:|Rs|INR|I@NR)(\s+)([\d\.\,]+)(\,)(\d{2}-\d{2}-\d{2,4})'
    # Substituting by adding a space after the decimal number
    processed_sms = re.sub(pattern, r'\1\2\3 \4 \5', text)
    return processed_sms

def preprocess_sms5(text):
    # Add a space after 'Rs.' or 'INR' followed by numbers
    pattern = r'(?i)(Rs\.|Rs:|INR\.|INR:|Rs|INR|I@NR)(\s+)([\d\.\,]+)(\.|\,)([A-z]|-)'
    # Substituting by adding a space after the decimal number
    processed_sms = re.sub(pattern, r'\1\2\3 \4 \5', text)
    return processed_sms

def preprocess_sms6(text):
    # Add a space after 'Rs.' or 'INR' followed by numbers
    pattern = r'(?i)(Rs\.|Rs:|INR\.|INR:|Rs|INR|I@NR)(\s+)([\d\.\,]+)([A-z])'
    # Substituting by adding a space after the decimal number
    processed_sms = re.sub(pattern, r'\1\2\3 \4', text)
    return processed_sms

def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities


############
# api root #
############
app = fastapi.FastAPI()

@app.get('/health', status_code=200)
def health_check():
    '''
    health check handler.
    '''
    return fastapi.responses.JSONResponse(
        content={'message': 'Server is Healthy'},
        status_code=200
    )


##########
# api v1 #
##########
v1 = fastapi.FastAPI(json_encoders={float: str})


@v1.get('/execute')
def execute_model(input_payload: dict):
    '''
    health check handler.
    '''
    df = pd.DataFrame(input_payload)

    df['sms_list'] = df['sms_list'].apply(lambda x : preprocess_sms1(x))
    df['sms_list'] = df['sms_list'].apply(lambda x : preprocess_sms2(x))
    df['sms_list'] = df['sms_list'].apply(lambda x : preprocess_sms3(x))
    df['sms_list'] = df['sms_list'].apply(lambda x : preprocess_sms4(x))
    df['sms_list'] = df['sms_list'].apply(lambda x : preprocess_sms5(x))
    df['sms_list'] = df['sms_list'].apply(lambda x : preprocess_sms6(x))
    df['sms_list'] = df['sms_list'].apply(lambda x: ' '.join(x.split()))

    df['predicted_entities'] = df['sms_list'].apply(extract_entities)

    return fastapi.responses.JSONResponse(
        content={'data': df[['hash', 'predicted_entities']].to_dict()},
        status_code=200
    )

# mount v1 api paths
app.mount('/api/v1', v1)

# for development setup
if __name__ == "__main__":
    uvicorn.run(
        'server:app', host='0.0.0.0', port=8080, reload=False, workers=4
    )
