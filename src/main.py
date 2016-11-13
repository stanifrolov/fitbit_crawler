import fitbit

from src.settings import client_id, client_secret, access_token, refresh_token

authd_client = fitbit.Fitbit(client_id,
                             client_secret,
                             access_token=access_token,
                             refresh_token=refresh_token)


def intraday_heart(date):
    heart = authd_client.intraday_time_series('activities/heart', date)
    heartrate_dataset = heart['activities-heart-intraday']['dataset']
    heart = {}
    for entry in heartrate_dataset:
        heart[entry['time'].encode('ascii')] = entry['value']

    return heart

date = '2016-10-15'
heartrate_data = intraday_heart(date)

for d, hr in sorted(heartrate_data.items()):
    print d, hr

