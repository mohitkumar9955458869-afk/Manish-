import os
from telethon import TelegramClient, events
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# आपकी सेटिंग्स
API_ID = 34949178
API_HASH = '8e443b273d4a1b0c9d8c51158365a314'
TOKEN = '8577685759:AAHhIqqX0DYC6iws_PgJfOy86XWNAnS7eOU'

client = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=TOKEN)

# Welcome Message + ID निकालने वाला हिस्सा
@client.on(events.ChatAction)
async def welcome(event):
    if event.user_joined:
        user = await event.get_user()
        name = user.first_name
        user_id = user.id
        await event.reply(f"नमस्ते {name}!\nआपकी User ID है: `{user_id}`")

# Render के लिए पोर्ट चालू रखना (ताकि बोट न सोये)
class HealthCheck(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is Running")

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), HealthCheck)
    server.serve_forever()

print("--- Welcome Bot Shuru Ho Gaya Hai! ---")
threading.Thread(target=run_server, daemon=True).start()
client.run_until_disconnected()
        
