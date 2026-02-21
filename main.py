from telethon import TelegramClient, events

# --- अपनी जानकारी यहाँ भरें ---
API_ID = 34949178
API_HASH = '8e443b273d4a1b0c9d8c51158365a314'
BOT_TOKEN = '8535209367:AAGWQo0PB39eD0qIE4iXPxzcpTwNUf-Hy9s' # अपना असली टोकन यहाँ डालें
# ---------------------------

client = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

print("✅ बोट सफलतापूर्वक चालू हो गया है!")

@client.on(events.ChatAction)
async def handler(event):
    if event.user_joined or event.user_added:
        user = await event.get_user()
        full_name = f"{user.first_name} {user.last_name or ''}".strip()
        
        welcome_text = (
            f"📢 **नया मेंबर ग्रुप में आया है!**\n\n"
            f"👤 **नाम:** {full_name}\n"
            f"🆔 **ID:** `{user.id}`\n"
            f"🔗 **यूजरनेम:** @{user.username if user.username else 'N/A'}"
        )
        await event.reply(welcome_text)

client.run_until_disconnected()
