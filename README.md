# fitbit_crawler
Fibit data crawler using the python fitbit API implementation https://github.com/orcasgit/python-fitbit

## How to use

Create a ```settings.py``` file and provide

```
client_id = <FITBIT APP CLIENT ID>
client_secret = <FITBIT APP CLIENT SECRET>
access_token = <FITBIT APP ACCESS TOKEN>
refresh_token = <OPTIONAL>
```

## Download intraday-heartrate data as xlsx file

Run ```main.py``` and provide a date string as ```YYYY-MM-DD``` where the
``retrieve_intraday_heart(client, client_id, date)`` function is called.
