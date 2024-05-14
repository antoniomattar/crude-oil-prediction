import http.client, urllib.parse

def get_raw_data(TOKEN):
    conn = http.client.HTTPSConnection('api.marketaux.com')
    params = urllib.parse.urlencode({
        'api_token': TOKEN,
        'symbols': 'AAPL,TSLA',
        'limit': 50,
        })

    conn.request('GET', '/v1/news/all?{}'.format(params))

    res = conn.getresponse()
    data = res.read()
    decoded_data = data.decode("utf-8")
    # JSONify the data
    import json
    jsonified_data = json.loads(decoded_data)
    return jsonified_data

def get_sentiment_and_industry(data):
    couples_of_tag_sentiments_industry = []
    for article in data['data']:
        entities = article['entities']
        for entity in entities:
            couples_of_tag_sentiments_industry.append( ( entity['symbol'], entity['industry'], entity['sentiment_score']) )
    
    return couples_of_tag_sentiments_industry