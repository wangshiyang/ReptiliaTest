#-*- coding:GBK -*-
'''
Created on 2012-11-4
@author: virusyang
'''

from Utility import PriorityQueue,Parser

import urllib2
import os
import string
import socket

def updatePriQueue(priQueue,url,beginurl):
    extraPrior = url.endswith('.html') and 20 or 0
    extraBeginUrl = beginurl in url and 5 or 0
    extraLevel = string.find(url,'/')
    schemeType = ['http://','ftp://','file://']
    flag = 0
    for type in schemeType:
        if url.startswith(type):
            flag = 1
    if not flag:
        return
    item = priQueue.getitem(url)
    if item:
        newitem = (item[0]+1+extraPrior+extraBeginUrl-extraLevel,item[1])
        priQueue.remove(item)
        priQueue.push(newitem)
    else:
        priQueue.push((1+extraPrior+extraBeginUrl-extraLevel,url))


def analyseHtml(url,html,priQueue,downlist,beginurl):
    p = Parser(html)
    for v in p.links:
        if not downlist.count(v):
            updatePriQueue(priQueue,v,beginurl)

       

def downloadUrl(id,url,priQueue,downlist,downFolder,beginurl):
    downFileName = downFolder+'/%d.html'%(id,)
    print 'downloading',url,'as',downFileName
   
    socket.setdefaulttimeout(2)
    try:
        fp = urllib2.urlopen(url)
    except:
        print '[failed]'
        return 0
    else:
        downlist.push(url)
        op = open(downFileName,"wb")
        try:
            html = fp.read()
        except:
            op.close()
            fp.close()
            print '[failed]'
            return 0
        else:
            print '[success]'
            op.write(html)
            op.close()
            fp.close()

            analyseHtml(url,html,priQueue,downlist,beginurl)
            return 1

def spider(beginurl,pages,downFolder):

    priQueue = PriorityQueue()            
    downlist = PriorityQueue()            
    priQueue.push((1,beginurl))
    i = 0
    while not priQueue.empty() and i <pages:
        k,url = priQueue.pop()
        if downloadUrl(i+1,url,priQueue,downlist,downFolder,beginurl):
            i+=1

    print '\nDownload',i,'pages.'

def main():
#    if(sys.argv[1]==None):
#        sys.argv[1]="csdn.net"
#    if(sys.argv[2]==None):
#        sys.argv[2]="2"
#    if(sys.argv[3]==None):
#        sys.argv[3]="E:\Downloads"
    
    url="http://bbs.csdn.net/"
    pages="2"
    dir="E:/Downloads"
    beginurl = url#sys.argv[1]        
    pages = string.atoi(pages)#sys.argv[2])       
    downloadFolder = dir#sys.argv[3]           
    if not os.path.isdir(downloadFolder):
        os.mkdir(downloadFolder)

    spider(beginurl,pages,downloadFolder)

if __name__ =='__main__':
    main()