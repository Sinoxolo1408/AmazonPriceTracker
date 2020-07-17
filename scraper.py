import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = input('Enter amazon URL here:')  # Amazon URL for specific item

userAgent = input('Enter your user agent here:')
headers = {"User-Agent": ''}  # Google search 'my user agent' and copy text and paste here


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()  # The product you want tracked
    price = soup.find(id="priceblock_ourprice").get_text()  # The price that you will tracking
    converted_price = float(price[0:5])

    if converted_price < 1.000:  # desired price
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # Generating password
    server.login("Email", "Password")  # Add email address and generated password

    subject = 'Price has dropped'
    body = 'Check the amazon link ...'  # Include the above URL

    msg = f"Subject: {subject}\n\n{body}"

    primary_email = input('Primary Email:')
    secondury_email = input('Secondury Email:')
    server.sendmail(primary_email, secondury_email, msg)

    print('Email has been sent')

    server.quit()


while True:
    check_price()
    time.sleep(60 * 60)  # Time program not running
