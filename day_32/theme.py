"""
# SMTP
# simple mail transfer protocol

import smtplib

my_email = "englishisakovich@gmail.com"
password = "hydtordiwiqbxxrq"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="asilbeknitu@gmail.com", msg="Hello")
connection.close()

"""


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

day_today = dt.datetime(year=2020, month=12, day=11)
print(day_today)

