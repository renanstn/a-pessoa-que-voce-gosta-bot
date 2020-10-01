import re
import random
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from model import Suitor
from settings import (BOT_TOKEN, DATABASE_URL, MAX_MESSAGES,
    HM_CHANCES, HEROKU_URL, PORT)


updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher
Suitor.create_table()


def start(update, context):
    message = "Bem vindo(a) ao bot que simula uma conversa com a \
        pessoa que você gosta. Esperamos que tenha uma experiência \
        imersiva e o mais próximo possível da realidade."
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message
    )


def handle_message(update, context):
    chat_id = update.effective_chat.id
    message = update.message.text.lower()
    # Registra ou carrega o(a) pretendente que ta mandando mensagem
    suitor, created = Suitor.get_or_create(chat_id=chat_id)

    # Atualiza o número de mensagens que esse(a) pretendente já enviou
    if not created:
        query = Suitor.update(messages=Suitor.messages+1).where(Suitor.chat_id==chat_id)
        query.execute()

    # Verifica se a pessoa já não ta enchendo o saco
    if suitor.messages > MAX_MESSAGES:
        context.bot.send_message(chat_id=chat_id, text="Você foi bloqueado.")
    # Verifica se a pessoa disse 'oi', e responde, pq eu não sou mal educado
    # Mas responde 1 vez só, pq eu tbm não sou trouxa.
    elif re.search(r'oi', message) and not suitor.said_hi:
        context.bot.send_message(chat_id=chat_id, text="oi")
        suitor.said_hi=True
        suitor.save()
    # Talvez respondo algo, mas só pra pessoa parar de encher o saco.
    else:
        if random.random() < HM_CHANCES:
            context.bot.send_message(chat_id=chat_id, text="hm")


start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, handle_message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

# updater.start_polling()
updater.start_webhook(
    listen='0.0.0.0',
    port=PORT,
    url_path=BOT_TOKEN
)
updater.bot.set_webhook(HEROKU_URL + BOT_TOKEN)
print("Mozão ta on!")
