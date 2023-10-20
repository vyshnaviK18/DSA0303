import openai
api_key = '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'
prompt = "Translate the following English text to French: 'Hello, how are you?'"
response = openai.Completion.create(
    engine="text-davinci-002", 
    prompt=prompt,
    max_tokens=50  
)
generated_text = response.choices[0].text
print("Generated Text:")
print(generated_text)
