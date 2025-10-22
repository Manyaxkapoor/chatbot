import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

FAQ_DATA = """
Q: How do I reset my password?
A: Click 'Forgot Password' on the login page, enter your email, and follow the link sent to you.
"""

SYSTEM_PROMPT = f"""You are a technical support chatbot. Answer questions based ONLY on this FAQ:
{FAQ_DATA}
Be concise and professional."""

def ask_chatbot(question, temperature=0):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        temperature=temperature,
        max_tokens=150
    )
    return response.choices[0].message.content

# Test the same question 5 times
if __name__ == "__main__":
    question = "How do I reset my password?"
    
    print("Testing with temperature=0 (Deterministic):")
    print("=" * 60)
    responses_deterministic = []
    for i in range(5):
        response = ask_chatbot(question, temperature=0)
        responses_deterministic.append(response)
        print(f"Response {i+1}: {response}\n")
    
    # Check if all responses are identical
    all_same = all(r == responses_deterministic[0] for r in responses_deterministic)
    print(f"All responses identical: {all_same}")
    print(f"Determinism rate: {(responses_deterministic.count(responses_deterministic[0]) / 5) * 100}%")
    
    print("\n" + "=" * 60)
    print("Testing with temperature=0.7 (Non-deterministic):")
    print("=" * 60)
    for i in range(5):
        response = ask_chatbot(question, temperature=0.7)
        print(f"Response {i+1}: {response}\n")
