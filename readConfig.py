'''
@LastEditors: huangfengrui
@LastEditTime: 2019-11-21 14:33:11
@Author: huangfengrui
@Date: 2019-11-21 14:22:25
@Description: 
'''
import json

class ReadConfig:
  def getConfig (self):
    f = open('config.json','r', encoding='utf-8').read()
    temp = json.loads(f)
    return temp
