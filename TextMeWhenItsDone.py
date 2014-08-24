"""
TextMeWhenItsDone.py
"""
import smtplib

GMAIL = "gmail.com"

def TextMe(email, password, phonenumber, carrier, sender = "YO"):
    if email[email.index("@")+1:] == GMAIL:
        server = smtplib.SMTP("smtp.gmail.com", 587)

    if carrier == "ATT":
        carrier = "@mms.att.net"
        
    server.starttls()
    server.login(email, password)
    server.sendmail(sender, phonenumber + carrier, "Hey your program is done")
