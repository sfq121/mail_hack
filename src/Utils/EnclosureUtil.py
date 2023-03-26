from email.mime.application import MIMEApplication

from src.Utils import DownFile

def addenclosure(enclosurepath, message):
        for filepath in enclosurepath:
                filename = filepath.split('/')[-1]
                # 判断是否为url
                if filepath[0:4] == 'http':
                        urlfile = DownFile.getfile(filepath, filename)
                        filepath = urlfile[0]
                        filename = urlfile[1]
                        # 调用currencyfile方法
                        message.attach(currencyfile(filepath, filename))
                else:
                        message.attach(currencyfile(filepath, filename))
        return message

def currencyfile(currencyfile,filename):
        word = MIMEApplication(open(currencyfile, 'rb').read())
        word.add_header('Content-Disposition', 'attachment', filename=filename) #设置附件信息
        return word