# -*- coding:utf-8 -*-
import urllib
import urllib2

page = 1
url = 'http://store.nike.com/cn/zh_cn/pd/kd-8-ep-%E7%AF%AE%E7%90%83%E9%9E%8B/pid-10287976/pgid-10314135?cp=cnns_soc_071115_m_bbkd8_si01/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason