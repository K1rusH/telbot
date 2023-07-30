import telebot
from telebot import types

bot = telebot.TeleBot('ваш токен')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привет")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я тестовый бот, рад знакомству", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Привет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Пост об увлечении')
        btn2 = types.KeyboardButton('Селфи')
        btn3 = types.KeyboardButton('Фото')
        btn4 = types.KeyboardButton('Прислать войсы')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) 


    elif message.text == 'Пост об увлечении':
        bot.send_message(message.from_user.id, '''Я довольно разносторонний человек и увлечений много, тяжело выделить что-то одно главное.
                                                Можно сказать это программирование, так как в силу своей профессии провожу за кодом достаточно много времени.
                                                Больших достижений и проектов не имею, в большей степени помогаю ребятам исправлять ошибки, объяснять что-то ну и так же вместе с ними учиться.
                                                Я постоянно нахожусь в процессе самообучения, не важно какое это направление''', parse_mode='Markdown')
    elif message.text == 'Селфи':
        bot.send_photo(message.from_user.id, photo=open('images/sel.jpg', 'rb'))
    elif message.text == 'Фото':
        bot.send_photo(message.from_user.id, 'https://sun9-15.userapi.com/c4124/u25310159/73566482/x_41387735.jpg')
    elif message.text == 'Прислать войсы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('о ChatGPT')
        btn2 = types.KeyboardButton('Базы данных')
        btn3 = types.KeyboardButton('Первая любовь')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Какой войс интересует ?', reply_markup=markup)
    if message.text == 'о ChatGPT':
        bot.send_audio(message.from_user.id, audio=open('voice/msg856303179-27292.ogg', 'rb'))
    elif message.text == 'Базы данных':
        bot.send_audio(message.from_user.id, audio=open('voice/msg856303179-27294.ogg', 'rb'))
    elif message.text == 'Первая любовь':
        bot.send_audio(message.from_user.id, audio=open('voice/msg856303179-27298.ogg', 'rb'))    

bot.polling(none_stop=True, interval=0)

