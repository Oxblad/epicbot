import telebot
import random
from telebot import types
import os

token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(token)
fout = open('message.txt', 'rt', encoding='utf-8')
chat_ids_file = 'chat_id'

lines = fout.readlines()
fout.close()
text = []
for line in lines:
    text.append(line)


def save_chat_id(chat_id):
    # Function add id if no id
    chat_id = str(chat_id)
    with open(chat_ids_file, "a+") as ids_file:
        ids_file.seek(0)

        ids_list = [line.split('\n')[0] for line in ids_file]

        if chat_id not in ids_list:
            ids_file.write(f'{chat_id}\n')
            ids_list.append(chat_id)
        else:
            pass
    return


@bot.message_handler(commands=['start'])
def welcome(message):
    if message.chat.type == 'private':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('Поддержать')
        item1 = types.KeyboardButton('Мои функции💜')
        markup.add(item, item1)
        bot.send_message(message.chat.id,
                         "Добро пожаловать, это бот <b>Эпично❤️</b>, бот создан для интеликтуалов для "
                         "поднятия актива в чате😂 \n - Добавь меня в группу \n - Дать доступ к сообщению боту \n - "
                         "Наслаждайтесь!", parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def else_text(message):
    if not message.chat.type == "private":
        delete_links(message)
        save_chat_id(message.chat.id)
        rand = random.randint(0, 100)
        if rand <= 4:
            bot.reply_to(message, random.choice(text))
        else:
            pass
    else:

        if message.text == 'Мои функции💜':
            bot.send_message(message.chat.id,
                             'Что я умею?❤\n 📞☎ Я могу отвечать на сообщения в группе любым пользователям \n⭐ Я '
                             'администрирую чат от спама и другой фикни :З')
        elif message.text == 'Поддержать':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item = types.InlineKeyboardButton("Поддержать", url='https://qiwi.me/viannedi')

            markup.add(item)
            bot.send_message(message.chat.id,
                             "Спасибо что решили поддержать меня❤", parse_mode='html', reply_markup=markup)


@bot.message_handler(func=lambda message: message.entities is not None and message.chat.id == message.chat.id)
def delete_links(message):
    for entity in message.entities:
        if entity.type in ["url", "text_link"]:
            bot.delete_message(message.chat.id, message.message_id)
        else:
            return


if __name__ == "__main__":
    bot.infinity_polling()
