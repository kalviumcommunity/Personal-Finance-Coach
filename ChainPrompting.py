import os
import google.generativeai as genai
from dotenv import load_dotenv

# Setup 
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

# 1. The System Instruction 
system_instruction = "You are an expert financial planning assistant that helps users create a detailed budget."

# 2. Initialize the Modek
model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    system_instruction=system_instruction
)

# 3. The User Prompt with CoT Instructions
user_prompt = """
Based on my financial data, create a monthly budget for me.

**First, provide a step-by-step thinking process on how you will calculate the budget allocation. After you have detailed all your reasoning steps, present the final, summarized budget in a clean Markdown table.**

My Financial Data:
- **Monthly Income:** ₹80,000
- **Fixed Expenses (Needs):**
  - Rent: ₹25,000
  - Utilities: ₹5,000
  - Loan Payment: ₹10,000
- **Financial Goals (Savings & Investments):**
  - Save 20% of my total income.
  - Invest a flat ₹5,000 into a mutual fund.

Begin your response with your step-by-step thinking process.
"""

# 4. Running the Conversation
chat = model.start_chat()
response = chat.send_message(user_prompt)

print(response.text)

# AI REsponse 

"""
Here's a detailed breakdown of the thinking process I'll use to create your monthly budget, followed by the summarized budget itself.       

### Step-by-Step Thinking Process for Budget Allocation

To create your monthly budget, I'll follow these logical steps:

1.  **Identify Total Monthly Income:** The foundational step is to clearly note down your entire monthly income. This is the total pool of money we have to work with.

2.  **Calculate Total Fixed Expenses (Needs):** These are your non-negotiable, essential expenses that typically remain constant each month. I will sum up all the provided "Needs" to get a subtotal for this category.
    *   Rent
    *   Utilities
    *   Loan Payment

3.  **Calculate Total Financial Goals (Savings & Investments):** This category includes money you set aside for your future financial well-being.
    *   First, I will calculate the specific percentage-based savings goal (20% of your total income).
    *   Next, I will add the flat, specific investment amount for the mutual fund.
    *   Crucially, I will treat these two goals as additive commitments. This means you want to both save 20% of your income *and* specifically invest ₹5,000 in a mutual fund, ensuring both objectives are met.

4.  **Calculate Remaining Income for Discretionary Spending (Wants):** After allocating funds to your essential "Needs" and your "Savings & Investments" goals, the remaining amount is what's left for your "Wants." This category is for flexible, non-essential spending that enhances your lifestyle but isn't strictly necessary (e.g., dining out, entertainment, hobbies, shopping, personal care, transport not covered by fixed needs). This is calculated by subtracting the total of "Needs" and "Savings & Investments" from your total monthly income.

5.  **Summarize and Present the Budget:** Finally, I will compile all these calculated figures into a clear, concise Markdown table. The table will categorize your income and expenses into logical sections (Income, Needs, Savings & Investments, and Wants) to provide an easy-to-understand overview. I will also ensure that the total allocated expenses perfectly balance with your total income.

---

### Your Monthly Budget

Based on your financial data and the thinking process above, here is your detailed monthly budget:

| Category                     | Item                       | Monthly Allocation (₹) |
| :--------------------------- | :------------------------- | :--------------------- |
| **I. Monthly Income**        | Salary / Earnings          | **80,000**             |
|                              |                            |                        |
| **II. Fixed Expenses (Needs)** | Rent                       | 25,000                 |
|                              | Utilities                  | 5,000                  |
|                              | Loan Payment               | 10,000                 |
| **Total Needs**              |                            | **40,000**             |
|                              |                            |                        |
| **III. Financial Goals (Savings & Investments)** | General Savings (20% of Income) | 16,000                 |
|                              | Mutual Fund Investment     | 5,000                  |
| **Total Savings & Investments** |                            | **21,000**             |
|                              |                            |                        |
| **IV. Discretionary Spending (Wants)** | Remaining for Flexible Spending | 19,000                 |
| **Total Wants**              |                            | **19,000**             |
|                              |                            |                        |
| **Total Monthly Outflow**    |                            | **80,000**             |
| **Remaining Balance**        | (Income - Total Outflow)   | **0**                  |

**Summary:**

*   **Income:** ₹80,000
*   **Needs:** ₹40,000 (50% of income)
*   **Savings & Investments:** ₹21,000 (26.25% of income)
*   **Wants:** ₹19,000 (23.75% of income)

This budget ensures all your fixed obligations are met and your financial goals are actively pursued, leaving a clear amount for your flexible spending each month.
"""