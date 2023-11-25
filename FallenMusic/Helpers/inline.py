from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="• مسح •", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="ll", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
            ],
            [
            InlineKeyboardButton("≪ 𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊 ≫", url=f"https://t.me/source_alpop"),
            InlineKeyboardButton("جروب السورس", url=f"https://t.me/bar_al_pop"),
            InlineKeyboardButton("مطور السورس1", url=f"https://j_s_9"),
            InlineKeyboardButton("مطور السورس2", url=f"https://t.me/vip_alpop"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="‹ اضف البوت في مجموعتك ›",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="• اوامر التشغيل  •", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="• سوࢪس البوب •", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="• جروب الدعم •", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="• مطورين السورس •", url="https://t.me/source_alpop_info"
        ),
        InlineKeyboardButton(text="• مالك البوت •", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="‹ اضف البوت في مجموعتك ›",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="• سوࢪس البوب •", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="• جروب الدعم •", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="• مطورين السورس •", url="https://t.me/source_alpop_info"
        ),
        InlineKeyboardButton(text="• مالك البوت •", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="• اوامࢪ التشغيل •",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="• اوامر المطور •", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="• اوامر المالك •", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="• رجوع •", callback_data="fallen_home"),
        InlineKeyboardButton(text="• مسح •", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="• جروب الدعم •", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="• رجوع •", callback_data="fallen_help"),
        InlineKeyboardButton(text="• مسح •", callback_data="close"),
    ],
]
