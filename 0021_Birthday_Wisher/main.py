import pandas as pd
import datetime as dt
import random, os, smtplib

MY_NAME = 'Hossein'
MY_EMAIL = 'emailfortest.sh@gmail.com'
MY_PASSWORD = 'mntgpnjbuaehvymo'

letters = os.listdir('./letters')
birthdays = pd.read_csv('./birthdays.csv').to_dict()

# Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
for i in range(len(birthdays['name'])):
    if birthdays['month'][i] == now.month and birthdays['day'][i] == now.day:
        # Pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f'./letters/{random.choice(letters)}') as file:
            content = file.read()
            content = content.replace('[NAME]', birthdays['name'][i])
            content = content.replace('[MYNAME]', MY_NAME)
                
        # Send the generated letter to that person's email address.
        connection = smtplib.SMTP('smtp.gmail.com', port=587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthdays['email'][i],
                            msg=f'Subject:Happy Birthday {birthdays['name'][i]}!\n\n{content}')
        connection.close()
