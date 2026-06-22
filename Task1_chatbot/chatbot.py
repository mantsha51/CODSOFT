print("YOUR VERY OWN RULE BASED CHATBOT!!")

print("Text 'bye'or 'bye!!!' to end chat<3")

name = input("Enter your name: ")
print("Hello", name, "! Nice to meet you.")

while True:

    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hi! How are you?")

    elif user == "im fine" or user =="im good":
        print("Bot: That's great!") 
        
    elif user == "thank you" or user == "thanks":
        print("Bot: You're welcome!")

    elif user == "what are you?" or user == "what are you":
        print("Bot: I am a chatbot made by mantsha.")

    elif user == "who am i":
        print("Bot:", name, ", you are my user!")

    elif user == "how are you":
         print("Bot: I am doing great!")

    elif user == "who created you":
         print("Bot: I was created by Mantsha Rizvi.")

    elif user == "what is your favorite color":
        print("Bot: I like pastel pink because my creater likes it too!")

    elif user == "good morning":
         print("Bot: Good morning!", name)

    elif user == "good night" or user == "goodnight":
        print("Bot: Good night! sleep well!!")

    elif user == "bye" or user == "bye!!!":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")