import time
from internetspeedbot import InternetSpeedTwitterBot

UP_PAYMENT = 500
DOWN_PAYMENT = 5000

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()

if float(bot.down) < DOWN_PAYMENT or float(bot.up)<DOWN_PAYMENT:
    bot.tweet_at_provider(UP_PAYMENT,DOWN_PAYMENT)

