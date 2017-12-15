# -*- coding: utf-8 -*-

import sys

def data_pre(Name_lable,Name_data):
    file_ind =open(Name_lable,'r')
    newfile=open(Name_data,'w')
    Com=[]
    for line in file_ind: #open('*.txt','r'):    
        item = line.strip()
        Com.append(item)
    file_ind.close()
    #print Com
    file_src = open('company_desc.total','r')  #company_desc.tota为包含各公司信息的数据库文件
    cnt = 0
    D={}
    D2={}
    for line in file_src: #open('company_desc.total'):
        #\t
        #V={};
        cnt += 1
        if cnt % 100000 == 1:
            print cnt
        items = line.strip().split("\t")
        #print items[0]
        for i in range(0,len(Com)):
            #print Com[i]
            #print items[0]
            if Com[i]==items[0]:  
                if len(items) < 3:
                    continue
                if len(items[1]) < 2:
                    continue
                if len(items[2]) < 10:
                    continue
                if not D.has_key(items[0]):
                    D[items[0]] = items[2]
                    D2[items[0]]=line
		    #newfile.writelines(line)
                    #print line
                elif len(items[2]) > len(D[items[0]]):
                    D[items[0]] = items[2]
		    D2[items[0]]=line
                    #newfile.writelines(line)
                    #print line
    for key in D2:
	newfile.writelines(D2[key])
	print D2[key]
    file_src.close()
    newfile.close()
    

###############################################################################
if __name__=="__main__":
    reload(sys)
    sys.setdefaultencoding( "utf-8" )
    begin_page = int(raw_input(u'请输入要抽取的开始lable_num数：\n'))
    end_page = int(raw_input(u'请输入要抽取的终点lable_num数：\n'))
    for lable_num in range(begin_page, end_page+1):
        Name_lable = str(lable_num) + '.txt'
        Name_data= str(lable_num) + 'd.txt'        
        print '正在抽取编号为' + str(lable_num)+'的行业数据，并将其存储为' + Name_data + '......'
        data_pre(Name_lable,Name_data)
