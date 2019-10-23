from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from githubCode import GetGithubCode

class Iconfont:
  def __init__ (self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(10)
  def weiboLogin (self):
    self.driver.get('https://api.weibo.com/oauth2/authorize?client_id=1283124999&redirect_uri=https%3A%2F%2Fwww.iconfont.cn%2Fapi%2Flogin%2Fweibo%2Fcallback&response_type=code&scope=users_show&state=plus-login#weibo_redirect')
  def githubLogin (self):
    self.driver.get('https://www.iconfont.cn/api/login/github')
    login_name = self.driver.find_element_by_id('login_field')
    login_password = self.driver.find_element_by_id('password')
    login_name.send_keys('frankHelens')
    login_password.send_keys('fr7983565480.')
    login_submit = self.driver.find_element_by_class_name('btn')
    login_submit.click()
    sleep(5)
    self.checkLogin()
  def checkLogin(self):
    url = self.driver.current_url
    print('current_url', url)
    if (url == 'https://github.com/sessions/verified-device'):
      self.setVerified()
  # 输出邮箱提供的验证码
  def setVerified (self):
    code = GetGithubCode().getCode()
    print(code)
    verifiedInput = self.driver.find_element_by_id('otp')
    verifiedSubmit = self.driver.find_element_by_class_name('btn-primary')
    verifiedInput.send_keys(code)
    verifiedSubmit.click()
  def toHome (self):
    self.driver.get('https://www.iconfont.cn')
  #def getProject(self):
  
iconfont = Iconfont()
# iconfont.weiboLogin()
iconfont.githubLogin()
# iconfont.toHome()
