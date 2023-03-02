from header import *
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) #Подгружаем env

bot: Bot = Bot(token=os.getenv('TOKEN')) #ТОКЕН БОТА (берем из env)
dp = Dispatcher(bot) #Объект диспетчер-бот

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text='Справочная информация')) #Добавляет кнопку "Справочная информация"

@dp.message_handler(text='Справочная информация') #хэндлер для кнопки Справочная информация, отправляет соообщением данные переменной text
async def info(message: types.Message):
    text = 'Данный бот предназначен...'
    await message.answer(text)

@dp.message_handler(commands=['start']) #Тоже самое ^ для команды /start
async def start(message: types.Message):
    await bot.send_message(message.from_user.id,'Данный бот предназначен...',reply_markup=start_keyboard) #Так же здесь для пользователя включается отображение клавиатуры(ну тип кнопок которые мы наделаем)







executor.start_polling(dp, skip_updates=True) #Стартуем бота
