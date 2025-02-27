import requests
import fake_useragent
from bs4 import BeautifulSoup
import time

user = fake_useragent.UserAgent().random

header = {'user-agent': user}

pages = 2
yearFrom = "2010"
priceFrom = "2000000"


for page in range(1, pages+1):

    link = "https://kolesa.kz/cars/astana/?year[from]="+ yearFrom + "&price[from]=" + priceFrom + "&page" + str(page)

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
        


        print(title)
        print(price)
        print(year)
        print(link)
        print('*' * 70)

        # time.sleep(1)







