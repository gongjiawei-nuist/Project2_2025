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
daily_reading=[]
def callback(channel):
        if not GPIO.input(channel)
		send_daily_report()
GPIO.add_event_detect(channel,GPIO.BOTH,bouncetime=300)
GPIO.add_event_callback(channel,callback)
def send_daily_report():
	msg=EmailMessage()
	body="Daily Moisture Report"
	msg.set_content(body)
	msg['From']=from_email_addr
	msg['To']=to_email_addr
	msg['Subject']='TEST EMAIL'
	server=smtplib.SMTP('smtp.163.com',25)
	server.starttls()
	server.login(from_email_addr,from_email_pass)
	server.send_message(msg)
	server.quit()
while True:
        reading =GPIO.input(channel)
	daily_readings.append(reading)
	time.sleep(3600)
	if len(daily_readings)==4
		send_daily_report()
		daily_readings=[]
