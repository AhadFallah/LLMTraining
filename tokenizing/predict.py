import re
import tiktoken

with open('the_verdict.txt','r',encoding='utf-8')as f:
    mainText=f.read()

tokenizer=tiktoken.get_encoding('gpt2')
tokens=tokenizer.encode(mainText)
print(len(mainText))
sample=tokens[50:]
size=4


x=sample[:size]
y=sample[1:size+1]
print(f"x:{x}")
print(f"y:{y}")