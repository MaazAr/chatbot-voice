from transformers import pipeline, Conversation

chatbot = pipeline(task="conversational", model="facebook/blenderbot-400M-distill")
while True:
    user_message = input("You: ")
    conversation = Conversation(user_message)
    conversation = chatbot(conversation)
    print(conversation)
