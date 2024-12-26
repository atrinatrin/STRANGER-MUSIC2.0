from pyrogram import filters
from pyrogram.types import Message

from SHUKLAMUSIC import app
from SHUKLAMUSIC.core.call import SHUKLA
from SHUKLAMUSIC.utils.database import set_loop
from SHUKLAMUSIC.utils.decorators import AdminRightsCheck
from SHUKLAMUSIC.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(
        [
            "end", "stop", "cend", "cstop",  # دستورات انگلیسی
            "پایان", "توقف", "اتمام", "خروج",  # دستورات فارسی
            "استوپ", "وایسا", "بس", "تمام"  # دستورات فارسی عامیانه
        ],
        prefixes=["/"]  # پیشوند / برای تمام دستورات
    ) 
    & filters.group  # فقط در گروه‌ها
    & ~BANNED_USERS  # به جز کاربران مسدود شده
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    
    try:
        await SHUKLA.stop_stream(chat_id)
        await set_loop(chat_id, 0)
        await message.reply_text(
            _["admin_5"].format(message.from_user.mention),
            reply_markup=close_markup(_)
        )
    except Exception as e:
        await message.reply_text(
            f"❌ خطا در توقف پخش:\n\n{str(e)}",
            reply_markup=close_markup(_)
        )

# اضافه کردن پیام‌های خطا به فایل زبان
# در فایل strings/langs/fa.yml
"""
admin_5: "🎵 پخش موسیقی توسط {0} متوقف شد."
"""
