'''
@LastEditors: huangfengrui
@LastEditTime: 2019-11-21 16:56:05
@Author: huangfengrui
@Date: 2019-11-21 09:02:20
@Description: 
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from githubCode import GetGithubCode
import os
import shutil
import urllib.request
import zipfile
from readConfig import ReadConfig

class Iconfont:
  def __init__ (self):
    self.config = ReadConfig().getConfig()
    #设置Chrome的下载路径到本项目
    chromeOptions = webdriver.ChromeOptions()
    prefs = {
      'download.default_directory': os.getcwd()
    }
    chromeOptions.add_experimental_option('prefs', prefs)
    self.driver = webdriver.Chrome(chrome_options=chromeOptions)
    self.driver.implicitly_wait(10)
    self.checkOriginFile()
  # 微博登录 todo
  def weiboLogin (self):
    self.driver.get('https://api.weibo.com/oauth2/authorize?client_id=1283124999&redirect_uri=https%3A%2F%2Fwww.iconfont.cn%2Fapi%2Flogin%2Fweibo%2Fcallback&response_type=code&scope=users_show&state=plus-login#weibo_redirect')
  # github登录
  def githubLogin (self):
    self.driver.get('https://www.iconfont.cn/api/login/github')
    login_name = self.driver.find_element_by_id('login_field')
    login_password = self.driver.find_element_by_id('password')
    login_name.send_keys(self.config['userName'])
    login_password.send_keys(self.config['password'])
    login_submit = self.driver.find_element_by_class_name('btn')
    login_submit.click()
    sleep(1)
    self.checkLogin()
  # 判断登录是否需要邮箱验证
  def checkLogin(self):
    url = self.driver.current_url
    print('current_url', url)
    if (url == 'https://github.com/sessions/verified-device'):
      sleep(5)
      self.setVerified()
    self.toProject()
  # 输出邮箱提供的验证码
  def setVerified (self):
    code = GetGithubCode().getCode()
    print('邮箱验证码:', code)
    verifiedInput = self.driver.find_element_by_id('otp')
    verifiedSubmit = self.driver.find_element_by_class_name('btn-primary')
    verifiedInput.send_keys(code)
    verifiedSubmit.click()
  # 跳转至首页
  def toHome (self):
    self.driver.get('https://www.iconfont.cn')
  # 跳转至项目页面
  def toProject (self):
    self.toHome()
    iconManager = self.driver.find_element_by_xpath('//*[@id="magix_vf_header"]/header/div/nav/ul/li[3]')
    ActionChains(self.driver).move_to_element(iconManager).perform()
    projectButton = self.driver.find_element_by_xpath('//*[@id="magix_vf_header"]/header/div/nav/ul/li[3]/ul[@class="head-dropdown"]/li[3]')
    projectButton.click()
  # 下载项目
  def downLoadProject(self):
    projectLink = self.driver.find_element_by_xpath("//span[contains(text(),'%s')]" % self.config['iconProject'])
    projectLink.click()
    sleep(1)
    downloadButton = self.driver.find_element_by_partial_link_text('下载至本地')
    downloadButton.click()
    sleep(3)
    self.driver.quit()
  # 关闭浏览器
  def exit(self):
    self.driver.quit()
  # 设置iconfont
  def setIconfont (self):
    root_path = os.getcwd()
    # 目标文件
    targe_path = root_path + "\\iconfont"
    iconfontFile = zipfile.ZipFile(root_path + '\\download.zip', "r")
    filePath = iconfontFile.namelist()[0]
    fileTypeNames = ['woff', 'ttf', 'svg', 'css', 'eot']
    for type in fileTypeNames:
      fileName = filePath + 'iconfont.%s' % type
      iconfontFile.extract(fileName, root_path + "\\iconfont")
    self.move_file('./iconfont/%s' % filePath, root_path + "\\iconfont")
    os.rmdir(targe_path + "\\%s" % filePath)
  # 移动文件
  def move_file(self, src_dir, target_dir):
    if not os.path.exists(target_dir):
      os.mkdir(target_dir)
    count = 0
    for item in os.listdir(src_dir):
      src_name = os.path.join(src_dir,item)
      target_name = os.path.join(target_dir,item)
      count += 1
      shutil.move(src_name,target_name)
      if count >= 20000:
        break
  # 判断源文件是否存在，存在则删除
  def checkOriginFile (self):
    if (os.path.exists('download.zip')):
      os.remove('download.zip')
iconfont = Iconfont()
iconfont.toHome()
sleep(9999)
# iconfont.githubLogin()
# iconfont.downLoadProject()
# iconfont.setIconfont()
