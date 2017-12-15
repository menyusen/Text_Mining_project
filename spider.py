
# -*- coding: utf-8 -*- #---------------------------------------   
#   程序：URL地址随数字发生变化的网页抓取
#   日期：2016-8-18   
#   语言：Python 2.7
#   操作：输入带分页的地址，去掉最后面的数字，设置一下起始页数和终点页数。   
#   功能：下载对应页码内的所有页面并存储为html文件。   
#---------------------------------------      
import string, urllib2, sys  
import time
#定义爬虫函数   
def kz_spider(url_1,url_2,begin_page,end_page):     
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    for i in range(begin_page, end_page+1):  
        sName = string.zfill(i,5) + '.html'#自动填充成六位的文件名   
        print '正在下载第' + str(i) + '个网页，并将其存储为' + sName + '......'  
        f = open(sName,'w+')  
	req = urllib2.Request(
		url = url_1 + str(i)+url_2+str(i),
		headers = headers
	)
	m = urllib2.urlopen(req).read()  
        f.write(m)  
        f.close()
	time.sleep(5)  
   
#-------- 在这里输入参数 ------------------   
 
# 某一个网页的地址   
#bdurl = 'http://tieba.baidu.com/p/2296017831?pn='   
#iPostBegin = 1   
#iPostEnd = 10   

reload(sys) 
sys.setdefaultencoding( "utf-8" ) 

kzurl_1 = str(raw_input(u'请输入网页url地址第一个变化数字前的字符，不包含变化的数字：\n'))
kzurl_2 = str(raw_input(u'请输入网页url地址两个变化之间的字符，不包含变化的数字：\n'))    
begin_page = int(raw_input(u'请输入开始的页数：\n'))  
end_page = int(raw_input(u'请输入终点的页数：\n'))  
#-------- 在这里输入参数 ------------------   
#调用   
kz_spider(kzurl_1,kzurl_2,begin_page,end_page)
