import fitbit
from fitbit_crawler import *

from src.settings import client_id, client_secret, access_token, refresh_token


# FitbitOauth2Client
client = fitbit.Fitbit(client_id, client_secret, access_token=access_token, refresh_token=refresh_token)

retrieve_intraday_heart(client, client_id, '2016-11-02')
