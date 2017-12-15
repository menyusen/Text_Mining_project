#---------------------------------import---------------------------------------
#encoding:utf-8
import re,BeautifulSoup,sys,string;
from BeautifulSoup import BeautifulSoup;
#-----------------------------------------------------------------------------

def main():
    reload(sys)
    sys.setdefaultencoding( "utf-8" )
    #begin_page = int(raw_input(u'请输入开始的页数：\n'))
    #end_page = int(raw_input(u'请输入终点的页数：\n'))
    num = int(raw_input(u'请输入网页解析的数目：\n'))
    #for i in range(begin_page, end_page+1):
    #Companyfile=open('name','w')
    #Companyfile.close()
    for i in range(1, num+1):
        sName = string.zfill(i,5) + '.html'#自动填充成五位的文件名   
        file = open(sName,'r')
	sNamex = string.zfill(i,5) + 'x.html'
        newfile=open(sNamex,'w')
	lineNum = 0
	for line in file.readlines()[500:]:
	    newfile.writelines(line)
	file.close()
	newfile.close()
	newfile=open(sNamex,'rw+')
	#Companyfile=open('name','rw+')
	respHtml=newfile.read()
	songtasteHtmlEncoding = "GB2312";
	soup = BeautifulSoup(respHtml, fromEncoding=songtasteHtmlEncoding);
	for a in soup.findAll(name='a',attrs={'ka':re.compile("title$"),'href':True,'target':True,'class':None}):
            print a.text
	   # Companyfile.writelines(a.text)
	newfile.close()
	#Companyfile.close()
	
###############################################################################
if __name__=="__main__":
    main();
