
import requests
import fake_useragent
from bs4 import BeautifulSoup
import time



import aiogram
import aiogram.filters
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


import app.keyboards as keyboard


class dataTO(StatesGroup):
    userFromYear = State()
    userPriceFrom = State()
    userPages = State()


router = aiogram.Router()

@router.message(aiogram.filters.CommandStart())
async def start(message: aiogram.types.Message, state: FSMContext):
    await state.set_state(dataTO.userFromYear)
    await message.answer(f'Привет {message.from_user.full_name}. Введи с какого года рассматривать машины')



@router.message(dataTO.userFromYear)
async def recFromYear(message: aiogram.types.Message, state: FSMContext):
    await state.update_data(userFromYear=message.text)
    await state.set_state(dataTO.userPriceFrom)
    await message.answer("Отлично. Теперь введи стоимость с которой стоит рассматривать предложения")


@router.message(dataTO.userPriceFrom)
async def recPriceFrom(message: aiogram.types.Message, state: FSMContext):
    await state.update_data(userPriceFrom=message.text)
    await state.set_state(dataTO.userPages)
    await message.answer("Отлично. Сколько страниц объявлений тебе вывести")


@router.message(dataTO.userPages)
async def PrintCars(message: aiogram.types.Message, state: FSMContext):
    await state.update_data(userPages=message.text)
    data = await state.get_data()
    user = fake_useragent.UserAgent().random

    header = {'user-agent': user}

    # pages = 2
    # yearFrom = "2010"
    # priceFrom = "2000000"


    for page in range(1, int(data["userPages"])+1):

        link = "https://kolesa.kz/cars/astana/?year[from]="+ data["userFromYear"] + "&price[from]=" + data["userPriceFrom"] + "&page" + data["userPages"]

        time.sleep(1)
        # responce = requests.get(link, headers=header)
        responce = requests.get(link)


        

        soup = BeautifulSoup(responce.text, 'lxml')
        blockCars = soup.find_all('div', class_='a-list__item')


        for car in blockCars:
            
            carstitle = car.find('h5', class_='a-card__title')
            if carstitle:
                title = carstitle.text.strip()
            else:
                title = "Название нету"
                continue

            carsprice = car.find('span', class_='a-card__price')
            if carsprice:
                price = carsprice.text.strip()
            else:
                price = "Цены нету"


            
            carsdescription = car.find('p', class_='a-card__description')
            if carsdescription:
                description = carsdescription.text.strip()
            else:
                description = "Описание нет"


            carlink = car.find('a', class_='a-card__link')
            if carlink:
                link = "https://kolesa.kz" + carlink['href']
            else:
                link = "Ссылки нету"
            
            year = "Года нету"


            for word in description.split():
                if word.isdigit() and len(word) == 4:
                    year = word
                    break
            

            
            await message.answer("Машина: " + title + "\n" + "Цена: " + price + "\n" + year + "года" + "\n" + "Подробная информация: " + link, reply_markup=keyboard.main)


            # print(title)
            # print(price)
            # print(year)
            # print(link)
            # print('*' * 70)

            # time.sleep(1)
    await state.clear()



    


