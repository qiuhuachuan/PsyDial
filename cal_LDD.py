import os

import jieba
import numpy as np
import ujson

existing_files = os.listdir('./data')
print('file counter', len(existing_files))
total_files = len(existing_files)

turns = []
client = []
counselor = []
client_jieba_tokens = []
counselor_jieba_tokens = []
for each_file in existing_files:
    with open(f'./data/{each_file}', 'r', encoding='utf-8') as f:
        messages = ujson.load(f)
    
    turns.append(len(messages)/2)
    for el in messages:
        role = el['role'] 
        content = el['content']
        if role == 'client':
            client.append(len(content))
            client_jieba_tokens += jieba.lcut(content)
        elif role == 'counselor':
            counselor.append(len(content))
            counselor_jieba_tokens += jieba.lcut(content)

print(np.mean(turns))
print(np.mean(client))
print(np.mean(counselor))

print('total jieba(client)', len(client_jieba_tokens))
print('unique jieba(client)', len(set(client_jieba_tokens)))

# PUW: Proportion of Unique Words
PUW_client = round(len(set(client_jieba_tokens))/len(client_jieba_tokens)*100, 2)
print('PUW (client):', PUW_client)
# UWPD: Unique Words Per Dialogue
UWPD_client = round(len(set(client_jieba_tokens))/total_files, 2)
print('UWPD (client):', UWPD_client)
LDD_client = PUW_client * UWPD_client
print('LDD (client):', LDD_client)

print('total jieba(counselor)', len(counselor_jieba_tokens))
print('unique jieba(counselor)', len(set(counselor_jieba_tokens)))
# PUW: Proportion of Unique Words
PUW_counselor = round(len(set(counselor_jieba_tokens))/len(counselor_jieba_tokens)*100, 2)
print('PUW (counselor):', PUW_counselor)
# UWPD: Unique Words Per Dialogue
UWPD_counselor = round(len(set(counselor_jieba_tokens))/total_files, 2)
print('UWPD (counselor):', UWPD_counselor)
LDD_counselor = PUW_counselor * UWPD_counselor
print('LDD (counselor):', LDD_counselor)