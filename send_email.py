import smtplib
from email.message import EmailMessage

from_email_addr="bno03972367@163.com"
from_email_pass="GTNMYJAJP8h2ghT5"
to_email_addr="bno03972365@163.com"

msg=EmailMessage()
body="Hello from Raspberry Pi"
msg.set_content(body)
msg['From']=from_email_addr
msg['To']=to_email_addr
msg['Subject']='TEST EMAIL'
server=smtplib.SMTP('smtp.163.com',25)
server.starttls()
server.login(from_email_addr,from_email_pass)
server.send_message(msg)
print('Email sent')
server.quit()
