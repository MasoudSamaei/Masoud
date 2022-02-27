
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

user_name = 'masoud.samaei71@gmail.com'
password = 'masoudsamaie@1371'

server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.ehlo()
server.starttls()

# login to my smtp server
server.login(user_name, password)


CV = open('Masoud Samaei CV.pdf', 'rb')
attachment = CV.read()

msg = MIMEMultipart('mixed')
from_email = 'Masoud Samaei <masoud.samaei71@gmail.com>'
msg['From'] = from_email

To = 'masoud.samaie@gmail.com'
msg['To'] = 'masoud.samaie@gmail.com'


ProfessorName = 'Samaei'
ReminderBodyText = f""" Dear Dr. {ProfessorName},

I'm sure you must be really busy, and I don't want to seem to interrupt. I am waiting for your feedback on my previous email.
Hope you can find a few minutes on this. I appreciate your time.

Also, I am attaching the previous email and CV on this email on the case that has been deleted accidently.

Sincerely yours,
Masoud Samaei

====================================
**************************************************
====================================
"""

field_of_professor = 'rock mechanics'
subject = f'Prostective PhD student interested in {field_of_professor}'
msg['Subject'] = subject

txt_part = MIMEText(ReminderBodyText, 'plain')
msg.attach(txt_part)

pdfname = 'Masoud Samaei CV.pdf'
part = MIMEBase('application', 'octet-stream', Name=pdfname)
part.set_payload(attachment)
encoders.encode_base64(part)
part.add_header('Content-Decomposition', 'attachment', filename=pdfname)

msg.attach(part)

msg_str = msg.as_string()

server.sendmail(from_email, To, msg_str)
print(f'Successfully sent to {To}')

time.sleep(15)

server.quit()
