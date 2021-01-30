import datetime as dt
import pytz

current_date = dt.datetime.now(pytz.timezone('Asia/Kolkata')).date()
current_time = dt.datetime.now(pytz.timezone('Asia/Kolkata')).time()
previous_day=current_date-dt.timedelta(days=1)

if current_time.hour<=12:
    time='T14:30:00'
else:
    time = 'T09:00:00'

fromdt=f'{previous_day.isoformat()}'+time

market_domains='bloombergquint.com,livemint.com,moneycontrol.com,economictimes.indiatimes.com,business-standard.com,financialexpress.com'
#bolly_domains=
#india_domains=
#international_domains=
#science_domains=
#tech_domains=

language='en'
sort='publishedAt'

