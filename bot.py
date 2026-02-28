from telethon import TelegramClient, events
import logging

# ========= CONFIG =========
api_id = 30536759              # <-- apna API ID yahan daalo
api_hash = "2633cf40ebefbc2a2b62a4439978e41c" # <-- apna API HASH yahan daalo
# ==========================

logging.basicConfig(level=logging.INFO)

client = TelegramClient("userbot", api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def auto_reply(event):
    # Khud ke message ko ignore karo
    if event.out:
        return

    try:
        print("Incoming:", event.raw_text)
        await event.reply("I'm on")
    except Exception as e:
        print("Reply error:", e)

print("Starting userbot...")
client.start()   # first run pe phone number + OTP maangega
print("Userbot is running. Send me a DM to test.")
client.run_until_disconnected()
