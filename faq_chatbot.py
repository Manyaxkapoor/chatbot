import os
from datetime import datetime
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ============================================
# EXPANDED FAQ DATABASE
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

Q: Can I merge multiple accounts?
A: No, account merging is not supported. You'll need to manually transfer data between accounts.

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

Q: Can I change my billing cycle?
A: Yes, contact support@example.com. Changes take effect on your next renewal date.

Q: Do you offer invoices?
A: Yes, invoices are automatically emailed after each payment. Access past invoices at Settings > Billing > Invoice History.

Q: What currency do you charge in?
A: USD by default. International customers see charges converted by their bank's exchange rate.

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

Q: Can I use the app offline?
A: Limited offline mode available in mobile apps. Desktop browser version requires constant internet connection.

Q: How do I report a bug?
A: Go to Help > Report Bug, or email bugs@example.com with: 1) What you were doing 2) What happened 3) Screenshots 4) Browser/device info.

Q: The app won't load. What should I do?
A: 1) Check status.example.com for outages 2) Clear cache 3) Try different browser 4) Disable VPN 5) Check firewall settings.

Q: Do you support screen readers?
A: Yes, we're WCAG 2.1 AA compliant. Best experience with JAWS, NVDA, or VoiceOver.

Q: Can I use keyboard shortcuts?
A: Yes! Press '?' anywhere to see all shortcuts. Common ones: Ctrl+S (save), Ctrl+/ (search), Esc (close modal).

═══════════════════════════════════════════════════════════════
FEATURES & USAGE
═══════════════════════════════════════════════════════════════

Q: How do I export my data?
A: Go to Settings > Data > Export Data. Choose format (CSV, JSON, or PDF). You'll receive a download link within 24 hours.

Q: How do I import data?
A: Go to Settings > Data > Import. Supports CSV, JSON, and Excel files up to 50MB. Follow the template provided.

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

Q: How do I collaborate with team members?
A: Upgrade to Team plan. Invite members via Settings > Team > Invite. Set permissions: Admin, Editor, or Viewer.

Q: What's the file size limit for uploads?
A: Free: 10MB per file, Pro: 100MB per file, Enterprise: 1GB per file. Total storage: Free (2GB), Pro (100GB), Enterprise (unlimited).

Q: Can I integrate with other tools?
A: Yes! Native integrations with Slack, Zapier, Google Workspace, Microsoft 365, Salesforce, and 50+ others. See Settings > Integrations.

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

Q: What's included in the Enterprise plan?
A: Everything in Pro, plus: unlimited storage, unlimited users, priority support, dedicated account manager, custom integrations, SLA guarantee, advanced security features.

Q: Can I pay annually?
A: Yes! Annual plans save 20%: Pro $190/year (save $38), Enterprise gets volume discounts.

Q: Do you offer a money-back guarantee?
A: Yes, 14-day money-back guarantee on first purchase. No questions asked.
"""

# ============================================
# SYSTEM PROMPT
# ============================================
SYSTEM_PROMPT = f"""You are a friendly and helpful customer support chatbot for our software company.

CORE RULES:
1. Answer questions using ONLY information from the FAQ database below
2. If information is NOT in the FAQ, respond: "I don't have that information. Please contact im.manyakspoor@gmail.com for help."
3. Remember the entire conversation and refer back to previous questions when relevant
4. Be conversational - use phrases like "As I mentioned earlier..." or "Going back to your question about..."
5. Be concise but complete
6. Maintain a friendly, professional tone
7. Never make up information

FAQ DATABASE:
{FAQ_DATA}
"""

# ============================================
# CHATBOT WITH MEMORY
# ============================================
class ChatBot: 
    # this is used to help bot remember the prev conversation_history

    def __init__(self):
        """Initialize chatbot with conversation memory"""
        self.conversation_history = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
        self.message_count = 0
    
    def ask(self, question):
        """Ask a question - bot remembers all previous questions"""
        
        # Add user's question to memory
        self.conversation_history.append({
            "role": "user",
            "content": question
        })
        
        # Get response with FULL conversation context
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=self.conversation_history,  # Entire conversation!
            temperature=0,  # Deterministic
            max_tokens=400
        )
        
        answer = response.choices[0].message.content
        
        # Add bot's answer to memory
        self.conversation_history.append({
            "role": "assistant",
            "content": answer
        })
        
        self.message_count += 1
        return answer
    
    def clear_memory(self):
        """Start fresh conversation"""
        self.conversation_history = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
        self.message_count = 0

# ============================================
# SIMPLE CLEAN INTERFACE
# ============================================
def main():
    print("\n" + "=" * 70)
    print("🤖 FAQ SUPPORT CHATBOT")
    print("=" * 70)
    print("\n I can help with:")
    print("• Account Management  • Billing & Payments  • Technical Support")
    print("• Features & Usage    • Plans & Pricing")
    print("\n Commands:")
    print("• 'new' - Start fresh conversation")
    print("• 'quit' - Exit")
    print("\n I remember everything we discuss in this conversation!\n")
    print("-" * 70 + "\n")
    
    bot = ChatBot()
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Handle empty input
        if not user_input:
            continue
        
        # Handle quit
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print(f"\nThanks for chatting! We had {bot.message_count} exchanges ;)")
            print("Have a great day!\n")
            break
        
        # Handle new conversation
        if user_input.lower() in ['new', 'clear', 'reset']:
            confirm = input("\n  Start a new conversation? I'll forget everything (yes/no): ").lower()
            if confirm in ['yes', 'y']:
                bot.clear_memory()
                print("✅ Memory cleared! Let's start fresh.\n")
            continue
        
        # Get bot response
        answer = bot.ask(user_input)
        print(f"\n🤖 Bot: {answer}\n")
        print("-" * 70 + "\n")

if __name__ == "__main__":
    main()
