import smtplib, random
import datetime as dt

RECIPIENT_EMAIL = 'emailfortest.sh@gmail.com'
MY_EMAIL = 'emailfortest.sh@gmail.com'
MY_PASSWORD = 'mntgpnjbuaehvymo'

with open('quotes.txt') as file:
    content = file.read().splitlines()

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    connection = smtplib.SMTP('smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECIPIENT_EMAIL,
                        msg=f'Subject:Monday Motivational Quote\n\n{random.choice(content)}')
    connection.close()
