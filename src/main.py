import fitbit
from fitbit_crawler import *
from datetime import datetime

from src.settings import client_id, client_secret, access_token, refresh_token


# FitbitOauth2Client
client = fitbit.Fitbit(client_id, client_secret, access_token=access_token, refresh_token=refresh_token)

today = datetime.now().date()
period_of_days = 30

retrieve_intraday_heart(client, client_id, today, period_of_days)
