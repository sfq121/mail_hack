from email.header import Header
from email.mime.multipart import MIMEMultipart

from src.Utils import Html2Mail, EnclosureUtil

def getMail(sender,receivers,subject,enclosurepath):
        #读取html作为邮件
    html = open("./file/邮件内容.html", "rt", encoding='utf-8', errors='ignore')
    mailhtml = html.read()
    # 创建邮件对象
    message = MIMEMultipart()
    # 发送的html转为邮件
    Html2Mail.addmailhtml(mailhtml, message)
    # 如果附件地址不为空则,进行附件发送操作
    if len(enclosurepath) != 0:
       EnclosureUtil.addenclosure(enclosurepath, message)

    #填充mess信息
    message['From'] = Header(sender)
    message['To'] = Header(receivers[0])
    message['Subject'] = Header(subject)

    html.close()
    return message