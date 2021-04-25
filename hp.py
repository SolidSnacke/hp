from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from telegram.ext import CommandHandler
import random

TOKEN = ''
faul = 0
count = 0


def help(update, context):
    update.message.reply_text('''/start - начало опроса.
/stop - остановка опроса.
Ответы можно записать цифрой или же текстом.
В конце ороса произойдет оценка ваших знаний.
    ''')
    return faul


# просто пасхалочка не обращайте внимение.
def easter_egg(update, context):
    global faul
    global count
    faul = 0
    count = 0
    f = random.randint(0, 1)
    if f == 1:
        video = open('data/BRUH.mp4', 'rb')
    if f == 0:
        video = open('data/Monkey.mp4', 'rb')
    update.message.reply_text("О вот и пасхалочка.")
    context.bot.send_video(update.message.chat.id, video)
    return ConversationHandler.END


def get_stop(update, context):
    global faul
    global count
    faul = 0
    count = 0
    update.message.reply_text("Жаль. Тогда прощайте увидимся позже(возможно)")
    return ConversationHandler.END


def start(update, context):
    global faul
    global count
    faul = 0
    count = 0
    update.message.reply_text("""Приветствую!
Вы попали на небольшой опрос-тест.
Буду рад если вы пройлете его до конца.
Если же вы хотите остановить вопрос напишите /stop.""")

    update.message.reply_text("""И так первый вопрос:
Какой актер сыграл роль Ипполита в фильме 
«Ирония судьбы, или С лёгким паром»?
    
1.Андрей Мягков
2.Юрий Яковлев
3.Олег Басилашвили""")
    photo = open('data/first.png', 'rb')
    context.bot.send_photo(update.message.chat.id, photo)
    faul += 1
    return faul


def film_c_first(update, context):
    global faul
    global count
    first = update.message.text
    update.message.reply_text(
        """Второй вопрос:
Какой киноактер произнес фразу: 
«Красиво плывет эта группа в полосатых купальниках!»?
        
1.Алексей Смирнов
2.Василий Лановой
3.Иван Дмитриев""")
    photo = open('data/two.jpeg', 'rb')
    context.bot.send_photo(update.message.chat.id, photo)
    faul += 1
    if first == "2" or first == 'Юрий Яковлев':
        count += 1
    return faul


def film_c_two(update, context):
    global faul
    global count
    two = update.message.text
    update.message.reply_text(
        """Третий вопрос:
В каком фильме впервые прозвучала песня 
«Позвони мне, позвони... »?

1.'Карнавал'
2.'Эта весёлая планета'
3.'Самая обаятельная и привлекательная'""")
    photo = open('data/three.png', 'rb')
    context.bot.send_photo(update.message.chat.id, photo)
    faul += 1
    if two == "2" or two == 'Василий Лановой':
        count += 1
    return faul


def film_c_three(update, context):
    global faul
    global count
    three = update.message.text
    update.message.reply_text(
        """Четвертый вопрос:
Как звали радистку в сериале 
«Семнадцать мгновений весны»?

1.Кэт
2.Жаклин
3.Мэрилин""")
    photo = open('data/four.png', 'rb')
    context.bot.send_photo(update.message.chat.id, photo)
    faul += 1
    if three == "1" or three in 'Карнавал':
        count += 1
    return faul


def film_c_four(update, context):
    global faul
    global count
    four = update.message.text
    update.message.reply_text(
        """Пятый вопрос:
Какое имя не носила ни одна из подруг в фильме 
«Москва слезам не верит»?

1.Надежда
2.Антонина
3.Екатерина""")
    photo = open('data/five.png', 'rb')
    context.bot.send_photo(update.message.chat.id, photo)
    faul += 1
    if four == "1" or four == 'Кэт':
        count += 1
    return faul


def film_c_five(update, context):
    global faul
    global count
    five = update.message.text
    update.message.reply_text(
        """Шестой вопрос:
Какую профессию получает героиня Любови Орловой в фильме 
"Светлый путь"?

1.Певица
2.Ткачиха
3.Учительница""")
    photo = open('data/six.png', 'rb')
    context.bot.send_photo(update.message.chat.id, photo)
    faul += 1
    if five == "1" or five == 'Надежда':
        count += 1
    return faul


def film_c_six(update, context):
    global faul
    global count
    six = update.message.text
    update.message.reply_text(
        """Седьмой вопрос:
По какой причине опоздал из увольнения суворовец Трофимов в фильме 
"Офицеры"?

1.Бегемота смотрел в зоопарке
2.Качался на качелях
3.Проспал""")
    photo = open('data/seven.png', 'rb')
    context.bot.send_photo(update.message.chat.id, photo)
    faul += 1
    if six == "2" or six == 'Ткачиха':
        count += 1
    return faul


