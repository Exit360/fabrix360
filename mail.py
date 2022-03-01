import smtplib
from email.message import EmailMessage
import email.message



def email(useremail,message):
	
	
	email = "fabrix360.com@gmail.com"
	email_user = "fabrix360.com@gmail.com"
	email_send = email
	subject = f"Message from Heroku app by {useremail}"
	# msg = MIMEMultipart()//no more needed becaus eyou imported sendemail instead i deleted MIMEM imports
	msg = EmailMessage()
	msg['from'] = email_user
	msg['To'] = email_send
	msg['Subject'] = subject
	message = message
	body = message 
	msg.set_content(body)
	text = msg.as_string()
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	
	# server.starttls() /because you used SMTP_SSL and changed port to 465
	server.login(email_user, 'jxmdkohbjmsuoxge')
	# server.sendmail(email_user, email_send, text)
	server.send_message(msg)
	server.quit()