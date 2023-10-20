from transformers import MarianTokenizer, MarianMTModel
model_name = "Helsinki-NLP/opus-mt-en-fr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
english_text = "Hello, how are you?"
input_ids = tokenizer.encode(english_text, return_tensors="pt")
translated_ids = model.generate(input_ids, max_length=50, num_beams=5, early_stopping=True)
translated_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)
print("English Text:", english_text)
print("French Translation:", translated_text)
