from telethon import TelegramClient, events
import logging

# ========= CONFIG =========
api_id = 30536759              # apna real API ID daalo
api_hash = "2633cf40ebefbc2a2b62a4439978e41c" # apna real API HASH daalo
# ==========================

logging.basicConfig(level=logging.INFO)

client = TelegramClient(
    "userbot",
    api_id,
    api_hash,
    connection_retries=10,
    timeout=20
)

@client.on(events.NewMessage(incoming=True))
async def auto_reply(event):
    if event.out:
        return
    try:
        print("Incoming:", event.raw_text)
        await event.reply("I'm on")
    except Exception as e:
        print("Reply error:", e)

print("Starting userbot...")
client.start()   # first run pe phone + OTP maangega (local pe karo)
print("Userbot is running...")
client.run_until_disconnected()
