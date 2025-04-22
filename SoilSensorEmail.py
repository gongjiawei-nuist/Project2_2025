import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)
from_email_addr="bno03972367@163.com"
from_email_pass="GTNMYJAJP8h2ghT5"
to_email_addr="bno03972365@163.com"
daily_readings=[]
def send_email(moisture_status):
	msg=EmailMessage()
	body=f"Soil moisture: {moisture_status}"
	msg.set_content(body)
	msg['From']=from_email_addr
	msg['To']=to_email_addr
	msg['Subject']='moisture status report'
	server=smtplib.SMTP('smtp.163.com',25)
	server.starttls()
	server.login(from_email_addr,from_email_pass)
	server.send_message(msg)
	server.quit()
try:
	while True:
		moisture_status ="dry"if GPIO.input(channel)else "wet"
		send_email(moisture_status)
		time.sleep(60)
except KeyboardInterrupt:
	GPIO.cleanup()
