from fileinput import filename
import smtplib
import time
from email.message import EmailMessage
msg = EmailMessage()
msg['Subject'] = 'looking for a job in sales'
msg["From"] = 'Toumi Ammar Mekki'
msg["to"] ='careers@khaasit.com'

with open('CoverLetterDesign.txt') as myfile:data=myfile.read()
msg.set_content(data)

with open('Meki Sales.pdf',"rb") as f:file_data=f.read()
print("file data is binary" , file_data)
file_name=f.name
print("file name is",file_name)
msg.add_attachment(file_data,maintype="application",subtype="pdf",filename=file_name)


sender_email = "amartoumi100@gmail.com"
# message = "Ammar Hacked"
rec_email = "careers@khaasit.com"


password = input(str("please enter your password :"))
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
print("Login success")
server.send_message(msg)

print("Email has been sent to ",rec_email)
