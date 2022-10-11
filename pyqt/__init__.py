
import os
import sys
'''
print(__file__)#获取当前程序路径，注意：这里打印出来的路径为相对路径
#动态获取绝对路径
print(os.path.abspath(__file__)) #这才是当前程序绝对路径
print(os.path.dirname(os.path.abspath(__file__))) #当前程序上一级目录，其中dirname返回目录名，不要文件名
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#当前程序上上一级目录
'''
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #当前程序上上一级目录，这里为mycompany
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR) #添加环境变量