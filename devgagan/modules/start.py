from pyrogram import filters
from devgagan import app
from devgagan.core import script
from devgagan.core.func import subscribe
from config import OWNER_ID
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# ------------------- Start-Buttons ------------------- #

buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Update", url="https://t.me/outlawbots"),
        InlineKeyboardButton("Support", url="https://t.me/offchats")],
        [ InlineKeyboardButton("Buy Premium", url= "t.me/CallAdminsRobot"),
         InlineKeyboardButton("Help", url="https://graph.org/How-To-Use-12-04")]
    ]
)

@app.on_message(filters.command("start"))
async def start(_, message):
    join = await subscribe(_, message)
    if join == 1:
        return
    await message.reply_photo(photo="https://graph.org/file/d6682e6f820d882c38efd.jpg",
                              caption=script.START_TXT.format(message.from_user.mention), 
                              reply_markup=buttons)
