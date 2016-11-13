import fitbit
import xlsxwriter
import collections

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

    heart = collections.OrderedDict(sorted(heart.items()))

    workbook = xlsxwriter.Workbook('heartrate.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    worksheet.write(row, col, 'Date')
    worksheet.write(row, col + 1, 'Heartrate')

    row += 1

    for key in heart.keys():
        row += 1
        worksheet.write(row, col, key)
        worksheet.write(row, col + 1, heart[key])

    workbook.close()

intraday_heart('2016-10-15')
