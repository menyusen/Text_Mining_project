#---------------------------------import---------------------------------------
#encoding:utf-8
#import bs4
import sys,string;
#-----------------------------------------------------------------------------

def main():
    reload(sys)
    sys.setdefaultencoding( "utf-8" )
    begin_page = int(raw_input(u'请输入开始的lable_num数：\n'))
    end_page = int(raw_input(u'请输入终点的lable_num页数：\n'))
    for lable_num in range(begin_page, end_page+1):
        Name = str(lable_num) + 'ddd.txt'
        Companyfile=open(Name,'w')
        sName=str(lable_num)+'dd.txt'
        file=open(sName,'r')
	i=0
        for line in file:
	    i+=1
            #items = line.strip().split(" ")
            if(i%3==2):
                Companyfile.writelines(line)
        file.close()
        Companyfile.close()

###############################################################################
if __name__=="__main__":
    main();
