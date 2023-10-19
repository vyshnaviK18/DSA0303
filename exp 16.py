import spacy

nlp = spacy.load("en_core_web_sm")
text = "Apple Inc. is an American multinational technology company headquartered in Cupertino, California. It was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976."
doc = nlp(text)
for entity in doc.ents:
    print(f"Entity: {entity.text}, Label: {entity.label_}")
