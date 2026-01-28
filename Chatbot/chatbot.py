def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if user_input in ["hello", "hi", "hey", "hai"]:
        return "Hello! Nice to meet you 😊"

    elif user_input == "how are you":
        return "I'm doing well, thank you!"

    elif user_input in ["i am fine", "i'm fine", "fine", "good"]:
        return "That's great to hear 👍"

    elif user_input in ["not good", "bad"]:
        return "Oh no! I hope things get better soon."

    # Time-based greetings
    elif user_input == "good morning":
        return "Good morning! Have a wonderful day 🌞"

    elif user_input == "good afternoon":
        return "Good afternoon!"

    elif user_input == "good evening":
        return "Good evening!"

    elif user_input == "good night":
        return "Good night! Sweet dreams 🌙"

    # Chatbot identity
    elif user_input == "what is your name":
        return "I am a rule-based chatbot written in Python."

    elif user_input == "who created you":
        return "I was created by a student using Python programming."

    elif user_input == "are you a robot":
        return "Yes, I am a chatbot, not a human 🤖"

    elif user_input == "what language are you written in":
        return "I am written in the Python programming language."

    # Capabilities
    elif user_input == "what can you do":
        return ("I can respond to greetings, simple questions,\n"
                "and have a basic conversation with you.")

    elif user_input == "help":
        return ("Try typing:\n"
                "hello, how are you, good morning,\n"
                "what is your name, what can you do,\n"
                "thank you, bye")

    # Polite conversation
    elif user_input in ["thank you", "thanks", "thank u"]:
        return "You're welcome! 😊"

    elif user_input == "sorry":
        return "It's okay, no worries."

    elif user_input == "please":
        return "Sure! Let me know how I can help."

    # Personal questions
    elif user_input == "where are you from":
        return "I exist inside this computer program."

    elif user_input == "do you like me":
        return "Of course! I enjoy chatting with you 😊"

    elif user_input == "are you real":
        return "I'm real as a program, but not a human."

    # Fun interactions
    elif user_input == "tell me a joke":
        return "Why did the computer get cold? Because it forgot to close its windows 😂"

    elif user_input == "sing a song":
        return "La la la 🎵 I'm not a great singer, but I try!"

    elif user_input == "dance":
        return "💃🕺 (Imagine me dancing!)"

    # Study-related
    elif user_input == "what is python":
        return "Python is a high-level, easy-to-learn programming language."

    elif user_input == "what is a chatbot":
        return "A chatbot is a program that simulates human conversation."

    # Exit
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Thanks for chatting 👋"

    # Default
    else:
        return "Sorry, I don't understand that."

print("Chatbot: Hello! I am chatbot.")
print("Chatbot: Type 'bye' to end the conversation.")

while True:
    user = input("You: ")
    reply = chatbot_response(user)
    print("Chatbot:", reply)

    if user.lower() in ["bye", "exit", "quit"]:
        break
