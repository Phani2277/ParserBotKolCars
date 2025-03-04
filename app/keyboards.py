from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/start')]
], resize_keyboard=True)

carBody = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='седан'), KeyboardButton(text='универсал'), KeyboardButton(text='хэтчбек'), KeyboardButton(text='лимузин')], 
    [KeyboardButton(text='купе'), KeyboardButton(text='родстер'), KeyboardButton(text='кабриолет'), KeyboardButton(text='внедорожник')],
    [KeyboardButton(text='кроссовер'), KeyboardButton(text='микровэн'), KeyboardButton(text='минивэн'), KeyboardButton(text='микроавтобус')],
    [KeyboardButton(text='фургон'), KeyboardButton(text='пикап'), KeyboardButton(text='тарга'), KeyboardButton(text='фастбек')],
    [KeyboardButton(text='лифтбек'), KeyboardButton(text='хардтоп'), KeyboardButton(text='Ничего')]
], resize_keyboard=True)


carKDDKeyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='механика'), KeyboardButton(text='АКПП'), KeyboardButton(text='Автомат')], 
    [KeyboardButton(text='Типтроник'), KeyboardButton(text='Вариатор'), KeyboardButton(text='Робот')],
    [KeyboardButton(text='Ничего')]
], resize_keyboard=True)


carnullexp = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='0')]
], resize_keyboard=True)

