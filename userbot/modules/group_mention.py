<<<<<<< HEAD
=======
# credits: mrconfused
# imported by AshSTR

>>>>>>> aa6c8c6c4f3f7bf54a31feb0ff4696a83a5f7fb0
import asyncio
from userbot.events import register
from userbot import PM_LOGGR_BOT_API_ID

@register(outgoing=True, incoming=True, func=lambda e: e.mentioned)
async def log_tagged_messages(event):
    hmm = await event.get_chat()
        
    if PM_LOGGR_BOT_API_ID:
        sender = await event.get_sender()
        await asyncio.sleep(5)
<<<<<<< HEAD
        if not event.is_private:
=======
        if not event.is_private and not (await event.get_sender()).bot:
>>>>>>> aa6c8c6c4f3f7bf54a31feb0ff4696a83a5f7fb0
            await event.client.send_message(
                PM_LOGGR_BOT_API_ID,
                f"#TAGS \n<b>Sent by : </b><a href = 'tg://user?id={sender.id}'> {sender.first_name}</a>\
			\n<b>Group : </b><code>{hmm.title}</code>\
                        \n<b>Message : </b><a href = 'https://t.me/c/{hmm.id}/{event.message.id}'> link</a>",
                parse_mode="html",
                link_preview=True,
            )
<<<<<<< HEAD
        else:
            await event.client.send_message(
                PM_LOGGR_BOT_API_ID,
                f"#TAGS \n<b>Sent by : </b><a href = 'tg://user?id={sender.id}'> {sender.first_name}</a>\
                        \n<b>ID : </b><code>{sender.id}</code>",
                parse_mode="html",
                link_preview=True,
            )
        e = await event.client.get_entity(int(PM_LOGGR_BOT_API_ID))
        fwd_message = await event.client.forward_messages(
=======
            e = await event.client.get_entity(int(PM_LOGGR_BOT_API_ID))
            fwd_message = await event.client.forward_messages(
>>>>>>> aa6c8c6c4f3f7bf54a31feb0ff4696a83a5f7fb0
                    e,
                    event.message,
                    silent=True
                )
<<<<<<< HEAD
=======
        else:
            if event.is_private:
                if not (await event.get_chat()).bot:
                    await event.client.send_message(
                        PM_LOGGR_BOT_API_ID,
                        f"#TAGS \n<b>Sent by : </b><a href = 'tg://user?id={sender.id}'> {sender.first_name}</a>\
                                \n<b>ID : </b><code>{sender.id}</code>",
                        parse_mode="html",
                        link_preview=True,
                    )
                    e = await event.client.get_entity(int(PM_LOGGR_BOT_API_ID))
                    fwd_message = await event.client.forward_messages(
                            e,
                            event.message,
                            silent=True
                        )
>>>>>>> aa6c8c6c4f3f7bf54a31feb0ff4696a83a5f7fb0
