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
#give id
vocap={token:integer for integer,token in enumerate(all_words)}

class SimpleTokenizerV1:
    def __init__(self,vocap):
        #same in put make the string to token ids
        self.str_to_int=vocap
        #this will make int first and string as value
        self.int_to_str={i:s for s,i in vocap.items()}
    def encode(self,text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\\s)', text)
        result=[item for item in preproccessed if item.strip()]
        ids=[self.str_to_int for s in result]
        return ids
    def decode(self,ids):
        text=" ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\\s+([,.?!"()\\])', r'\\1', text) 
        return text
tokenrizer=SimpleTokenizerV1(vocap)
print(tokenrizer.decode([14]))