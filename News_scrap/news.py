from newsapi.newsapi_client import NewsApiClient
import pandas as pd
import param
import newsabout
from automail import send_mail
from secret import key

newsapi = NewsApiClient(api_key=key)

# /v2/top-headlines

topic=newsabout.preference[0]
top_headlines = newsapi.get_everything(q=topic,
                                       domains=param.market_domains,
                                        language=param.language,
                                       from_param=param.fromdt,
                                        #to='2021-01-23',
                                       sort_by=param.sort
                                          )

articles=top_headlines['articles']

df=pd.DataFrame(articles)

df['publishedAt']=pd.to_datetime(df['publishedAt'], format="%Y-%m-%dT%H:%M:%SZ")


if top_headlines['status'] == 'ok':
    print('Total', top_headlines['totalResults'],'articles found from sources.')
else:
    print('OOps!! Result not found')

send_mail(df,topic)

