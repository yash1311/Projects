import requests
from bs4 import BeautifulSoup
from automail import send_mail

url='https://www.amazon.in/Microsoft-Surface-PUV-00028-Touchscreen-Graphics/dp/B084HZRFH6/ref=sr_1_3?crid=RESM53VF5ARM&dchild=1&keywords=surface&qid=1611381050&sprefix=surface%2Caps%2C403&sr=8-3'
url2='https://www.amazon.in/Microsoft-STQ-00013-10-1-inch-Processor-Graphics/dp/B08DHHB2W1/ref=sr_1_4?dchild=1&keywords=surface&qid=1611383531&sr=8-4'
head = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}


def check_price():
    page = requests.get(url, headers=head)

    soup =BeautifulSoup(page.content, 'html.parser')

    title=soup.find(id='productTitle').get_text()
    price=soup.find(id="priceblock_dealprice").get_text()
    converted_price1=price[2:]
    converted_price2=float(converted_price1.translate({ord(','): None}))

    if converted_price2>=90000.00:
        send_mail(url)


    print(title.strip())=-
    print(converted_price2)


check_price()