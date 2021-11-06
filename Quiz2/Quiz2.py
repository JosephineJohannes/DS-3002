import requests
import csv
import time
import pandas as pd
import re

again = True
f = open('TickerList.txt', 'r')
content = f.read()

while(again):
    stock_ticker = input("What single stock ticker would you like to see? ")
    if stock_ticker in content:
        url = "https://yfapi.net/v6/finance/quote"
        querystring = {"symbols": stock_ticker}

        headers = {
            'x-api-key': "a4z8IUpfTSMBN0gI1yLW9QrxUgnlCuY3VMw0Sdn1"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        response.raise_for_status()  # raises exception when not a 2xx response
        response = response.json()

        current_price = str(response['quoteResponse']['result'][0]['regularMarketPrice'])
        print("Current Price $" + current_price)
        market_time = response['quoteResponse']['result'][0]['regularMarketTime']
        market_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(market_time))
        print("Market Time: " + market_time)
        company_name = str(response['quoteResponse']['result'][0]['shortName'])
        print("Company Name: " + company_name)

        with open('stock_file.csv', mode='a', newline='') as stock_file:
            stock_writer = csv.writer(stock_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            stock_writer.writerow([stock_ticker, market_time, current_price])

        answer = input("Would you like to input another single ticker? Type Yes for another input and No to stop ")
        if answer == "No":
            again = False
        else:
            again = True

    else:
        print("Please input a valid stock symbol")

f.close()
