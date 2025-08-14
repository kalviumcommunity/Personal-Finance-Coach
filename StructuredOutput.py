import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from typing import List
import dataclasses 

# --- Setup ---
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

# --- 1. Define the desired JSON structure using Dataclasses ---

@dataclasses.dataclass 
class Transaction:
    description: str
    category: str
    amount: float

@dataclasses.dataclass 
class CategorizedTransactions:
    transactions: List[Transaction]


# --- 2. Configure the model to use our schema ---
generation_config = genai.GenerationConfig(
    response_mime_type="application/json",
    response_schema=CategorizedTransactions
)

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=generation_config
)

# --- 3. Create a prompt with the raw data ---
prompt = """
Categorize the following list of financial transactions.
Use categories like: Food, Transport, Entertainment, Bills, Income, Shopping.

Transactions:
- Zomato Order: -350.00
- Uber ride to office: -180.50
- Salary Deposit: +50000.00
- Netflix Monthly Subscription: -499.00
- New Shoes from Nike: -7500.00
"""

# --- 4. Generate content and parse the structured response ---
print("--- Asking the AI for a structured JSON response ---")
response = model.generate_content(prompt)

print(" --- Raw JSON Output from AI ---")
print(response.text)

# Now, we can easily load the JSON string into a Python dictionary
parsed_data = json.loads(response.text)

print("--- Parsed Python Dictionary ---")
print(parsed_data)

print(" --- Easy Data Access --- ")
first_transaction_category = parsed_data['transactions'][0]['category']
print(f"The category of the first transaction is: '{first_transaction_category}'")


"""
--- Asking the AI for a structured JSON response --

 --- Raw JSON Output from AI --- 

{"transactions":[{"amount":-350.00,"category":"Food","description":"Zomato Order"},{"amount":-180.50,"category":"Transport","description":"Uber ride to office"},{"amount":50000.00,"category":"Income","description":"Salary Deposit"},{"amount":-499.00,"category":"Entertainment","description":"Netflix Monthly Subscription"},{"amount":-7500.00,"category":"Shopping","description":"New Shoes from Nike"}]}

 --- Parsed Python Dictionary --- 

{'transactions': [{'amount': -350.0, 'category': 'Food', 'description': 'Zomato Order'}, {'amount': -180.5, 'category': 'Transport', 'description': 'Uber ride to office'}, {'amount': 50000.0, 'category': 'Income', 'description': 'Salary Deposit'}, {'amount': -499.0, 'category': 'Entertainment', 'description': 'Netflix Monthly Subscription'}, {'amount': -7500.0, 'category': 'Shopping', 'description': 'New Shoes from Nike'}]}

 --- Easy Data Access --- 

The category of the first transaction is: 'Food'
"""