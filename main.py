import telebot
from telebot.types import Message, ReplyKeyboardMarkup as RKM, ReplyKeyboardRemove as RKR
from telebot.types import InlineKeyboardMarkup as IKM, InlineKeyboardButton as IKB, CallbackQuery
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
clear = RKR()


@bot.message_handler(commands=["start"])
def start(m: Message):
    kb = RKM(True, True)
    kb.row("Хрустальный шар", 'Книга "Гадаем на кофейной гуще"')
    kb.row("Магический шар", "Руны")
    bot.send_message(m.chat.id, 'Здравствуйте, магазин эзотерики "Шары из Гусь-Хрустального" приветствует Вас',
                     reply_markup=kb)
    bot.register_next_step_handler(m, reg,kb)


def reg(m:Message, kb:RKM):
    if m.text == "Хрустальный шар":
        hr_shar(m)
        return
    elif m.text == 'Книга "Гадаем на кофейной гуще"':
        book(m)
        return
    elif m.text == "Магический шар":
        mag_shar(m)
        return
    elif m.text == "Руны":
        runes(m)
        return
    else:
        bot.send_message(m.chat.id, "Такого товара нет, пожалуйста выберите товар, нажав на кнопку снизу",
                         reply_markup=kb)
        bot.register_next_step_handler(m, reg,kb)

bot.infinity_polling()