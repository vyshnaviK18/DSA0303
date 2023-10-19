import nltk
import re

nltk.download("punkt")
dialog_act_patterns = [
    (r"\b(?:hi|hello|hey|howdy)\b", "Greeting"),
    (r"\b(?:bye|goodbye|see you|farewell)\b", "Farewell"),
    (r"\b(?:what|who|where|when|why|how|is|are|am|do|does|did)\s.*\?\s*$", "Question"),
    (r".*\?\s*$", "Yes-No Question"),
    (r".*\.\s*$", "Statement"),
]

def recognize_dialog_acts(text):
    for pattern, act in dialog_act_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return act
    return "Other"

conversation = [
    "Hello, how are you?",
    "I'm good. How about you?",
    "I'm doing well, thanks.",
    "What time is it?",
    "Can you pass the salt, please?",
    "Sure, here you go.",
    "Goodbye!",
]

for utterance in conversation:
    dialog_act = recognize_dialog_acts(utterance)
    print(f"Utterance: '{utterance}'")
    print(f"Dialog Act: {dialog_act}")
    print()
