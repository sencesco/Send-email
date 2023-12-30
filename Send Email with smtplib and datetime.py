import smtplib

my_email = "Yourmail@gmail.com"
# For use smtplib: Need to generate App Password not your passwod
password = "YourApp_pass"

connection = smtplib.SMTP("smtp.gmail.com")
# Connet to tls, TLS is Transport Layer Security 
# can see more TLS info.: https://en.wikipedia.org/wiki/Transport_Layer_Security
connection.starttls()
connection.login(user=my_email, password=password)

# msg="Subject:" for make a mail subject and follow double \n (\n\n) for new line and write a mail content
connection.sendmail(from_addr=my_email, to_addrs="reciever@hotmail.com", 
                    msg="Subject:Hello from python send mail test\n\n Test Tes, if read it, that will copleted to send")
connection.close()


my_email2 = "Yourmail@hotmail.com"
# For use smtplib: Need to generate App Password not your passwod
password2 = "YourApp_pass"


# We can also do same as file handling wtih a with statement like a code below for ignore connection.close()
with smtplib.SMTP("smtp.outlook.com") as connection2:
    connection2.starttls()
    connection2.login(user=my_email2, password=password2)
    connection2.sendmail(from_addr=my_email2, to_addrs="reciever@gmail.com", 
                        msg="Subject:Hello from python send mail reply\n\n I already recieve it.")
    
import datetime as dt    
 
now = dt.datetime.now()    # Retunr a current time
year = now.year
month = now.month
day_of_week = now.weekday()
print(f"I't is current tiem: {now}.")
print(f"The type of \"now\" object: {type(now)}.")
print(f"This year is a {year}.")
print(f"This month is {month}.")
print(f"This is {day_of_week} of a week.")

date_of_birth = dt.datetime(year=1993, month=4, day=23)
print(f"Date of Birth: {date_of_birth}")





