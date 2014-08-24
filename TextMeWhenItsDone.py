"""
TextMeWhenItsDone.py
"""
import smtplib

def TextMe(email, password, phonenumber, carrier, sender = "YO"):
    if email == gmail:
        server = smtplib.SMTP("smtp.gmail.com", 587)
    
    server.login(email, password)
    server.sendmail(sender, phonenumber + carrier, "Hey your program is done")
