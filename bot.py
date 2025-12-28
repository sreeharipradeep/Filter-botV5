from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import start, filters, admin

app = Client(
    "RoseStyleFilterBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

start.register(app)
filters.register(app)
admin.register(app)

app.run()
