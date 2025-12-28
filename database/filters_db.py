from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client.rose_filter_bot
col = db.filters

async def save_filter(chat_id, keyword, data):
    await col.update_one(
        {"chat_id": chat_id, "keyword": keyword},
        {"$set": {"data": data}},
        upsert=True
    )

async def get_filter(chat_id, keyword):
    return await col.find_one(
        {"chat_id": chat_id, "keyword": keyword}
    )
