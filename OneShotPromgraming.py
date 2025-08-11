import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("API_KEY")

# Configure API key
genai.configure(api_key=api_key)

# Create model instance
model = genai.GenerativeModel("gemini-2.5-flash") 

# One-shot prompt: include 1 example before the real question
prompt = """
refrence
Question: Which city has the best culture in India like Kolkata?
Answer: Varanasi - Known for its spiritual depth, classical music heritage, and ancient traditions, similar to Kolkata's cultural richness.

question
Question: Which city has the best culture in India like Chennai?
"""

# Generate response
response = model.generate_content(prompt)

# Print the output
print(response.text)

# Gemini Response 

"""**Kolkata** - Known for its vibrant intellectual scene, deep-rooted classical music and literary traditions
 (Rabindra Sangeet, Bengali literature), and a strong emphasis on arts and education, 
 much like Chennai's focus on Carnatic music, Bharatnatyam, and Tamil culture.
 Both cities are cultural capitals of their respective regions, valuing tradition and artistic expression deeply.
"""
