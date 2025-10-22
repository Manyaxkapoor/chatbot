import os
from groq import Groq
from dotenv import load_dotenv

print("🚀 Script STARTED - Checking setup...")

# Load environment variables
load_dotenv()

# Check if API key is loaded
api_key = os.getenv("GROQ_API_KEY")
print(f"🔑 API Key loaded: {api_key is not None}")
if api_key:
    print(f"   Key starts with: {api_key[:10]}...")

# Initialize Groq client
try:
    client = Groq(api_key=api_key)
    print("✅ Groq client initialized successfully")
except Exception as e:
    print(f"❌ Groq client failed: {e}")
    exit(1)

print("🤖 Making API call now...")

# Make the API call - NO function, just direct code
try:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": "Say just 'Hello World' and nothing else."}
        ],
        temperature=0.1,
        max_tokens=10
    )
    
    answer = response.choices[0].message.content
    print(f"✅ SUCCESS! API Response: '{answer}'")
    print("🎉 Check your Groq dashboard - you should see this request!")
    
except Exception as e:
    print(f"❌ API Call Failed: {e}")

print("🏁 Script COMPLETED")