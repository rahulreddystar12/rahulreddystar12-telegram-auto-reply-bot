import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# Load from environment
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
session_string = os.getenv('SESSION_STRING')

# Initialize with StringSession
client = TelegramClient(StringSession(session_string), api_id, api_hash)

replied_users = set()

reply_text = (
    "👋 Hello!\n\n"
    "Thank you for reaching out.\n\n"
    "🎯 To get exclusive access to our VIP channel, please complete a one-time payment of ₹249.\n\n"
    "🔹 How to join:\n"
    "1️⃣ Copy this link and open it in your browser:\n"
    "   https://payments.cashfree.com/forms/thedesire\n"
    "2️⃣ Enter ₹249 as the payment amount\n"
    "3️⃣ Complete the payment process\n"
    "4️⃣ Send me a screenshot of your successful payment here\n\n"
    "🌟 VIP Channel perks:\n"
    "• No spam or irrelevant links\n"
    "• Weekly exclusive content updates\n"
    "• Direct admin support for your queries\n\n"
    "⚠️ Note: Responses will be limited until payment confirmation is received.\n\n"
    "Looking forward to welcoming you aboard! 🚀"
)


@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:
        sender_id = event.sender_id
        if sender_id not in replied_users:
            await client.send_message(
                event.chat_id, reply_text,
                parse_mode=None,
                link_preview=False
            )
            replied_users.add(sender_id)

print("🤖 Auto-reply is active. Press Ctrl+C to stop.")
client.start()
client.run_until_disconnected()
