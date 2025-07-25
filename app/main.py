from telethon.sync import TelegramClient, events
from discord_hooks import Webhook

import requests
import os
import json
import logging

logger = logging.getLogger(__name__)


def main(config: dict):
    try:
        url = config['discord']['url']
        api_id = config['telegram']['api_id']
        api_hash = config['telegram']['api_hash']
        channel_name = config['telegram']['channel_name']
    except:
        raise Exception('Error processing config file')

    with TelegramClient('FSR_Discord', api_id, api_hash).start() as client:
        @client.on(events.NewMessage(chats=channel_name))
        async def handler(event):
            logger.info(f"New message from {event.message.sender_id}")
            if hasattr(event.message.media, "photo"):
                download_res = await client.download_media(event.message.media, './image')
                files = {'file': (open(download_res, 'rb'))}
                requests.post(url, files=files)
                os.remove(download_res)
            if not event.message.message == "":
                Webhook(url, msg=event.message.text).post()

        client.run_until_disconnected()


if __name__ == "__main__":
    import logging.config

    logging.config.fileConfig('logger.conf')
    with open('../config.json') as config_file:
        config = json.load(config_file)

    logger.info("Starting Bridge")
    main(config)
