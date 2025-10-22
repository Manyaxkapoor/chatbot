import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Define your FAQ knowledge base
FAQ_DATA = """
Q: How do I reset my password?
A: Click 'Forgot Password' on the login page, enter your email, and follow the link sent to you.

Q: What are your support hours?
A: Our support team is available Monday-Friday, 9 AM to 5 PM EST.

Q: How do I update my billing information?
A: Go to Settings > Billing > Update Payment Method.

Q: What browsers do you support?
A: We support Chrome, Firefox, Safari, and Edge (latest two versions).
"""

# System prompt - this controls the chatbot's behavior
SYSTEM_PROMPT = f"""You are a technical support chatbot. Your job is to answer customer questions based ONLY on the FAQ information provided below.

Rules:
1. Only answer questions using information from the FAQ
2. If a question is not covered in the FAQ, say "I don't have information about that. Please contact support@example.com"
3. Be concise and helpful
4. Always maintain a professional tone
5. Do not make up information

FAQ Information:
{FAQ_DATA}
"""

def ask_faq_chatbot(question):
    """Ask the FAQ chatbot a question"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        temperature=0,  # Set to 0 for maximum determinism!
        max_tokens=200
    )
    return response.choices[0].message.content

# Test with multiple questions
if __name__ == "__main__":
    test_questions = [
        "How do I reset my password?",
        "What are your support hours?",
        "Can you help me with programming?",  # Not in FAQ
        "What browsers work with your app?"
    ]
    
    for question in test_questions:
        print(f"\n❓ Question: {question}")
        print(f"💬 Answer: {ask_faq_chatbot(question)}")
        print("-" * 60)