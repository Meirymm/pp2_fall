import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
difference = (today - yesterday).total_seconds()/60 #minutes
difference1 = (today - yesterday).total_seconds() #seconds

print(today)
print(yesterday)
print(difference)
print(difference1)
