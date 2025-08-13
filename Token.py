import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

# --- 1. System Instruction with Few-Shot Examples ---
# We teach the model how to behave by giving it a role and examples.
system_instruction = """
You are a text processing utility. Your only function is to take a piece of text and show how a Large Language Model would tokenize it.
A token can be a word, part of a word (a sub-word), or punctuation.
You must return the output as a Python list of strings. Do not add any other explanation.

---
**Example 1:**
User Text: "Hello, world!"
AI Response:
["Hello", ",", " world", "!"]
---
**Example 2:**
User Text: "Tokenization is complex."
AI Response:
["Token", "ization", " is", " complex", "."]
---
"""

#Initialize the Model with the Tokenizer Role
model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    system_instruction=system_instruction
)

# Define the Text We Want to Tokenize 
text_to_tokenize = "Should I invest in stocks? It feels risky."

#  Running the "Tokenizer" 
chat = model.start_chat()

print(f"Original Text: '{text_to_tokenize}'\n")
print("Asking AI to demonstrate tokenization")

response = chat.send_message(text_to_tokenize)

print(response.text)

# Ai Response 
"""
Original Text: 'Should I invest in stocks? It feels risky.'

Asking AI to demonstrate tokenization
["Should", " I", " invest", " in", " stocks", "?", " It", " feels", " risky", "."]
"""