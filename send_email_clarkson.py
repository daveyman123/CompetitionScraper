#!/usr/bin/python
import subprocess
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
import datetime
import time
import os

def sendmail():
#	os.remove(filez)
	subprocess.call(["sudo scrapy crawl AStorageInnClarkson"],shell = True)
#	time.sleep(10)
	subprocess.call(["sudo scrapy crawl PublicStorageClarkson"],shell = True)
#	time.sleep(10)
	subprocess.call(["sudo scrapy crawl ExtraSpaceClarkson"],shell = True)
#	time.sleep(10)
#	subprocess.call(["sudo scrapy crawl ExtraSpaceDoug22"],shell = True)
#        time.sleep(10)

 #       subprocess.call(["sudo scrapy crawl StPeters"],shell = True)
#	time.sleep(100)
        

	filez = "/home/pi/business/%s.csv" %(datetime.datetime.now().strftime("%H"))

	part = MIMEBase('application', "octet-stream")
	part.set_payload(open(filez, "rb").read())


	msg = MIMEMultipart()
	msg['From'] = "djgraff1@cougars.ccis.edu"
	msg['To'] = "astorageinnlemay@gmail.com"
	msg['Date'] = formatdate(localtime = True)
	msg['Subject'] = "Competition Report"
	msg.attach(MIMEText("Clarkson"))




	content = 'example email stuff here'

	mail = smtplib.SMTP('smtp.gmail.com',587)

	mail.ehlo()

	mail.starttls()

	mail.login('djgraff1@cougars.ccis.edu','2ZNf+Uy}')

	encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="data Clarkson %s.csv"'%(datetime.datetime.now().strftime("%m-%d-%y")))
	msg.attach(part)

       

        print 'email sent'
        mail.sendmail('djgraff1@cougars.ccis.edu','astorageinnlemay@gmail.com',msg.as_string())
#	time.sleep(33)
	os.remove(filez)

def sleep():
    time.sleep(4000)


def monitor():
   
    while True:
	weekday = datetime.datetime.today().weekday()
        curr_time = datetime.datetime.now().time()
        curr_hour = curr_time.hour
	curr_min = curr_time.minute
	print curr_hour
	time.sleep(3)
        #if weekday == 1 or weekday == 2 or weekday == 4:
	#	if curr_hour == 12: #and curr_min == 30:
	sendmail()
	break;
def main():


	
	monitor()

if __name__ == '__main__':
    main()

