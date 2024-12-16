import random

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
    bot.register_next_step_handler(m, reg, kb)


def hr_shar(m: Message):
    kb = RKM(True, True)
    kb.add("Назад")
    bot.send_animation(m.chat.id,
                       "https://i.pinimg.com/originals/01/91/e4/0191e49fc1d6cd26f4425f141a672a80.gif",
                       caption="Гадалка Серафима рекомендует (и Ванга тоже (конец света скоро))", reply_markup=kb)
    bot.register_next_step_handler(m, reg_back)


def book(m: Message):
    kb = RKM(True, True)
    kb.add("Назад")
    bot.send_animation(m.chat.id,
                       "https://www.neizvestniy-geniy.ru/images/works/photo/2019/01/1991525_1.gif",
                       caption="Можно просто почитать, для общего развития, писал сам Олег Шепс", reply_markup=kb)
    bot.register_next_step_handler(m, reg_back)


def runes(m: Message):
    kb = RKM(True, True)
    kb.add("Назад")
    bot.send_photo(m.chat.id,
                       "https://avatars.mds.yandex.net/get-shedevrum/12367607/543440b0b7bc11eead925e32ab44ab44/orig",
                       caption="Могут сделать все что угодно (ну, может почти, не знаем, хотя... Нет наверное, но "
                               "можете купить, прикольная безделушка)", reply_markup=kb)
    bot.register_next_step_handler(m, reg_back)



def mag_shar(m: Message):
    answs = ["Да", "Вероятно", "Не знаю", "Скорее нет, чем да", "Нет"]
    bot.reply_to(m, answs[random.randint(0, 4)])
    reg_back(m)


def reg(m: Message, kb: RKM):
    if m.text == "Хрустальный шар":
        hr_shar(m)
        return
    elif m.text == 'Книга "Гадаем на кофейной гуще"':
        book(m)
        return
    elif m.text == "Магический шар":
        kb = RKM(True, True)
        kb.add("Узнать ответ")
        bot.send_message(m.chat.id,
                         "Задайте свой вопрос (вопрос должен подразумевать ответы да/нет), как будете готовы "
                         "- нажмите на кнопку",
                         reply_markup=kb)
        bot.register_next_step_handler(m, mag_shar)
        return
    elif m.text == "Руны":
        runes(m)
        return
    else:
        bot.send_message(m.chat.id, "Такого товара нет, пожалуйста выберите товар, нажав на кнопку снизу",
                         reply_markup=kb)
        bot.register_next_step_handler(m, reg, kb)


def reg_back(m: Message):
    kb = RKM(True, True)
    kb.row("Хрустальный шар", 'Книга "Гадаем на кофейной гуще"')
    kb.row("Магический шар", "Руны")
    bot.send_message(m.chat.id, 'Выберите следующий товар',
                     reply_markup=kb)
    bot.register_next_step_handler(m, reg, kb)


bot.infinity_polling()
