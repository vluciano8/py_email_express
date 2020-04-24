from pyfiglet import Figlet
from clint.textui import colored, puts

import smtplib
import config
import colors
import getpass


f = Figlet(font='doom')
print (f.renderText('Email Express'))
print (colors.colorText('[[blue]] [[white-background]] version 1.0 [[white]] [[blue-background]]\n'))

#-------Optional Settings (Also can be modified as default values in config.py file associated)
name = input('> What is your name? ')
print(f'\nHola {name}!!\n')

config.EMAIL_ADDRESS = input('\n >What is your email? ')

config.PASSWORD = getpass.getpass("\n >What is your password? ")

print(config.PASSWORD)

config.DEST_ADDRESS = input('\n >To whom is the email? ')

#------------------------------------------------------------------------------------------------

subject = input('\n> What would be the subject of the email?\n\n ') 
msg = input('\n> Write the email:\n\n ')

def send_email(subject, msg):
    try:
        server = smtplib.SMTP(config.SMTP_ADDRESS)
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.DEST_ADDRESS, config.DEST_ADDRESS, message)
        server.quit()
        print(colors.colorText('\n[[green]][[black-background]] Yep!! Email Sent!! [[white]]\n'))
    except:
        print(colors.colorText('\n[[red]][[black-background]] Boomer!! Something failed!! [[white]]\n'))


send_email(subject, msg)
