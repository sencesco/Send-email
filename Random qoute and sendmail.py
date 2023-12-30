import smtplib
import datetime as dt
import random as rd

my_email = "Yourmail@gmail.com"
password = "YourApp_pass"

current_dt  = dt.datetime.now()
current_day_week = current_dt.weekday()
if current_day_week == 4:
    with open("quotes.txt") as bd_file:
        list_fr = bd_file.readlines()
        qoute = rd.choice(list_fr)
    
    print(qoute)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="reciever@hotmail.com", 
                        msg=f"Subject: Friday Motivation\n\n{qoute}")
    
    