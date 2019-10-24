from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from githubCode import GetGithubCode
import os
import urllib.request

class Iconfont:
  def __init__ (self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(10)
  # 微博登录 todo
  def weiboLogin (self):
    self.driver.get('https://api.weibo.com/oauth2/authorize?client_id=1283124999&redirect_uri=https%3A%2F%2Fwww.iconfont.cn%2Fapi%2Flogin%2Fweibo%2Fcallback&response_type=code&scope=users_show&state=plus-login#weibo_redirect')
  # github登录
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
  # 判断登录是否需要邮箱验证
  def checkLogin(self):
    url = self.driver.current_url
    print('current_url', url)
    if (url == 'https://github.com/sessions/verified-device'):
      self.setVerified()
    else:
      # self.toHome()
      self.toProject()
  # 输出邮箱提供的验证码
  def setVerified (self):
    code = GetGithubCode().getCode()
    print(code)
    verifiedInput = self.driver.find_element_by_id('otp')
    verifiedSubmit = self.driver.find_element_by_class_name('btn-primary')
    verifiedInput.send_keys(code)
    verifiedSubmit.click()
  # 跳转至首页
  def toHome (self):
    self.driver.get('https://www.iconfont.cn')
  # 跳转至项目页面
  def toProject (self):
    self.driver.get('https://www.iconfont.cn/manage/index?manage_type=myproject')
  # 下载项目
  def downLoadProject(self):
    downloadUrl = self.driver.find_element_by_partial_link_text('下载至本地')
    print('downloadUrl', downloadUrl)
    # 该目录下创建一个文件夹iconfont，判断没有文件夹就创建
    if not os.path.exists('iconfont'):
      os.mkdir('logoImg')
    # 跳到文件夹
    os.chdir('logoImg')
    try:
      urllib.request.urlretrieve(downloadUrl, 'iconfont')
    except:
      print('404:%s' % url)
    else:
      print('已下载:%s' % url)
    os.chdir('..')
iconfont = Iconfont()
# iconfont.weiboLogin()
iconfont.githubLogin()
iconfont.downLoadProject()
# iconfont.toHome()
