import os
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime

# --- Setup ---
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel('gemini-2.5-flash')

# --- The Prompt Template ---
prompt_template = """
You are FinCoach, a helpful personal finance assistant.

Today's Date: {date}
User's Name: {user_name}

User's Request:
Based on my goal to '{user_goal}', please give me one simple, actionable tip.
"""

# --- 2. Gather Dynamic Data ---
user_data = {
    "name": "Aditya",
    "goal": "save up for a down payment on a house"
}

# This is real-time dynamic data.
current_date = datetime.now().strftime("%B %d, %Y")


# --- 3. Construct the Final Prompt ---
final_prompt = prompt_template.format(
    date=current_date,
    user_name=user_data["name"],
    user_goal=user_data["goal"]
)

# --- 4. Run the Conversation ---
print("FinCoach's Dynamic Response ")

response = model.generate_content(final_prompt)
print(response.text)

# Ai response 

"""
FinCoach's Dynamic Response 
Hello Aditya! Today is August 14, 2025.

That's a fantastic goal, saving for a down payment on a house! Here is one simple, actionable tip for you:

**Automate your savings.** Set up an automatic transfer from your checking account to a dedicated high-yield savings account specifically for your down payment, scheduled for each payday. Even if it's a small amount to start, consistency is key!
"""