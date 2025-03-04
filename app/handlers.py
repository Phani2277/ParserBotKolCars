
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
    carsBodyClass = State()
    userKDD = State()
    userFromYear = State()
    userToYear = State()
    userPriceFrom = State()
    userPriceTo = State()
    userPages = State()
    


router = aiogram.Router()

@router.message(aiogram.filters.CommandStart())
async def start(message: aiogram.types.Message, state: FSMContext):
    await state.set_state(dataTO.carsBodyClass)
    await message.answer(f'Привет {message.from_user.full_name}. Выбери тип кузова автомобиля', reply_markup=keyboard.carBody)
    

@router.message(dataTO.carsBodyClass)
async def recCarbody(message: aiogram.types.Message, state: FSMContext):
    match message.text:
        case "седан":
            await state.update_data(carsBodyClass="sedan/")
        case "универсал":
            await state.update_data(carsBodyClass="station-wagon/")
        case "хэтчбек":
            await state.update_data(carsBodyClass="hatchback/")
        case "лимузин":
            await state.update_data(carsBodyClass="limousine/")
        case "купе":
            await state.update_data(carsBodyClass="body-coupe/")
        case "родстер":
            await state.update_data(carsBodyClass="body-roadster/")
        case "кабриолет":
            await state.update_data(carsBodyClass="cabriolet/")
        case "внедорожник":
            await state.update_data(carsBodyClass="suv/")
        case "кроссовер":
            await state.update_data(carsBodyClass="crossover-suv/")
        case "микровэн":
            await state.update_data(carsBodyClass="microvan/")
        case "минивэн":
            await state.update_data(carsBodyClass="minivan/")
        case "микроавтобус":
            await state.update_data(carsBodyClass="van/")
        case "фургон":
            await state.update_data(carsBodyClass="wagon/")
        case "пикап":
            await state.update_data(carsBodyClass="body-pickup/")
        case "тарга":
            await state.update_data(carsBodyClass="targa/")
        case "фастбек":
            await state.update_data(carsBodyClass="fastback/")
        case "лифтбек":
            await state.update_data(carsBodyClass="liftback/")
        case "хардтоп":
            await state.update_data(carsBodyClass="hardtop/")
        case "Ничего":
            await state.update_data(carsBodyClass="")

        
    
    await state.set_state(dataTO.userKDD)
    await message.answer("Выбери КПП", reply_markup=keyboard.carKDDKeyboard)


@router.message(dataTO.userKDD)
async def recKDD(message: aiogram.types.Message, state: FSMContext):
    match message.text:
        case "механика":
            await state.update_data(userKDD="1")
        case "АКПП":
            await state.update_data(userKDD="2345")
        case "Автомат":
            await state.update_data(userKDD="2")
        case "Типтроник":
            await state.update_data(userKDD="3")
        case "Вариатор":
            await state.update_data(userKDD="4")
        case "Робот":
            await state.update_data(userKDD="5")
        case "Ничего":
            await state.update_data(userKDD="")
        


    await state.set_state(dataTO.userFromYear)
    await message.answer("Введи с какого года рассматривать машины", reply_markup=keyboard.carnullexp)


@router.message(dataTO.userFromYear)
async def recFromYear(message: aiogram.types.Message, state: FSMContext):
    
    await state.update_data(userFromYear=message.text)
    await state.set_state(dataTO.userToYear)
    await message.answer("Отлично. Теперь введи до какого года стоит рассматривать предложения", reply_markup=keyboard.carnullexp)


@router.message(dataTO.userToYear)
async def recToYear(message: aiogram.types.Message, state: FSMContext):
    
    await state.update_data(userToYear=message.text)
    await state.set_state(dataTO.userPriceFrom)
    await message.answer("Отлично. Теперь введи стоимость с которой стоит рассматривать предложения", reply_markup=keyboard.carnullexp)



@router.message(dataTO.userPriceFrom)
async def recPriceFrom(message: aiogram.types.Message, state: FSMContext):
    await state.update_data(userPriceFrom=message.text)
    await state.set_state(dataTO.userPriceTo)
    await message.answer("Отлично. Теперь введи стоимость до которой стоит рассматривать предложения", reply_markup=keyboard.carnullexp)


@router.message(dataTO.userPriceTo)
async def recPriceTo(message: aiogram.types.Message, state: FSMContext):
    await state.update_data(userPriceTo=message.text)
    await state.set_state(dataTO.userPages)
    await message.answer("Отлично. Сколько страниц объявлений тебе вывести")




@router.message(dataTO.userPages)
async def PrintCars(message: aiogram.types.Message, state: FSMContext):
    await state.update_data(userPages=message.text)
    data = await state.get_data()
    user = fake_useragent.UserAgent().random
    if int(data["userPages"]) <= 0:
        await message.answer("Ошибка: получено некорректное количество страниц", reply_markup=keyboard.main)
    header = {'user-agent': user}

    # pages = 2
    # yearFrom = "2010"
    # priceFrom = "2000000"


    for page in range(1, int(data["userPages"])+1):


        # carsBodyClass = State()
        # userKDD = State()
        # userFromYear = State()
        # userToYear = State()
        # userPriceFrom = State()
        # userPriceTo = State()
        # userPages = State()


        param = [""]
        

        if data["userKDD"] != "":
            param.append("auto-car-transm="+ data["userKDD"])
        if data["userFromYear"] != "":
            param.append("year[from]=" + data["userFromYear"])
        if data["userToYear"] != "":
            param.append("year[to]=" + data["userToYear"])
        if data["userPriceFrom"] != "":
            param.append("price[from]=" + data["userPriceFrom"])
        if data["userPriceTo"] != "":
            param.append("price[to]=" + data["userPriceTo"])

        # param = ["auto-car-transm="+Kpp]

        # if yearFrom != "":
        #     param.append("year[from]=" + yearFrom)
        # if yearTo != "":
        #     param.append("year[to]=" + yearTo)
        # if priceFrom != "":
        #     param.append("price[from]=" + priceFrom)
        # if priceTo != "":
        #     param.append("price[to]=" + priceTo)



        # link = "https://kolesa.kz/cars/astana/?year[from]="+ data["userFromYear"] + "&price[from]=" + data["userPriceFrom"] + "&page=" + data["userPages"]
        link = "https://kolesa.kz/cars/" + data["carsBodyClass"] + "astana/?" + "&".join(param[1:])+"&page=" + str(page)

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
                linkdescription = "https://kolesa.kz" + carlink['href']
            else:
                linkdescription = "Ссылки нету"
            
            year = "Года нету"


            for word in description.split():
                if word.isdigit() and len(word) == 4:
                    year = word
                    break
            

            
            await message.answer("Машина: " + title + "\n" + "Цена: " + price + "\n" + year + "года" + "\n" + "Подробная информация: " + linkdescription, reply_markup=keyboard.main)
            print(link)


            # print(title)
            # print(price)
            # print(year)
            # print(link)
            # print('*' * 70)

            # time.sleep(1)
    await state.clear()



    


