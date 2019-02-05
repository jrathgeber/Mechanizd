import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.utils import COMMASPACE, formatdate
from email import encoders

def send_mail( send_from, send_to, subject, text, files, server, port, username, password, isTls=True):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = subject
	
    msg.add_header('Content-Type','text/html')
    msg.attach( MIMEText(text, 'html') )

    for f in files:
        part = MIMEText('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
        msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    if isTls: smtp.starttls()
    smtp.login(username,password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
