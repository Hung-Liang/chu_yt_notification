from lib.handler.discord_handler import DiscordHandler
from lib.handler.telegram_handler import TelegramHandler
from lib.utils.logger import log
from lib.utils.tools import (
    get_id_list,
    get_live_title_and_url,
    get_message,
    get_upload_id,
)


def send_notify(channel_id, group="group_1"):
    id_list = get_id_list(group)

    upload_id = get_upload_id(channel_id)
    title, url, channel_title = get_live_title_and_url(upload_id)

    if title:
        telegram_message, discord_message = get_message(
            title, url, channel_title, group
        )

        log("[main]", "Telegram Message: ", telegram_message)
        log("[main]", "Discord Message: ", discord_message)

        for cid in id_list:
            TelegramHandler().send_message(cid, telegram_message)

        # TelegramHandler().send_message(telegram_channel_id, telegram_message)
        if group == "group_1":
            DiscordHandler().send_message(discord_message)
