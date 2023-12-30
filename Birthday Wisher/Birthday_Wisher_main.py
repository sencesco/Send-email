import pandas as pd
import smtplib
import datetime as dt
import random as rd

my_email = "Yourmailt@gmail.com"
password = "YourApp_pass"
stmp_mail_client = "smtp.gmail.com"
re_name_reciever = "[NAME]"
re_name_sender = "Angela"
file_path = f"letter_templates/letter_{rd.randint(1,3)}.txt"
num = 0

current_dt  = dt.datetime.now()
current_month = current_dt.month
current_day =  current_dt.day

df_list_fr = pd.read_csv("birthdays.csv", index_col=False)
df_match_name_and_email = df_list_fr[(df_list_fr['month'] == current_month) & (df_list_fr['day'] == current_day)][['name','email']]
match_name = df_match_name_and_email['name'].tolist()
match_email = df_match_name_and_email['email'].tolist()

for name in match_name:
    with open(file_path) as letter_file:
        content = letter_file.read()
    with smtplib.SMTP(stmp_mail_client) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        content = content.replace(re_name_reciever, name)
        content = content.replace(re_name_sender, "Sencs")
        connection.sendmail(from_addr=my_email, to_addrs=match_email[num], 
                        msg=f"Subject: Happy Birthday (Test python send via email)\n\n{content}") 
    num+=1   

