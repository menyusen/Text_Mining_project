#coding:utf-8 
import os
import sys
import random
import math
import util

# return the number of total words (included in the vocabulary) in input file
def word_num(voc_file, input):
    V = util.load_vocabulary(voc_file)
    num = 0
    for line in open(input):
        items = line.strip().split(" ")
        for item in items:
            if V.has_key(item):
                num += 1
    return num

# compute the prior probability
def Prior(voc_file, inputs_list):
    Num = []
    for input in inputs_list:
        Num.append(word_num(voc_file, input))
    
    sum = 0.0
    for num in Num:
       sum += num
    
    P = []
    for num in Num:
        P.append(num / sum)
    return P

# to compute conditional probablility
def CondProb(voc_file, inputs_list):
    # the num of words in each input file
    Num = []
    for input in inputs_list:
        Num.append(word_num(voc_file, input))

    # the length of the vocabulary
    V = util.load_vocabulary(voc_file)
    V_len = len(V)

    T = []    
    for input in inputs_list:
        D = {}
        for key in V:
            D[key] = 0

        for line in open(input):
            items = line.strip().split(" ")
            for item in items:
                if D.has_key(item):
                    D[item] += 1
                    #print item
                    #print D[item]
        T.append(D)

    CondP = {}
    for key in V:
        CondP[key] = []
    for c in range(len(T)):
        Tc = T[c]
        Nc = Num[c]
        for word in Tc:
            condprob = (Tc[word] + 1) * 1.0 / (Nc + V_len)
            CondP[word].append(condprob)

    return CondP

# to save model
def save_model(Prior, CondP, model_file):
    fout = open(model_file, 'w')

    strP = []
    for prior in Prior:
        strP.append(str(prior)) 
    print >> fout, " ".join(strP)

    for key in CondP:
        newline = []
        newline.append(key)
        for ele in CondP[key]:
            newline.append(str(ele))
        print >> fout, " ".join(newline)
    fout.close()    

# to load model
def load_model(model_file):
    Prior = []
    CondP = {}
    begin = 1
    for line in open(model_file):
        items = line.strip().split(" ")
        if begin == 1:
            for item in items:
               Prior.append(item)
            begin = 0
            continue
        key = items[0]
        CondP[key] = items[1:]
    return Prior, CondP

# to predict test file
def predict(test_file, result_file, model_file):
    fout = open(result_file, 'w')
    [P, CondP] = load_model(model_file) 
    for line in open(test_file):
        items = line.strip().split(" ")
        Score = []
        for c in range(len(P)):
            score = math.log(float(P[c]))
            for item in items:
                if not CondP.has_key(item):
                    continue
                score += math.log(float(CondP[item][c]))
            Score.append(str(score))
        print >> fout, " ".join(Score)
    fout.close()     
 
def eval(result_file):
    Num = 0
    Num1 = 0
    L=[710,947,1613,2282,2617,2803,3345,3562,4346,4736,5073,5780,5984,6378,6511,6720]
    for line in open(result_file):
        Num += 1
	if Num<=int(L[0]):
	    lable_num=1
	elif Num<=int(L[1]):
	    lable_num=2
	elif Num<=int(L[2]):
            lable_num=3
	elif Num<=int(L[3]):
            lable_num=4
	elif Num<=int(L[4]):
            lable_num=5
        elif Num<=int(L[5]):
            lable_num=6
        elif Num<=int(L[6]):
            lable_num=7
        elif Num<=int(L[7]):
            lable_num=8
        elif Num<=int(L[8]):
            lable_num=9
        elif Num<=int(L[9]):
            lable_num=10
        elif Num<=int(L[10]):
            lable_num=11
        elif Num<=int(L[11]):
            lable_num=12
        elif Num<=int(L[12]):
            lable_num=13
        elif Num<=int(L[13]):
            lable_num=14
        elif Num<=int(L[14]):
            lable_num=15
        elif Num<=int(L[15]):
            lable_num=16
	k=0
        items = line.strip().split(" ")
	for item in items:
	    if float(items[lable_num-1])>=float(item):
		k+=1
        if k>=14:#float(items[0]) > float(items[1]):
            Num1 += 1
	else:
	    print Num,line
    print Num1 * 100.0 / Num
    
def recall_precise(file,lable_num,sample_num):

    jr_right = 0
    jr_wrong = 0
    njr_right = 0
    njr_wrong = 0
 
    cnt = 0
    for line in open(file):
        cnt += 1
        items = line.strip().split(" ")
	k=0
        items = line.strip().split(" ")
        for item in items:
            if float(items[lable_num-1])>=float(item):
                k+=1
        if k>=14:#float(items[0]) > float(items[1]):
            if cnt <= sample_num:
                jr_right += 1
            else:
                jr_wrong += 1
        elif cnt <= sample_num:
            njr_wrong += 1
        else:
            njr_right += 1 
    recall = jr_right * 100.0 / (jr_right + njr_wrong)
    precise = jr_right * 100 / (jr_right + jr_wrong)
    print jr_right, jr_wrong, njr_right, njr_wrong            
    print recall, precise      
     
def train_v1():        
    input1 = "../data/jinrong/jinrong.desc.uniq.seg"
    input2 = "../data/not_jinrong/not_jinrong.uniq.sample.seg"
    #voc_file = "../data/wordcount.4"
    voc_file = "../data/word_count/wordcount_2/chi.jr.wdcnt.2.sort.1.1w"
    output = "../model/wordcount_2/chi.0811.1.1w.model"

    inputs = []
    inputs.append(input1)
    inputs.append(input2)

    P = Prior(voc_file, inputs)
    CondP = CondProb(voc_file, inputs)
    save_model(P, CondP, output)

def train(training_list, voc_file, model_file):

    inputs = []
    for line in open(training_list):
        inputs.append(line.strip())

    P = Prior(voc_file, inputs)
    CondP = CondProb(voc_file, inputs)
    save_model(P, CondP, model_file)


if __name__ == '__main__':

    if len(sys.argv) < 5:
        print "Usage: python NaiveBayes.py train datalist voc_file model_file"
	print "Usage: =================or================"
        print "Usage: python NaiveBayes.py predict test_file model_file result_file"
        exit(0)

    if sys.argv[1] == "train":
        datalist = sys.argv[2]
        voc_file = sys.argv[3]
        model_file = sys.argv[4]
        train(datalist, voc_file, model_file)
    
    #test_file = "../data/for_test/company_desc.total.3.sample.seg"
    #result_file = "../data/for_test/wordcount_2/chi.0811.1.1w.res"
    if sys.argv[1] == "predict":
        test_file = sys.argv[2]
        model_file = sys.argv[3]
        result_file = sys.argv[4]
        
	#lable_num = int(raw_input('please input the number of lable：\n'))
	#model_file = "../model/wordcount_2/chi.0811.1w.model"
        predict(test_file, result_file, model_file)
        eval(result_file)
	#sample_num=0
	#for line in open(test_file,'r'):
	#    sample_num+=1
        #recall_precise(result_file,lable_num, sample_num)
    


