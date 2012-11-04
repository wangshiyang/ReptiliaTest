'''
Created on 2012-11-4

@author: virusyang
'''
import bisect
import re

class PriorityQueue(list):
    def __init__(self):
        list.__init__(self)
        self.map = {}

    def push(self,item):
        if self.count(item) == 0:
            bisect.insort(self,item)
            self.map[item[1]] = item

    def pop(self):
        r = list.pop(self)
        del self.map[r[1]]
        return r

    def getitem(self,url):
        if self.map.has_key(url):
            return self.map[url]
        else:
            return None

    def empty(self):
        return len(self) == 0

    def remove(self,item):
        list.remove(self,item)
        del self.map[item[1]]

    def count(self,item):
        if len(self) == 0:
            return 0
        left = 0
        right = len(self)-1
        mid = -1
        while left<=right:
            mid = (left+right)/2
            if self[mid] < item:
                left = mid+1
            elif self[mid] >item:
                right= mid-1
            else:
                break
        return self[mid] == item and 1 or 0
       
       

class Parser():
    def __init__(self,html):
        self.links = []
        re_pattern = "\shref=[\"']?([^\"'\s>]+)[\"'\s>]"
        re_href = re.compile(re_pattern,re.IGNORECASE)
        for m in re_href.finditer(html):
            href = m.group(1)
            self.links.append(href)