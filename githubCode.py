'''
@LastEditors: huangfengrui
@LastEditTime: 2019-11-21 16:47:55
@Author: huangfengrui
@Date: 2019-11-21 09:02:20
@Description: 
'''
import poplib
import re
from readConfig import ReadConfig

class GetGithubCode:
  def __init__(self):
    config = ReadConfig().getConfig()
  # 此函数通过使用poplib实现接收邮件
  def getEmailContent(self):
    # 要进行邮件接收的邮箱。改成自己的邮箱
    email_address = config.email
    # 要进行邮件接收的邮箱的密码。改成自己的邮箱的密码
    email_password = config.emailPassword
    # 邮箱对应的pop服务器，也可以直接是IP地址
    # 改成自己邮箱的pop服务器；qq邮箱不需要修改此值
    pop_server_host = "pop.qq.com"
    # 邮箱对应的pop服务器的监听端口。改成自己邮箱的pop服务器的端口；qq邮箱不需要修改此值
    pop_server_port = 995

    try:
      # 连接pop服务器。如果没有使用SSL，将POP3_SSL()改成POP3()即可其他都不需要做改动
      email_server = poplib.POP3_SSL(host=pop_server_host, port=pop_server_port, timeout=10)
      print("pop3----connect server success, now will check username")
    except:
      print("pop3----sorry the given email server address connect time out")
      exit(1)
    try:
      # 验证邮箱是否存在
      email_server.user(email_address)
      print("pop3----username exist, now will check password")
    except:
      print("pop3----sorry the given email address seem do not exist")
      exit(1)
    try:
      # 验证邮箱密码是否正确
      email_server.pass_(email_password)
      print("pop3----password correct,now will list email")
    except:
      print("pop3----sorry the given username seem do not correct")
      exit(1)

    # 邮箱中其收到的邮件的数量
    print(email_server.list())
    email_count = len(email_server.list()[1])
    if (email_count == 0):
      exit('邮箱数量为0')
      return
    # 通过retr(index)读取第index封邮件的内容；这里读取最后一封，也即最新收到的那一封邮件
    resp, lines, octets = email_server.retr(email_count)
    # lines是邮件内容，列表形式使用join拼成一个byte变量
    self.email_content = b'\r\n'.join(lines)
    # 再将邮件内容由byte转成str类型
    self.email_content = self.email_content.decode()
    # 关闭连接
    email_server.close()
  # 获取code
  def getCode (self):
    self.getEmailContent()
    pattern = re.compile(r'Verification code: \d+')   # 查找数字
    code = pattern.findall(self.email_content)[0].split('Verification code: ')[1]
    return code
