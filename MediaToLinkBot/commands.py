from pyrogram import Client, __version__, filters
from pyrogram.raw.all import layer
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command('start') & filters.private)
async def start_command(client, message):
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton('Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/mnbots'),
        InlineKeyboardButton('Sᴜᴩᴩᴏʀᴛ', url='https://t.me/mnbots-support')
        ],[
        InlineKeyboardButton('ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url="https://t.me/+klNh8N3hXjM1MDFk")
    ]])
    await message.reply_text("I Am Simple Base Telegram Bot.", reply_markup=button)
