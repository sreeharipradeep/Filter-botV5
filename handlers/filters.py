from pyrogram import filters
from database.filters_db import save_filter, get_filter

def register(app):

    # /filter or /f (reply based)
    @app.on_message(
        (filters.command("filter") | filters.command("f"))
        & filters.reply
        & filters.group
    )
    async def add_filter(_, message):

        if len(message.command) < 2:
            return await message.reply(
                "❌ Usage:\nReply to a message and use\n`/filter keyword`",
                quote=True
            )

        keyword = message.command[1].lower().strip()
        reply = message.reply_to_message

        data = {
            "text": reply.text or reply.caption or "",
            "photo": reply.photo.file_id if reply.photo else None,
            "buttons": reply.reply_markup
        }

        await save_filter(message.chat.id, keyword, data)
        await message.reply(f"✅ Saved **{keyword}**")

    # Trigger filter (exact match only)
    @app.on_message(
        filters.group
        & filters.text
        & ~filters.command
        & ~filters.service
    )
    async def trigger_filter(_, message):

        keyword = message.text.lower().strip()
        result = await get_filter(message.chat.id, keyword)

        if not result:
            return

        f = result["data"]

        if f["photo"]:
            await message.reply_photo(
                f["photo"],
                caption=f["text"],
                reply_markup=f["buttons"]
            )
        else:
            await message.reply_text(
                f["text"],
                reply_markup=f["buttons"]
            )
