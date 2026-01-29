import re
# //first step is to spreate the words
# words="hello world this is sample text?"
# result=re.split(r'([,.:;?_!"()\']|--|\s)',words)
# print(result)

# get the word from file
with open('the_verdict.txt','r',encoding='utf-8') as f:
    text= f.read()
# tokenrize or split base on regex pattern
preproccessed=re.split(r'([,.:;?_!"()\']|--|\s)',text)
# delete white space
result = [item for item in preproccessed if item.strip()]
# make the tokens unique and sort them
all_words=sorted(set(result))
