#SendMail.py
import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendEmailFn(fromaddr, toaddr, mailPass, zipFiles, dirPath):
    print('SendMail')
    try: 
        #set test values    
        #fromaddr = 'fromaddr@mail.com'
        #toaddr= ['mailone@mail.com', 'mailtwo@mail.com']
        #mailPass='passValue'
       
        #build mail message + attachment
        message = MIMEMultipart()
        message['From'] = fromaddr
        message['To'] = ','.join(toaddr)
        message['Subject'] = "Sabre Reports {}".format(date.today())
        body = 'This is a test mail. Current date {}. Please do not respond.'.format(date.today())
        message.attach(MIMEText(body, 'plain'))
      
        for toAttach in zipFiles:
            attachFile = open(toAttach, "rb")
            attachedFile = MIMEBase('application', 'octet-stream')
            attachedFile.set_payload((attachFile).read())
            encoders.encode_base64(attachedFile)
            fileName = str(toAttach).replace(dirPath,'')
            attachedFile.add_header('Content-Disposition', "attachment;filename= %s" % fileName)
            message.attach(attachedFile)
        
        #connect to a mail server and send mail
        server = smtplib.SMTP('mail_smtp_host_value', portValue)#replace smtp_host_value and port value for the real ones
        server.starttls()
        server.login(fromaddr, mailPass)
        mailMessage = message.as_string()
        server.sendmail(fromaddr, toaddr, mailMessage)
        server.quit()
        return 0
        print("Mail Sended")
    except Exception as e:
        print('Error sending mail message ', e)
        return 1