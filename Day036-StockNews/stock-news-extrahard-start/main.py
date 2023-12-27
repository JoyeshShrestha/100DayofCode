import requests
import os

from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").\


stock_api = "https://www.alphavantage.co/query"
parameter_stock = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey" :os.environ['STOCK_API_KEY']
}
response = requests.get(stock_api,params=parameter_stock)

response.raise_for_status()
stock_data = response.json()

data = stock_data
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
value =(difference/day_before_yesterday_closing_price)*100
# value = 6


if value > 5:
    new_api = "https://newsapi.org/v2/everything"
    news_parameter = {
        "q":COMPANY_NAME,
        "from":"2023-12-22",
        "sortBy":"popularity",
        "apiKey":os.environ['NEWS_API_KEY']
                }
    
    news_response = requests.get(new_api,params=news_parameter)
    news_data = news_response.json()
    articles_list = news_data["articles"]

    for i in range(3):
        print(articles_list[i])
print(value)    


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

