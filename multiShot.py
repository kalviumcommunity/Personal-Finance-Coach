import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# --- Setup ---
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

# --- 1. Define the System Instruction (with examples and rules) ---
system_instruction = """
You are a financial data analyst assistant. Your task is to analyze historical stock price data to identify patterns based on a specific rule.

**IMPORTANT RULES:**
- You DO NOT give financial advice or predict future prices.
- You ONLY analyze the historical data provided.
- Your analysis must be based *exclusively* on the rule defined in the examples.
- The rule for an 'Opportune Day' is a day where the stock price increased by at least 5% within the subsequent 3 trading days.

---
**Example 1**

Stock Trend Data:
```json
[
  {"day": 1, "price": 100},
  {"day": 2, "price": 95},
  {"day": 3, "price": 98},
  {"day": 4, "price": 105}
]
AI Response:

JSON

{
  "opportune_days": [
    {
      "day": 2,
      "price": 95,
      "reason": "The price increased to 105 (a 10.5% gain) within 2 days, which meets the >5% gain within 3 days rule."
    }
  ]
}
Example 2

Stock Trend Data:

JSON

[
  {"day": 1, "price": 200},
  {"day": 2, "price": 201},
  {"day": 3, "price": 202},
  {"day": 4, "price": 203}
]
AI Response:

JSON

{
  "opportune_days": []
}
"""

model = genai.GenerativeModel(
model_name='gemini-2.5-flash',
system_instruction=system_instruction
)

stock_data_10_days = [
{"day": 1, "price": 150},
{"day": 2, "price": 145},
{"day": 3, "price": 140}, 
{"day": 4, "price": 142},
{"day": 5, "price": 148}, 
{"day": 6, "price": 146},
{"day": 7, "price": 155},
{"day": 8, "price": 152},
{"day": 9, "price": 153},
{"day": 10, "price": 150}
]
stock_data_str = json.dumps(stock_data_10_days, indent=2)

user_prompt = f"""
Please analyze the following 10-day stock trend data for 'TechCorp Inc.' based on the rule.

Stock Trend Data:

JSON

{stock_data_str}
"""

chat = model.start_chat()
response = chat.send_message(user_prompt)

print(response.text)

# Ai response 

""" ```json
{
  "opportune_days": [
    {
      "day": 3,
      "price": 140,
      "reason": "The price increased to 148 (a 5.71% gain) on Day 5, which is within 2 days and meets the >5% gain within 3 days rule."
    },
    {
      "day": 4,
      "price": 142,
      "reason": "The price increased to 155 (a 9.15% gain) on Day 7, which is within 3 days and meets the >5% gain within 3 days rule."     
    },
    {
      "day": 6,
      "price": 146,
      "reason": "The price increased to 155 (a 6.16% gain) on Day 7, which is within 1 day and meets the >5% gain within 3 days rule."      
    }
  ]
}"""