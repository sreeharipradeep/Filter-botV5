from pyrogram import filters
from config import ADMINS

def register(app):

    @app.on_message(filters.command("stats") & filters.user(ADMINS))
    async def stats(_, message):
        await message.reply("🌹 Rose-Style Filter Bot Running")

    @app.on_message(filters.command("broadcast") & filters.user(ADMINS))
    async def broadcast(_, message):
        await message.reply("📢 Broadcast feature ready")
