import requests
import time
import configparser
from bs4 import BeautifulSoup

config = configparser.ConfigParser()
config.read('config.ini')

company_url = config['DEFAULT']['CompanyURL']
api_token = config['DEFAULT']['APIToken']
chat_id = config['DEFAULT']['ChatId']



def send_message():
    print("Send Message")

    message = 'Água voltou ou algo mudou'
    apiURL = f'https://api.telegram.org/bot{api_token}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chat_id, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)



while True:

    page = requests.get(company_url)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="statusModal")
    box_title = results.find("div", class_="box-titulo")
    status = box_title.find("div").find("div")["style"]

    if "#f51616" not in str(status):
        print("Changes Found!")
        send_message()
    else:
        print("Nothing changed, but I'm still alive!")

    time.sleep(600)
