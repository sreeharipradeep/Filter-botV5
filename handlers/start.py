from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import START_PICS, CHANNEL, GROUP, COMMUNITY, BOT_USERNAME

START_TEXT = """🍿 Welcome! 🍿

I am the filter bot of the Trixel Movie group 🎬.
You can add me to your channel or group and use me.

🍿 സ്വാഗതം! 🍿

ഞാൻ Trixel Movie 🎬 ഗ്രൂപ്പിന്റെ ഫിൽട്ടർ ബോട്ട് ആണ്.
നിങ്ങൾ എന്നെ നിങ്ങളുടെ Channel / Group-ൽ add ചെയ്ത്
use ചെയ്യാവുന്നതാണ് ☺️
"""

def register(app):

    @app.on_message(filters.private & filters.command("start"))
    async def start(_, message):

        buttons = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("📢 Channel", url=CHANNEL)],
                [InlineKeyboardButton("👥 Group", url=GROUP)],
                [InlineKeyboardButton("🌐 Community", url=COMMUNITY)],
                [InlineKeyboardButton(
                    "➕ Add Me To Your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                )]
            ]
        )

        await message.reply_media_group(
            [
                {"type": "photo", "media": START_PICS[0], "caption": START_TEXT},
                {"type": "photo", "media": START_PICS[1]}
            ]
        )

        await message.reply_text(
            "👇 Use the buttons below",
            reply_markup=buttons
        )
