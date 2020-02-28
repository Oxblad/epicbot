import telebot
import random
from telebot import types
import os

token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(token)

fout = open('message.txt', 'rt', encoding='utf-8')
lines = fout.readlines()
fout.close()

text = []
for line in lines:
    text.append(line)


@bot.message_handler(commands=['start'])
def welcome(message):
    if message.chat.type == 'private':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item = types.InlineKeyboardButton("Поддержать", url='https://qiwi.me/viannedi')

        markup.add(item)
        bot.send_message(message.chat.id,
                         "Добро пожаловать, это бот <b>Эпично❤️</b>, бот создан для интеликтуалов для "
                         "поднятия актива в чате😂 \n - Добавь меня в группу \n - Дать доступ к сообщению боту \n - "
                         "Насаждайтесь!", parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def elsetext(message):
    if not message.chat.type == "private":
        rand = random.randint(0, 100)
        if rand <= 5:
            bot.reply_to(message, random.choice(text))
        else:
            pass


bot.polling(none_stop=True)
