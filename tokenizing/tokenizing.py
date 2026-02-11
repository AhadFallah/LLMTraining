import re
# //first step is to spreate the words
# words="hello world this is sample text?"
# result=re.split(r'([,.:;?_!"()\']|--|\s)',words)
# print(result)

# get the word from file
with open('the_verdict.txt','r',encoding='utf-8') as f:
    mainText= f.read()
# tokenrize or split base on regex pattern
preproccessed=re.split(r'([,.:;?_!"()\']|--|\s)',mainText)
# delete white space
result = [item for item in preproccessed if item.strip()]
# make the tokens unique and sort them
all_words=sorted(set(result))
all_words.extend(["<|endoftext|>","<|unk|>"])
#give id
vocap={token:integer for integer,token in enumerate(all_words)}

class SimpleTokenizerV1:
    def __init__(self,vocap):
        #same in put make the string to token ids
        self.str_to_int=vocap
        #this will make int first and string as value
        self.int_to_str={i:s for s,i in vocap.items()}
    def encode(self,text):
        preprocessed1 = re.split(r'([,.?_!"()\']|--|\\s)', text)
        result=[item for item in preprocessed1 if item.strip()]
        #this line is same as abouve but in this condition that 
        #if i wrtie a wrod that unkown to text i give the llm 
        #this will write <|unk|> as token while  encoding
        result=[item if item in self.str_to_int else "<|unk|>" for item in preprocessed1]
        ids=[]
        for s in result:
           ids.append(self.str_to_int.get(s)) 
        return ids
    def decode(self,ids):
        text=" ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\\s+([,.?!"()\\])', r'\\1', text) 
        return text
tokenrizer=SimpleTokenizerV1(vocap)


#example 1
#hello don't exist in text 
text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2))
print(tokenrizer.encode(text))