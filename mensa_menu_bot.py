#!/usr/bin/env python3
import os
import time
import schedule
import requests
from telegram import Bot
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from datetime import datetime
from deep_translator import GoogleTranslator

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

# Create a Telegram Bot instance
bot = Bot(token=API_TOKEN)


def today_menu():
  menu = ""
  today_date = datetime.today().strftime('%d.%m.%Y')
  try:
    URL = "https://www.stw-thueringen.de/mensen/weimar/cafeteria-schwanseestrasse.html"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    meals = soup.find_all('div', class_='rowMeal')

    items = []
    for meal in meals:
      name = meal.find('div', class_='mealText')
      name_en = GoogleTranslator(source='auto', target='en').translate(name.text)
      price = meal.find('div', class_='mealPreise')
      item = name.text + ' (DE)\n' + name_en + " (EN)\n" + price.text
      items.append(item)
    menu = "Date: " + today_date \
            + "\n-----\n" \
            + "\n-----\n".join(items)    
  except:
    menu = "There is a problem with the server."
      
  bot.send_message(chat_id=CHANNEL_ID, text=menu)

# scheduled task
schedule.every().monday.at("08:00:00").do(today_menu)  
schedule.every().tuesday.at("08:00:00").do(today_menu)  
schedule.every().wednesday.at("08:00:00").do(today_menu)  
schedule.every().thursday.at("08:00:00").do(today_menu)  
schedule.every().friday.at("08:00:00").do(today_menu)  

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
