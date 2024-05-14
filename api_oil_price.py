import requests

def get_raw_data_monthly(api_token_key):
    url = 'https://www.alphavantage.co/query?function=BRENT&interval=monthly&apikey={}'.format(api_token_key)
    response = requests.get(url)
    data = response.json()
    return data