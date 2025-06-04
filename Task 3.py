import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Predefined intents
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
    "farewell": ["Goodbye!", "See you later!", "Take care!"],
    "name_query": ["I'm your chatbot assistant."],
    "how_are_you": ["I'm doing well, thank you!", "I am just code, but I'm running smoothly!"],
    "default": ["I'm not sure how to respond to that. Can you ask differently?"]
}

def classify_intent(doc):
    text = doc.text.lower()

    if any(token.lemma_ in ['hello', 'hi', 'hey'] for token in doc):
        return "greeting"
    elif any(token.lemma_ in ['bye', 'goodbye', 'farewell'] for token in doc):
        return "farewell"
    elif "your name" in text or "who are you" in text:
        return "name_query"
    elif "how are you" in text:
        return "how_are_you"
    else:
        return "default"

def chatbot_response(user_input):
    doc = nlp(user_input)
    intent = classify_intent(doc)
    return responses[intent][0]

# Chat loop
print("ChatBot 🤖: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'exit', 'quit']:
        print("ChatBot 🤖: Goodbye! 👋")
        break

    response = chatbot_response(user_input)
    print("ChatBot 🤖:", response)
