import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender='798356548@qq.com'    # 发件人邮箱账号
my_pass = 'vquowwrdxopybfhf'              # 发件人邮箱密码(当时申请smtp给的口令)
my_user='249132797@qq.com'      # 收件人邮箱账号，我这边发送给自己

def mail():
  ret=True
  try:
    msg=MIMEText('用python发送短信消息给你的测试内容,请勿拉黑', 'plain', 'utf-8')
    msg['From']=formataddr(["Frank", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To']=formataddr(["未确认э式×", my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject']="邮件主题-测试"                # 邮件的主题，也可以说是标题
    server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
    print('1', server)
    server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    print('2', server)
    server.sendmail(my_sender,[my_user], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    print('3', server)
    server.quit()# 关闭连接
  except Exception:# 如果 try 中的语句没有执行，则会执行下面的 ret=False
    ret=False
  return ret

ret = mail()
if ret:
  print("邮件发送成功")
else:
  print("邮件发送失败")

