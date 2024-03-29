from pyrogram import Client
import config
import asyncio
from main import bot
# https://t.me/slivmenss
client = Client("@slivmenss", config.API_ID, config.API_HASH)
client.start()
# https://t.me/slivmenss
async def get_chats():
    list = []
    async for dialog in client.iter_dialogs():
        if dialog.chat.type == 'supergroup':
            list.append({'title' : dialog.chat.first_name or dialog.chat.title, 'id' : dialog.chat.id})
    return list
# https://t.me/slivmenss
async def leave_from_channel(id):
    try:
        await client.leave_chat(id)
        return True
    except:
        return False
# https://t.me/slivmenss
async def spamming(spam_list, settings, db):
    while settings[4] == 1:
        for chat in spam_list:
            settings = db.settings()
            try:
                with open(f'{config.DIR}{settings[1]}', 'rb') as photo:
                    await client.send_photo(chat['id'], photo, caption=f"{settings[2]}\n\n{chat['text']}")
                    await bot.send_message(config.ADMIN, f'[LOG] Cообщение в {chat["title"]} было успешно отправленно.')
            except Exception as e:
                try:
                    await client.send_message(chat['id'], f"{settings[2]}\n\n{chat['text']}")
                    await bot.send_message(config.ADMIN, f'[LOG] Cообщение в {chat["title"]} было успешно отправленно.')
                except Exception as e:
                    await bot.send_message(config.ADMIN, f'[LOG] Cообщение в {chat["title"]} не было отправлено из-за ошибки: {e}')
            await asyncio.sleep(settings[5]*60)
            if settings[4] != 1:
                break
