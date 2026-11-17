
def recognize_dialog_act(sentence):

    sentence = sentence.lower().strip()

    if sentence.endswith("?"):
        return "Question"

    elif sentence.startswith(("hi", "hello", "hey")):
        return "Greeting"

    elif any(word in sentence for word in ["thank you", "thanks"]):
        return "Thanking"

    elif any(word in sentence for word in ["please", "could you", "can you"]):
        return "Request"

    elif sentence.startswith(("bye", "goodbye")):
        return "Farewell"

    else:
        return "Statement"


dialog = [
    "Hello!",
    "How are you?",
    "Please help me.",
    "Thank you!",
    "Goodbye!"
]

print("Dialog Act Recognition:\n")

for sentence in dialog:
    print(sentence, "-", recognize_dialog_act(sentence))
