#!/usr/bin/python
#coding:utf8
'''
Created on 2015年6月19日

@author: Kenny
'''
import wx
import sys

class Frame(wx.Frame):
    def __init__(self,parent,id,title):
        print "Frame__init__"
        wx.Frame.__init__(self,parent,id,title)
        
class App(wx.App):
    def __init__(self,redirect = True,filename = None):
        print "App__init__"
        wx.App.__init__(self,redirect,filename)
        