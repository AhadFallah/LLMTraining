from importlib.metadata import version
import tiktoken
tokenizer=tiktoken.get_encoding("gpt2")
words=tokenizer.encode('hello world')
print(words)
print(tokenizer.decode(words))