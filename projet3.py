def chatbot():
    print("Chatbot: Hello! Type something (type 'bye' to exit)\n")
    
    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Chatbot: Hi there!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks! How about you?")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif user_input == "help":
            print("Chatbot: Try saying 'hello', 'how are you', or 'bye'.")
        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()