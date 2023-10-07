import smtplib
from email.message import EmailMessage

from email.message import EmailMessage


def createMessage(content):
    message = EmailMessage()
    message['Subject'] = "hkexnews report"
    message['From'] = 'hkexnews spider'
    message['To'] = 'hkcto.com@gmail.com'
    message.set_content(content)
    return message


class Gmail():
    def __init__(self, username, secret) -> None:
        """usernaem: gmail user name
        secret: gmail 16-digit-app-password"""
        
        self.username = username
        self.secret = secret

    def send(self, msg: EmailMessage):

        # message = EmailMessage
        # message['Subject'] = "hkexnews report"
        # message['From'] = 'hkexnews spider'
        # message['To'] = 'hkcto.com@gmail.com'
        # message.set_content('gmail hello world')
        
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            try:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(self.username, self.secret)
                smtp.send_message(msg)
                print('Email sent Complete!')
            except Exception as e:
                print(e)
                

if __name__=="__main__":
    
    message = createMessage("createMessage Testing")
    
    gmail = Gmail(username="hkcto.com@gmail.com", secret="qtjdbtvgysljmpup")
    # message = EmailMessage()
    # message['Subject'] = "MarkSix"
    # message['From'] = 'HKJC'
    # message['To'] = 'hkcto.com@gmail.com'
    # message.set_content(f'日期:\n財運號碼: \n結餘:')
    gmail.send(message)  