#!/usr/bin/python
#coding:utf8
'''
Created on 2015年6月7日

@author: Administrator
'''

__author__ = 'Kenny'

import sys
import os
s = "请选择您需要的操作：\n添加前缀请按\"1\",取消前缀请按\"2\"\t"
s1 = '请输入前缀:\t'
s2 = '输入 \"y\" 或者 \"Y\" 重新输入或者输入其他前缀名 ?按任意键结束操作\t'
s3 = '请输入您要操作的文件路径:\t'

def addName(dir):
    #列出用户输入的路径下所有文件的文件名
    fileNames = os.listdir(dir)
    #提示用户输入前缀

    ex = raw_input(s1.decode('utf-8').encode('gbk'))
    #迭代出新的文件名
    for fileName in fileNames:
        newName = dir + '\\'+ ex +fileName
        print newName
        #使用新的文件名替换老的文件名
        os.rename(dir+'\\'+fileName,newName)
    print '*'*40
    print u'添加前缀完成！'
    
def reName(dir):
    #列出用户输入的路径下所有文件的文件名
    fileNames = os.listdir(dir)
    while True:
        ex = raw_input(s1.decode('utf-8').encode('gbk'))
        #获取前缀的长度
        x = len(ex)
        #判断前缀的长度，防止误输入
        if x <= 3: 
                print u'\"前缀太短了啊！\"'
                continue
                        
        for fileName in fileNames:
            
            if ex in fileName:
                #生成除过前缀长度以后的文件名
                newName = dir + '\\' + fileName[x:]
                print newName
                os.rename(dir+'\\'+fileName,newName)
            else:
                s5 = '这个前缀臣妾找不到啊！'
                print '\"%s\" -> '%ex + s5.decode('utf-8').encode('gbk')
                
        choice = raw_input(s2.decode('utf-8').encode('gbk'))
        if choice in ('y','Y'):
            pass
        else:
            print '*'*45+u'\n任务完成，再见！'
            break

if __name__ == '__main__':

    choice = int(raw_input(s.decode('utf-8').encode('gbk')))
    while True:
        dir = raw_input(s3.decode('utf-8').encode('gbk'))
        if os.path.isdir(dir):
            break
        else: print u'#### 错误！您输入的文件路径错误，请重新输入! ####'
    
    if choice == 1:
        addName(dir)
    elif choice == 2:
        reName(dir)
    else:print 'choose a right choice!!!'