import fitbit
from settings import client_id, client_secret, access_token, refresh_token

authd_client = fitbit.Fitbit(client_id,
                             client_secret,
                             access_token=access_token,
                             refresh_token=refresh_token)

data = authd_client.intraday_time_series('activities/heart')

print(data)
