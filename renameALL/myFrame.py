#!/usr/bin/python
#coding:utf8
'''
Created on 2015年6月7日

@author: Administrator
'''
import wx
import renameALL

class myApp(wx.App):
    def OnInit(self):
#         框架
        frame = wx.Frame(parent = None,
                         title = u'增删前缀小工具' ,
                         size = (500,400) 
                                             
                         )
#         面板
        panel = wx.Panel(frame, -1)
#         增加按钮
        self.add_button = wx.Button(parent = panel,
                               label = u'增加',
                               pos = (100,200),
                               size = (60,25)
                               )
        self.add_button.SetBackgroundColour('green')
        self.add_button.Bind(wx.EVT_BUTTON, self.addbutton)
#         删除按钮
        self.remove_button = wx.Button(parent = panel,
                                  label = u'删除',
                                  pos = (200,200),
                                  size = (60,25)
                                  )
        self.remove_button.SetBackgroundColour('red')
        self.remove_button.Bind(wx.EVT_BUTTON, self.removebutton)
#         静态提示文本
        text1 = wx.StaticText(parent = panel,
                              id = -1,
                              label = u'文件路径',
                              pos = (5,5),
                              size = (80,20),
                            style = wx.ALIGN_CENTER                              
                              )
        text1.SetForegroundColour('white')
        text1.SetBackgroundColour('black')
        text2 = wx.StaticText(parent = panel,
                              id = -1,
                              label = u'前    缀',
                              pos = (5,30),
                              size = (80,20),
                            style = wx.ALIGN_CENTER  
                                                        
                              )
        text2.SetForegroundColour('red')
        text2.SetBackgroundColour('green')
#         增加单行文本框
        path = wx.TextCtrl(parent = panel,
                           id = -1, 
                           pos = (85,5),
                           size = (200,20)
                           )
        profix = wx.TextCtrl(parent = panel,
                           id = -1, 
                           pos = (85,30),
                           size = (200,20)
                           )
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        frame.SetBackgroundColour('white')
        frame.Show()
        return True
    def addbutton(self,event):
        print 'add button'
    def removebutton(self,event):
        print 'remove button'
        
app = myApp()
app.MainLoop()