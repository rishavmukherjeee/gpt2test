from transformers import pipeline, set_seed
import os
print("LOADING...")
generator = pipeline('text-generation', model='gpt2-medium')
set_seed(41)
os.system('cls')
val=input("Enter the Starting of the sentence:")
x=generator(val, max_length=100, num_return_sequences=5,truncation=True)
with open('save.txt','w') as s:
    s.write(x[0]['generated_text'])
print(x[0]['generated_text'])

lang='en'