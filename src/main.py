#import Utils as Utils
from src.Utils import SendMail


class mailHack:
    def __init__(self):
        self.sender = "1448117242@qq.com"
        self.subject = "aa"
        self.mail_pass = "daqyavgqmwcbbaaj"
        self.attNum = ""
        self.mail_host = "smtp.qq.com"
        self.mail_user = "1448117242@qq.com"
        self.enclosurepath = ""
        self.header = ""

    def main(self):
        SendMail.sendmail.sendMail(self,self.sender,self.subject,self.mail_pass,self.mail_host,self.mail_user,self.header,self.enclosurepath)


        
if __name__ == '__main__':
     mailhack = mailHack()
     mailhack.main()
