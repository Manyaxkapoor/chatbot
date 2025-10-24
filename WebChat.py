import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ============================================
# FAQ DATABASE
# ============================================
FAQ_DATA = """
═══════════════════════════════════════════════════════════════
ACCOUNT MANAGEMENT
═══════════════════════════════════════════════════════════════

Q: How do I reset my password?
A: Click 'Forgot Password' on the login page, enter your email, and you'll receive a reset link within 5 minutes. The link expires after 1 hour.

Q: How do I change my email address?
A: Go to Settings > Account > Email Address. Enter your new email and verify it through the confirmation link sent to both old and new addresses.

Q: How do I change my username?
A: Go to Settings > Profile > Username. Note: You can only change your username once every 30 days.

Q: How do I delete my account permanently?
A: Go to Settings > Account > Delete Account. Enter your password and type "DELETE" to confirm. This action is permanent and cannot be undone. All data will be erased within 30 days.

Q: Can I recover a deleted account?
A: If deleted within the last 7 days, contact support@example.com immediately. After 7 days, recovery is impossible.

Q: How do I enable two-factor authentication (2FA)?
A: Go to Settings > Security > Two-Factor Authentication. Scan the QR code with Google Authenticator or Authy.

Q: I'm locked out of my account. What do I do?
A: After 5 failed login attempts, accounts are locked for 30 minutes. Contact support@example.com if you need immediate access.

═══════════════════════════════════════════════════════════════
BILLING & PAYMENTS
═══════════════════════════════════════════════════════════════

Q: What payment methods do you accept?
A: We accept Visa, Mastercard, American Express, Discover, PayPal, Apple Pay, Google Pay, and ACH bank transfers (US only).

Q: How do I update my billing information?
A: Go to Settings > Billing > Payment Methods. Click "Add New Card" or "Edit" on existing cards. Changes apply to future charges only.

Q: When will I be charged?
A: Billing occurs on the same day each month based on your signup date. For annual plans, you're charged once per year.

Q: How do I cancel my subscription?
A: Go to Settings > Subscription > Cancel Subscription. You'll retain full access until your current billing period ends. No partial refunds for remaining time.

Q: Can I get a refund?
A: Yes, full refunds available within 14 days of initial purchase. Contact support@example.com with your order number. Subsequent renewals are non-refundable.

Q: Do you offer discounts?
A: Yes! Students (50% off with .edu email), nonprofits (40% off with verification), annual plans (20% savings), and referrals (1 month free per referral).

Q: Why was my payment declined?
A: Common reasons: insufficient funds, expired card, incorrect CVV, or bank blocking the charge. Try another payment method or contact your bank.

═══════════════════════════════════════════════════════════════
TECHNICAL SUPPORT
═══════════════════════════════════════════════════════════════

Q: What are your support hours?
A: Standard support: Monday-Friday, 9 AM - 5 PM EST. Premium users get 24/7 support including weekends and holidays.

Q: What browsers do you support?
A: Chrome 100+, Firefox 95+, Safari 15+, Edge 100+. We support the latest 2 major versions of each browser.

Q: Why is the application running slowly?
A: Try these steps: 1) Clear browser cache and cookies 2) Disable browser extensions 3) Close unnecessary tabs 4) Check your internet speed (need 5+ Mbps) 5) Try incognito mode.

Q: Is there a mobile app?
A: Yes! Download from App Store (iOS 14+) or Google Play (Android 10+). Mobile apps have all features except advanced reporting.

Q: What are the system requirements?
A: Minimum: 4GB RAM, modern browser updated within 6 months, stable internet (5 Mbps download, 1 Mbps upload), screen resolution 1280x720 or higher.

Q: How do I report a bug?
A: Go to Help > Report Bug, or email bugs@example.com with: 1) What you were doing 2) What happened 3) Screenshots 4) Browser/device info.

Q: Do you support screen readers?
A: Yes, we're WCAG 2.1 AA compliant. Best experience with JAWS, NVDA, or VoiceOver.

Q: Can I use keyboard shortcuts?
A: Yes! Press '?' anywhere to see all shortcuts. Common ones: Ctrl+S (save), Ctrl+/ (search), Esc (close modal).

═══════════════════════════════════════════════════════════════
FEATURES & USAGE
═══════════════════════════════════════════════════════════════

Q: How do I export my data?
A: Go to Settings > Data > Export Data. Choose format (CSV, JSON, or PDF). You'll receive a download link within 24 hours.

Q: Can I share my account with others?
A: No, accounts are for individual use only. Consider our Team plan ($49/month for 5 users) for collaboration.

Q: Is my data encrypted?
A: Yes! AES-256 encryption for data at rest, TLS 1.3 for data in transit. We're SOC 2 Type II certified.

Q: Do you offer an API?
A: Yes, API access included in Pro ($49/month) and Enterprise plans. See docs.example.com/api for documentation.

Q: How often is data backed up?
A: Automatic backups every 6 hours. Manual backups available anytime at Settings > Data > Backup Now. Backups retained for 90 days.

Q: Can I customize the interface?
A: Yes! Go to Settings > Appearance. Choose themes (light/dark/auto), adjust font size, and rearrange dashboard widgets.

Q: What's the file size limit for uploads?
A: Free: 10MB per file, Pro: 100MB per file, Enterprise: 1GB per file. Total storage: Free (2GB), Pro (100GB), Enterprise (unlimited).

═══════════════════════════════════════════════════════════════
PLANS & PRICING
═══════════════════════════════════════════════════════════════

Q: What plans do you offer?
A: Free (basic features, 2GB storage), Pro ($19/month or $190/year, advanced features, 100GB storage), Enterprise (custom pricing, unlimited everything, dedicated support).

Q: Can I switch plans anytime?
A: Yes! Upgrade takes effect immediately. Downgrade takes effect at next renewal. You're never charged twice in one billing period.

Q: Is there a free trial?
A: Yes, 14-day free trial of Pro plan. No credit card required. Trial includes all Pro features.

Q: What happens if I downgrade?
A: You keep access to Pro features until your billing period ends. After that, features are limited to Free plan. Data is retained for 60 days.

Q: Do you offer educational discounts?
A: Yes! Students and teachers get 50% off with valid .edu email. Verify at Settings > Billing > Student Discount.
"""

