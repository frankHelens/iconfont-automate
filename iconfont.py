from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

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
  def toHome (self):
    self.driver.get('https://www.iconfont.cn')
  #def getProject(self):
  
iconfont = Iconfont()
iconfont.weiboLogin()
# iconfont.login()
# iconfont.toHome()
