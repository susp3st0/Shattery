# Install: pip install chatterbot chatterbot-corpus
import time

# Fix for Python 3.8+ where time.clock() was removed
if not hasattr(time, 'clock'):
    time.clock = time.perf_counter

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Create chatbot 
chatbot = ChatBot('MiniBot', storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///database.sqlite3')

# Train with basic data
trainer = ChatterBotCorpusTrainer(chatbot)
try:
    trainer.train("chatterbot.corpus.english")
except FileNotFoundError:
    print("\n[!] Corpus not found. Please install it: pip install chatterbot-corpus\n")

# Train with custom conversations
custom_trainer = ListTrainer(chatbot)
custom_trainer.train([
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
])

# Chat loop
while True:
    response = chatbot.get_response(user_input)
    print(f"Bot: {response}")