# ============================================
# SYSTEM PROMPT
# ============================================
SYSTEM_PROMPT = f"""You are a friendly and helpful customer support chatbot for our software company.

CORE RULES:
1. Answer questions using ONLY information from the FAQ database below
2. If information is NOT in the FAQ, respond: "I don't have that information. Please contact support@example.com or call 1-800-SUPPORT for help."
3. Remember the entire conversation and refer back to previous questions when relevant
4. Be conversational and friendly
5. Be concise but complete
6. Never make up information

FAQ DATABASE:
{FAQ_DATA}
"""

# ============================================
# CHATBOT FUNCTION
# ============================================
def get_bot_response(conversation_history):
    """Get response from chatbot with memory"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=conversation_history,
        temperature=0,
        max_tokens=400
    )
    return response.choices[0].message.content

# ============================================
# STREAMLIT PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="FAQ Support Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CUSTOM CSS
# ============================================
st.markdown("""
<style>
    .main {
        background-color: #f5f7fa;
    }
    .stChatMessage {
        background-color: black;
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    h1 {
        color: #2c3e50;
    }
    .sidebar-info {
        background-color: #e8f4f8;
        padding: 15px;
        border-radius: 20px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# SIDEBAR
# ============================================
with st.sidebar:
    st.title("🤖 FAQ Chatbot")
    st.markdown("---")
    
    st.markdown("### 📚 Knowledge Categories")
    st.markdown("""
    - 🔐 Account Management
    - 💳 Billing & Payments
    - 🛠️ Technical Support
    - ⚙️ Features & Usage
    - 💰 Plans & Pricing
    """)
    
    st.markdown("---")
    
    # # Statistics
    # if "messages" in st.session_state:
    #     # Count only user messages (exclude system prompt)
    #     user_messages = [m for m in st.session_state.messages if m["role"] == "user"]
    #     st.markdown("### 📊 Session Stats")
    #     st.info(f"**Questions Asked:** {len(user_messages)}")
    
    # st.markdown("---")
    
    # Clear chat button
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
        st.rerun()
    
    st.markdown("---")
    
    # Help section
    with st.expander("ℹ️ How to Use"):
        st.markdown("""
        1. Type your question in the chat box
        2. Press Enter or click Send
        3. The bot remembers all previous questions
        4. Ask follow-up questions naturally
        5. Click 'Clear Conversation' to start fresh
        """)
    
    with st.expander("💡 Example Questions"):
        st.markdown("""
        - How do I reset my password?
        - What payment methods do you accept?
        - Do you offer a free trial?
        - What are your support hours?
        - How do I export my data?
        """)
    
    st.markdown("---")
    st.caption("Powered by GROQ")
    st.caption("Manya Kapoor")

# ============================================
# MAIN CHAT INTERFACE
# ============================================

# Title
st.title("💬 Customer Support Chatbot")
st.markdown("**Ask me anything about our service! I remember our conversations.**")
st.markdown("---")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    # Add welcome message
    st.session_state.messages.append({
        "role": "assistant",
        "content": "👋 Heyaa! I'm your support assistant. I can help with account management, billing, technical issues, features, and pricing. What would you like to know?"
    })

# Display chat history (skip system message)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your question here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_bot_response(st.session_state.messages)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

