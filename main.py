import telebot
import schedule
import time

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'ID чата: {message.chat.id}')


@bot.message_handler(commands=['amir'])
def amir_command(message):
    bot.send_message(message.chat.id, 'Амир пидор')


# если работают команды не работает расписание, разкомментировать чтобы узнать id чата, потом обратно закомментировать
# bot.polling(none_stop=True)


def note(chat_id):
    try:
        bot.send_message(chat_id, 'Стенд')
        print(f"Message sent to chat_id: {chat_id} at {time.strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"Error sending message: {e}")


def prepare(chat_id):
    try:
        bot.send_message(chat_id, 'Коллеги, стенд через 5 минут')
        print(f"Message sent to chat_id: {chat_id} at {time.strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"Error sending message: {e}")


def meet(chat_id):
    try:
        bot.send_message(chat_id, 'Пожалуйста, зайдите на встречу')
        print(f"Message sent to chat_id: {chat_id} at {time.strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"Error sending message: {e}")


def meetPrepare(chat_id):
    try:
        bot.send_message(chat_id, 'Уважаемые коллеги, напоминаю, что встреча через 5 минут')
        print(f"Message sent to chat_id: {chat_id} at {time.strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"Error sending message: {e}")


# 5 минут карлсберг
schedule.every().monday.at("13:55:00").do(prepare, chat_id=-4017815885)
schedule.every().tuesday.at("13:55:00").do(prepare, chat_id=-4017815885)
schedule.every().wednesday.at("13:55:00").do(prepare, chat_id=-4017815885)
schedule.every().thursday.at("13:55:00").do(prepare, chat_id=-4017815885)
schedule.every().friday.at("13:55:00").do(prepare, chat_id=-4017815885)

# стенд карлсберг
schedule.every().monday.at("14:00:00").do(note, chat_id=-4017815885)
schedule.every().tuesday.at("14:00:00").do(note, chat_id=-4017815885)
schedule.every().wednesday.at("14:00:00").do(note, chat_id=-4017815885)
schedule.every().thursday.at("14:00:00").do(note, chat_id=-4017815885)
schedule.every().friday.at("14:00:00").do(note, chat_id=-4017815885)

# 5 минут магнум
schedule.every().monday.at("09:55:00").do(prepare, chat_id=-1001740636729)
schedule.every().tuesday.at("09:55:00").do(prepare, chat_id=-1001740636729)
schedule.every().wednesday.at("09:55:00").do(prepare, chat_id=-1001740636729)
schedule.every().thursday.at("09:55:00").do(prepare, chat_id=-1001740636729)
schedule.every().friday.at("09:55:00").do(prepare, chat_id=-1001740636729)

# стенд магнум
schedule.every().monday.at("10:00:00").do(note, chat_id=-1001740636729)
schedule.every().tuesday.at("10:00:00").do(note, chat_id=-1001740636729)
schedule.every().wednesday.at("10:00:00").do(note, chat_id=-1001740636729)
schedule.every().thursday.at("10:00:00").do(note, chat_id=-1001740636729)
schedule.every().friday.at("10:00:00").do(note, chat_id=-1001740636729)

# 5 мин развитие магнум
schedule.every().monday.at("14:55:00").do(prepare, chat_id=-4069232645)
schedule.every().tuesday.at("14:55:00").do(prepare, chat_id=-4069232645)
schedule.every().wednesday.at("14:55:00").do(prepare, chat_id=-4069232645)
schedule.every().thursday.at("14:55:00").do(prepare, chat_id=-4069232645)
schedule.every().friday.at("14:55:00").do(prepare, chat_id=-4069232645)

# стенд мин развитие магнум
schedule.every().monday.at("15:00:00").do(note, chat_id=-4069232645)
schedule.every().tuesday.at("15:00:00").do(note, chat_id=-4069232645)
schedule.every().wednesday.at("15:00:00").do(note, chat_id=-4069232645)
schedule.every().thursday.at("15:00:00").do(note, chat_id=-4069232645)
schedule.every().friday.at("15:00:00").do(note, chat_id=-4069232645)

# Carlsberg Prime Source 5 min
schedule.every().wednesday.at("15:55:00").do(meet, chat_id=-4056085513)
schedule.every().wednesday.at("16:00:00").do(meetPrepare, chat_id=-4056085513)

# Основной цикл программы
while True:
    schedule.run_pending()
    time.sleep(1)

# ясли -1001984858941
# карлсберг -4017815885
# magnum -1001740636729
# развитие магнум -4069232645
# Carlsberg Prime Source -4056085513
