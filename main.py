# Modules needed to draw the graph
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Self-written modules
import api_news
import api_oil_price

# Module to print in a more readable way
from pprint import pprint

# ==========================================================================================
# API NEWS PART

# hon men jib l api key tabaana
# your_api_token = '73EXkhBScAMyyGPOLzjiRetGdvnPJpXzt23EKjlm'
# raw_news_data = api_news.get_raw_data(your_api_token)
# couples_of_tag_sentiments_industry = api_news.get_sentiment_and_industry(raw_news_data)
# ==========================================================================================


# ==========================================================================================
# API OIL PRICE PART

BRENT_API_KEY = '7T76J7QNTQY2YTVV'
# we get the raw data from the API
raw_jsonified_data = api_oil_price.get_raw_data_monthly(BRENT_API_KEY)
pprint(raw_jsonified_data)

# ==========================================================================================