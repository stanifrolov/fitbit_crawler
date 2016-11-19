from datetime import timedelta, datetime

import xlsxwriter
import collections


def retrieve_intraday_heart(authd_client, client_id, start_date, period):
    """
    Retrieves intraday heart data and saves it in a xlsx document.
    :param authd_client: authorized FitbitOauth2Client object
    :param client_id: fitbit client id as
    :param start_date: start date of which data shall be retrieved
    :param period: days of period
    """
    for days in range(period):
        date = datetime.strftime(start_date - timedelta(days), '%Y-%m-%d')
        heart = authd_client.intraday_time_series('activities/heart', date)
        heartrate_dataset = heart['activities-heart-intraday']['dataset']

        if heartrate_dataset:
            heart = {}

            for entry in heartrate_dataset:
                heart[entry['time'].encode('ascii')] = entry['value']

            heart = collections.OrderedDict(sorted(heart.items()))

            workbook = xlsxwriter.Workbook('heart-intraday' + '-' + client_id + '-' + date + '.xlsx')
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
