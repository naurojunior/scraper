import requests
import time
import configparser
from bs4 import BeautifulSoup

config = configparser.ConfigParser()
config.read('config.ini')

company_url = config['DEFAULT']['CompanyURL']
api_token = config['DEFAULT']['APIToken']
chat_id = config['DEFAULT']['ChatId']

previous_status = None
current_status = None


def send_message(message):
    print("Send Message")

    api_url = f'https://api.telegram.org/bot{api_token}/sendMessage'

    try:
        response = requests.post(api_url, json={'chat_id': chat_id, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)


while True:

    page = requests.get(company_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'})

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="statusModal")
    box_title = results.find("div", class_="box-titulo")
    status = box_title.find("div").find("div")["style"]

    if "#f51616" in str(status):
        current_status = "broken"
    else:
        current_status = "working"

    if previous_status is None:
        previous_status = current_status

    if previous_status != current_status:
        print("Changes found! Current status:" + current_status)

        if current_status == "broken":
            current_message = "Interrupção no serviço de água"
        else:
            current_message = "Serviço de água voltou a funcionar"

        send_message(current_message)
    else:
        print("Nothing changed. Still alive. Current status:" + current_status)

    previous_status = current_status

    time.sleep(600)
