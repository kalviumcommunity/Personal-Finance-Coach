import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

# Initialize the Gemini Model
model = genai.GenerativeModel('gemini-2.5-flash')

# Data
expense_data = [
    {"date": "2025-06-05", "description": "Coffee with friend", "amount": 450.00},
    {"date": "2025-06-12", "description": "Movie tickets", "amount": 780.00},
    {"date": "2025-06-15", "description": "Electricity Bill", "amount": 1350.50},
    {"date": "2025-06-21", "description": "Restaurant dinner", "amount": 2200.00},
    {"date": "2025-06-28", "description": "Online Shopping", "amount": 3500.00},
    {"date": "2025-07-02", "description": "Groceries", "amount": 4200.75},
    {"date": "2025-07-10", "description": "Fuel for car", "amount": 2000.00},
    {"date": "2025-07-22", "description": "Zomato Order", "amount": 560.00},
    {"date": "2025-07-25", "description": "Weekend trip booking", "amount": 8500.00},
    {"date": "2025-07-28", "description": "Lunch at work", "amount": 250.00},
    {"date": "2025-07-28", "description": "New headphones", "amount": 4999.00},
    {"date": "2025-07-29", "description": "Uber ride", "amount": 175.00}
]

expenses_json_str = json.dumps(expense_data, indent=2)


# Prompt for AI Analysis
analysis_prompt = f"""
You are a helpful AI assistant. Your task is to track user expenses based on the provided transaction data and answer questions about it.

Transaction Data:
```json
{expenses_json_str}

Context:
Assume the current date is July 28th, 2025. A week runs from Monday to Sunday.

User Request:
Tell me the total expenses for today, this week, and this month. Provide a clear, simple summary of the spending.
"""

response = model.generate_content(analysis_prompt)

print(response.text)

# Ai response 
"""
Here's a summary of your expenses:

*   **Today (July 28th, 2025):** You spent **5249.0**.
*   **This Week (July 28th - August 3rd, 2025):** You have spent **5424.0** so far.
*   **This Month (July 2025):** Your total expenses are **20684.75**.
"""