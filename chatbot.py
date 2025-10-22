import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

FAQ_DATA = """
Q: How do I reset my password?
A: Click 'Forgot Password' on the login page, enter your email, and follow the link sent to you.

Q: What are your support hours?
A: Our support team is available Monday-Friday, 9 AM to 5 PM EST.

Q: How do I update my billing information?
A: Go to Settings > Billing > Update Payment Method.

Q: What browsers do you support?
A: We support Chrome, Firefox, Safari, and Edge (latest two versions).

Q: How do I cancel my subscription?
A: Go to Settings > Subscription > Cancel Subscription. You'll retain access until the end of your billing period.
"""

SYSTEM_PROMPT = f"""You are a helpful technical support chatbot for our software company.

Rules:
1. Answer questions using ONLY the FAQ information below
2. Be concise, friendly, and professional
3. If the question isn't in the FAQ, politely say you don't have that information and suggest contacting im.manyakapoor@gmail.com
4. Never make up information

FAQ Database:
{FAQ_DATA}
"""

def ask_chatbot(question):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        temperature=0,
        max_tokens=200
    )
    return response.choices[0].message.content

def main():
    print("=" * 60)
    print("🤖 Technical Support FAQ Chatbot")
    print("=" * 60)
    print("Type 'quit' or 'exit' to end the conversation\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("👋 Thank you for using our support chatbot!")
            break
        
        if not user_input:
            continue
        
        print("🤖 Bot: ", end="")
        response = ask_chatbot(user_input)
        print(response)
        print()

if __name__ == "__main__":
    main()