def film_c_seven(update, context):
    global faul
    global count
    seven = update.message.text
    update.message.reply_text(
        """Восьмой вопрос:
Какую фамилию носил один из персонажей фильма 
«Свадьба в Малиновке»?

1.Дума
2.Вече
3.Рада""")
    photo = open('data/eight.png', 'rb')
    context.bot.send_photo(update.message.chat.id, photo)
    faul += 1
    if seven == "1" or seven == 'Бегемота смотрел в зоопарке':
        count += 1
    return faul


def film_c_eight(update, context):
    global faul
    global count
    eight = update.message.text
    update.message.reply_text(
        """Девятый вопрос:
Какому герою фильма «Белое солнце пустыни» удалось выжить?

1.Петрухе
2.Сухову
3.Верещагину""")
    photo = open('data/nine.png', 'rb')
    context.bot.send_photo(update.message.chat.id, photo)
    faul += 1
    if eight == "1" or eight == 'Дума':
        count += 1
    return faul


def film_c_nine(update, context):
    global faul
    global count
    nine = update.message.text
    update.message.reply_text(
        """Десятый вопрос:
Как создатели фильма "Джентльмены удачи" обозначили его жанр?

1.Лирическая комедия
2.Нелирическая комедия
3.Криминальная комедия""")
    photo = open('data/ten.png', 'rb')
    context.bot.send_photo(update.message.chat.id, photo)
    faul += 1
    if nine == "2" or nine == 'Сухову':
        count += 1
    return faul


def film_c_ten(update, context):
    global faul
    global count
    ten = update.message.text
    update.message.reply_text(
        """Одиннадцатый вопрос:
Какая фигура украшала капот автомобиля Труса, Балбеса и Бывалого в фильме 
«Кавказская пленница»?

1.Дятел
2.Зубр
3.Олень""")
    photo = open('data/eleven.png', 'rb')
    context.bot.send_photo(update.message.chat.id, photo)
    faul += 1
    if ten == "2" or ten == 'Нелирическая комедия':
        count += 1
    return faul


def end(update, context):
    global faul
    global count
    eleven = update.message.text
    if eleven == "3" or eleven == 'Олень':
        count += 1
    update.message.reply_text(f""" Вы ответили на {count} вопросов из 11.""")
    if count == 0:
        update.message.reply_text('Ноль? Ты вообще ни разу не видел советских фильмов?\n'
                                  'и пересматривай фильмы, не позорься.\n'
                                  '(╯°□°）╯︵ ┻━┻')
    if count == 1:
        update.message.reply_text('Всего 1 правильный ответ, это не дело. А ну ка быстро иди\n'
                                  'и пересматривай фильмы, не позорься.\n'
                                  '(╯°□°）╯︵ ┻━┻')
    if count == 1 and count > 5:
        update.message.reply_text('Надо бы подтянуть знания.\n'
                                  'Лучше пересмотри парочку фильмов на досуге, так для интереса.')
    if count > 5 and count < 11:
        update.message.reply_text('Хорошо знаешь советские фильмы, то не идеально конечно.\n')
    if count == 11:
        update.message.reply_text('(　･ω･)☞ Да ты знаток, как я погляжу.\n'
                                  'Вот держи печеньку\n'
                                  '+ 1 печенька в вашем кармане.')
    update.message.reply_text('Спасибо за участие в опросе! Всего доброго!')
    faul = 0
    count = 0
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            1: [CommandHandler("help", help), CommandHandler('stop', get_stop),
                MessageHandler(Filters.text, film_c_first)],
            2: [CommandHandler("help", help), CommandHandler('stop', get_stop),
                MessageHandler(Filters.text, film_c_two)],
            3: [CommandHandler("help", help), CommandHandler('stop', get_stop),
                MessageHandler(Filters.text, film_c_three)],
            4: [CommandHandler("help", help), CommandHandler('stop', get_stop),
                MessageHandler(Filters.text, film_c_four)],
            5: [CommandHandler("help", help), CommandHandler('stop', get_stop),
                MessageHandler(Filters.text, film_c_five)],
            6: [CommandHandler("help", help), CommandHandler('stop', get_stop),
                MessageHandler(Filters.text, film_c_six)],
            7: [CommandHandler("help", help), CommandHandler('stop', get_stop),
                MessageHandler(Filters.text, film_c_seven)],
            8: [CommandHandler("help", help), CommandHandler('stop', get_stop),
                MessageHandler(Filters.text, film_c_eight)],
            9: [CommandHandler("help", help), CommandHandler('stop', get_stop),
                MessageHandler(Filters.text, film_c_nine)],
            10: [CommandHandler("help", help), CommandHandler('stop', get_stop),
                 MessageHandler(Filters.text, film_c_ten)],
            11: [CommandHandler("help", help), CommandHandler('stop', get_stop),
                 CommandHandler('easter_egg', easter_egg),
                 MessageHandler(Filters.text, end)]
        },

        fallbacks=[CommandHandler('stop', get_stop)]
    )
    dp.add_handler(conv_handler)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
# Знаю код выглядит очень странно.
# Пришлось писать формулировки вопросов вот так, т.к. если пиать нормально то первый 
# вопрос отобразится только после введения ответа
