import re
import time

import pandas as pd
import spacy # 3.7.5

df1 = pd.read_json('ffe8e4699721afdedf4d05334450a68c_enriched_unextracted.json')
df2 = pd.read_json('ffe9c5058fb8ae19e1abf4592fdb1790_enriched_unextracted.json')
df3 = pd.read_json('fff40ddd1e381f775bd51bbffbcdec5a_enriched_unextracted.json')

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

test_data = df1.copy()

print(test_data)

test_data['sms_list'] = test_data['sms_list'].apply(lambda x : preprocess_sms1(x))
test_data['sms_list'] = test_data['sms_list'].apply(lambda x : preprocess_sms2(x))
test_data['sms_list'] = test_data['sms_list'].apply(lambda x : preprocess_sms3(x))
test_data['sms_list'] = test_data['sms_list'].apply(lambda x : preprocess_sms4(x))
test_data['sms_list'] = test_data['sms_list'].apply(lambda x : preprocess_sms5(x))
test_data['sms_list'] = test_data['sms_list'].apply(lambda x : preprocess_sms6(x))
test_data['sms_list'] = test_data['sms_list'].apply(lambda x: ' '.join(x.split()))


def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities


start_time = time.time()
test_data['predicted_entities'] = test_data['sms_list'].apply(extract_entities)
end_time = time.time()
latency = end_time - start_time
print(f"latency : {latency}")

print(test_data)
