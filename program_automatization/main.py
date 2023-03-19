import time
import pyautogui
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Объявляем функцию-обработчик для команды /start
def start(update, context):
    # Выполняем код при получении команды /start
    discord_location = pyautogui.locateCenterOnScreen(r'program_automatization\discord.png')
    pyautogui.click(discord_location)
    time.sleep(2)
    eliseev_location = pyautogui.locateCenterOnScreen(r'program_automatization\eliseev.png')
    pyautogui.click(eliseev_location)
    time.sleep(3)
    message_location = pyautogui.locateCenterOnScreen(r'program_automatization\message_pole.png')
    pyautogui.click(message_location)
    message_text = update.message.text.split(' ', 1)[1]  # Получаем текст после команды /start
    print(f"Текст сообщения: {message_text}")
    pyautogui.typewrite(message_text)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)
    friends_location = pyautogui.locateCenterOnScreen(r'program_automatization\friends.png')
    pyautogui.click(friends_location)
    time.sleep(0.1)
    pyautogui.click(discord_location)

# Объявляем функцию-обработчик для сообщений
def handle_message(update, context):
    # Получаем текст сообщения
    message_text = update.message.text

    # Выполняем код для обработки сообщения
    ...

# Получаем токен бота из файла или переменной окружения
TOKEN = '6066582398:AAEYnE7Xty-YmhGk5xVpTf0t8nXepLeMWB4'

# Создаем объекты для работы с Telegram API
bot = telegram.Bot(token=TOKEN)
updater = Updater(TOKEN, use_context=True)

# Объявляем обработчики команд и сообщений
start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, handle_message)

# Регистрируем обработчики в updater
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(message_handler)

# Запускаем бота
updater.start_polling()
updater.idle()
