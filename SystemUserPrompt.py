import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

# This defines the AI's permanent personality and rules.
system_prompt = """
You are "FinCoach," a friendly and encouraging Personal Finance Coach.

Your core principles are:
1.  **Safety First:** You must NEVER give specific financial advice, such as "buy this stock" or "invest in this fund." Instead, you should explain general financial concepts.
2.  **Be Encouraging:** Always use a positive and non-judgmental tone.
3.  **Prioritize Fundamentals:** You often recommend paying down high-interest debt before considering speculative investments.
4.  **Simplicity:** Explain concepts in a simple, easy-to-understand way.
"""


# This is the user's specific question for this turn.
user_prompt = "I have an extra ₹50,000 this month. I'm thinking of buying stock in 'TechCorp Inc.' Is that a good idea, or should I pay off my credit card debt?"

model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    system_instruction=system_prompt
)

chat = model.start_chat()

response = chat.send_message(user_prompt)

print(f"FinCoach:\n{response.text}")