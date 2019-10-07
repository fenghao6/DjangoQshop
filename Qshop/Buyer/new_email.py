import smtplib
from email.mime.text import MIMEText
subject="作业"
content="""
今天作业adb
"""
sender="fenghao6bu6@163.com"
recver="""1490932430@qq.com,
1041369205@qq.com,
2126579184@qq.com,
576492000@qq.com"""

password = "123456q"
message=MIMEText(content,"plain","utf-8")
message["Subject"]=subject
message["From"]=sender
message["To"]=recver

smtp=smtplib.SMTP_SSL("smtp.163.com",465)
smtp.login(sender,password)
smtp.sendmail(sender,recver.split(",\n"),message.as_string())
smtp.close()