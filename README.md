# water-scraper
Just a side project to alert me when water systems went down / up.

This program keeps watching the water company from my city, and in case of the status changes from red to yellow/green, it sends me a message on Telegram.

If you live in another place, the scraper won't work, since I programmed to work with the water company from my city :V

But anyway, if works as inspiration, you have to create a file called `config.ini` with the format like:

```
[DEFAULT]
CompanyURL = [COMPANY_URL]
APIToken = [YOUR_BOT_API_TOKEN_FROM_TELEGRAM]
ChatId = [YOUR_CHAT_ID_FROM_TELEGRAM]
```

Known issue:
If you start the script with the status different from red, it will send you messages each 10 minutes. Since it's a very specific project done in 30 minutes or less, I don't care too much for me.
