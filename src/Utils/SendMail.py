import smtplib
from src.Utils import PackageMail

class sendmail:
    def sendMail(self,sender,subject,mail_pass,mail_host,mail_user,header,enclosurepath):
        number = 1
        err = 0
        Success = 0
        #读取邮箱发件人列表信息
        f = open("./file/邮箱账号.txt", "rt", encoding ='utf-8', errors='ignore')

        for address in f:
            c = address.split('\n')[0]
            receivers = [c]
            message = PackageMail.getMail(sender,receivers,subject,enclosurepath)
            number += 1
            try:
                smtpObj = smtplib.SMTP()
                smtpObj.connect(mail_host, 25)
                #登陆授权邮箱
                smtpObj.login(mail_user, mail_pass)
                #？？？此处是否可以加多线程做邮箱doss？？？
                smtpObj.sendmail(sender, receivers, message.as_string())
                smtpObj.close()
                print("Success")
                Success += 1
            except smtplib.SMTPException:
                print("Error")
                err += 1
        f.close()
        # 邮件总数
        all = Success + err
        print("共发送" + str(all) + "封邮件，成功发送" + str(Success) + "封邮件，有" + str(err) + "封邮件产生错误。")
