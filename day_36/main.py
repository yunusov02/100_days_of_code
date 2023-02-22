import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "I78L9LP31XRKSCYP"
NEWS_API_KEY = "1aaae68768254561b3db3bf40d9deddf"


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

# But now daily is premium that's why I used WEEKLY
stock_params = {
    'function': 'TIME_SERIES_WEEKLY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}
response = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
response.raise_for_status()

data: dict = response.json()['Weekly Time Series']
data_list = [i for i in data.values()]
yesterday_data = data_list[0]
yesterday_closing_price = data_list[0]['4. close']


#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = data_list[1]['4. close']


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage = (difference / float(yesterday_closing_price)) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# if diff_percentage > 5:
#     print("Great news")

## STEP 2: https://newsapi.org/ 
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if diff_percentage > 5:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qInTitle':COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

three_articles = articles[:3]

## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_article = [f"Headlines {article['title']}. \nBreif {article['description']}" for article in three_articles]
#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

