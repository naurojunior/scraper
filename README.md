# water-scraper
Just a side project to alert me when water systems went down.

This program keeps watching the water company from my city, and in case of the status changes from red to yellow/green, it sends me a message on Telegram.

If you live in another place, the scraper probably won't work, since I programmed to work with the water company from my city :V

But anyway, if works as inspiration, you have to create a file called `config.ini` with the format like:

```
[DEFAULT]
CompanyURL = [COMPANY_URL]
APIToken = [YOUR_BOT_API_TOKEN_FROM_TELEGRAM]
ChatId = [YOUR_CHAT_ID_FROM_TELEGRAM]
```
