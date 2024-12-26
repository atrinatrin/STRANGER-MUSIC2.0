from typing import Union
from pyrogram.types import InlineKeyboardButton

def setting_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text="کاربران مجاز ⊱", callback_data="AU"),
            InlineKeyboardButton(text="زبان ⊱", callback_data="LG"),
        ],
        [
            InlineKeyboardButton(text="حالت پخش ⊱", callback_data="PM"),
        ],
        [
            InlineKeyboardButton(text="تنظیمات رأی ⊱", callback_data="VM"),
        ],
        [
            InlineKeyboardButton(text="⊝ بستن", callback_data="close"),
        ],
    ]
    return buttons

def vote_mode_markup(_, current, mode: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(text="⊱ حالت رأی گیری", callback_data="VOTEANSWER"),
            InlineKeyboardButton(
                text="✓ فعال" if mode == True else "✗ غیرفعال",
                callback_data="VOMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text="⊖", callback_data="FERRARIUDTI M"),
            InlineKeyboardButton(
                text=f"مقدار فعلی: {current}",
                callback_data="ANSWERVOMODE",
            ),
            InlineKeyboardButton(text="⊕", callback_data="FERRARIUDTI A"),
        ],
        [
            InlineKeyboardButton(
                text="⊲ برگشت",
                callback_data="settings_helper",
            ),
            InlineKeyboardButton(text="⊝ بستن", callback_data="close"),
        ],
    ]
    return buttons

def auth_users_markup(_, status: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(text="⊱ کاربران مجاز", callback_data="AUTHANSWER"),
            InlineKeyboardButton(
                text="✓ فعال" if status == True else "✗ غیرفعال",
                callback_data="AUTH",
            ),
        ],
        [
            InlineKeyboardButton(text="⊱ لیست کاربران مجاز", callback_data="AUTHLIST"),
        ],
        [
            InlineKeyboardButton(
                text="⊲ برگشت",
                callback_data="settings_helper",
            ),
            InlineKeyboardButton(text="⊝ بستن", callback_data="close"),
        ],
    ]
    return buttons

def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(text="⊱ حالت جستجو", callback_data="SEARCHANSWER"),
            InlineKeyboardButton(
                text="✓ مستقیم" if Direct == True else "✗ درون خطی",
                callback_data="MODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text="⊱ حالت گروه", callback_data="AUTHANSWER"),
            InlineKeyboardButton(
                text="✓ فعال" if Group == True else "✗ غیرفعال",
                callback_data="CHANNELMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text="⊱ نوع پخش", callback_data="PLAYTYPEANSWER"),
            InlineKeyboardButton(
                text="✓ فعال" if Playtype == True else "✗ غیرفعال",
                callback_data="PLAYTYPECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⊲ برگشت",
                callback_data="settings_helper",
            ),
            InlineKeyboardButton(text="⊝ بستن", callback_data="close"),
        ],
    ]
    return buttons
