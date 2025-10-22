import os
import json
from datetime import datetime
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
"""

SYSTEM_PROMPT = f"""You are a technical support chatbot. Answer based ONLY on this FAQ:
{FAQ_DATA}
If information isn't available, say "I don't have information about that."""

class ChatbotLogger:
    def __init__(self, log_file="chatbot_log.json"):
        self.log_file = log_file
        self.logs = self.load_logs()
    
    def load_logs(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                return json.load(f)
        return []
    
    def log_interaction(self, question, answer, tokens_used):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "question": question,
            "answer": answer,
            "tokens_used": tokens_used
        }
        self.logs.append(log_entry)
        self.save_logs()
    
    def save_logs(self):
        with open(self.log_file, 'w') as f:
            json.dump(self.logs, f, indent=2)
    
    def get_stats(self):
        total_interactions = len(self.logs)
        total_tokens = sum(log.get('tokens_used', 0) for log in self.logs)
        return {
            "total_interactions": total_interactions,
            "total_tokens": total_tokens,
            "avg_tokens_per_interaction": total_tokens / total_interactions if total_interactions > 0 else 0
        }

logger = ChatbotLogger()

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
    
    answer = response.choices[0].message.content
    tokens_used = response.usage.total_tokens
    
    logger.log_interaction(question, answer, tokens_used)
    
    return answer

def main():
    print("🤖 FAQ Chatbot with Logging")
    print("Type 'stats' to see statistics, 'quit' to exit\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            stats = logger.get_stats()
            print(f"\n Session Statistics:")
            print(f"   Total interactions: {stats['total_interactions']}")
            print(f"   Total tokens used: {stats['total_tokens']}")
            print(f"   Average tokens per interaction: {stats['avg_tokens_per_interaction']:.2f}")
            break
        
        if user_input.lower() == 'stats':
            stats = logger.get_stats()
            print(f"\n Current Statistics:")
            print(f"   Total interactions: {stats['total_interactions']}")
            print(f"   Total tokens used: {stats['total_tokens']}")
            print(f"   Average tokens: {stats['avg_tokens_per_interaction']:.2f}\n")
            continue
        
        if not user_input:
            continue
        
        print("||Bot||:", ask_chatbot(user_input))
        print()

if __name__ == "__main__":
    main()
