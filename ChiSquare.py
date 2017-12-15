import os
import sys

# get words in input file
def get_words(input):
    W = {}
    #print input
    for line in open(input):
        items = line.strip().split(" ")
        for item in items:
            if not item in W:
                W[item] = 0
            W[item] += 1
    return W

# to get the word list from the input_list, stop words not included
def get_wordlist(input_list, stopword):
    W_stop = get_words(stopword)
    W_input = {}
    for line in open(input_list):
        W = get_words(line.strip())
        for key in W:
            # remove stop words
            if key in W_stop:
                continue
            if not key in W_input:
                W_input[key] = W[key]
            else:
                W_input[key] += W[key]
                
    return W_input

def filter_freq(W, freq):

    W_fil = {}
    for w in W:
        if W[w] < freq:
            continue
        W_fil[w] = W[w]
    return W_fil

# to comput Chi_square statistics 
def Chi_square(C1, num1, C2, num2):
    Chi = {}
    for term in C1:
        # number of term appears in class C1
        A = C1[term]
        # number of term appears in class C2 (not C1)
        B = C2[term]
        C = num1 - A
        D = num2 - B
        if A+B ==0 or C+D ==0:
            print term
            print A,B,C,D
            continue
        Chi[term] = (A*D - B*C) * (A*D - B*C) * 1.0 / (A+B) / (C+D)
    return Chi

# return the times word t appears (one line/ company) in class c
def appear_count(word_dict, file):
    D = {}
    '''
    for line in open(word_dict_file):
        items = line.strip().split(" ")
        D[items[0]] = 0
    '''
    for w in word_dict:
        D[w] = 0
    
    cnt = 0
    for line in open(file):
        if cnt % 100 == 1:
            print cnt
        cnt += 1
        items = line.strip().split(" ")
        for key in D:
            if key in items:
                D[key] += 1 
    
    return D, cnt    

def Chi_square(C1, num1, C2, num2):
    Chi = {}
    for term in C1:
        # number of term appears in class C1
        A = C1[term]
        # number of term appears in class C2 (not C1)
        B = C2[term]
        C = num1 - A
        D = num2 - B
        if A+B ==0 or C+D ==0:
            print term
            print A,B,C,D
            continue
        Chi[term] = (A*D - B*C) * (A*D - B*C) * 1.0 / (A+B) / (C+D)
    return Chi

# d1 + d2 +...
def dict_plus(dict_list):
    D_all = {}
    for D in dict_list:
        for key in D:
            if not key in D_all:
                D_all[key] = 0
            D_all[key] += D[key]
    return D_all
   
# dictA - dictB
def dict_minus(dictA, dictB):
    D_minus = {}
    for key in dictA:
        if not key in dictB:
            D_minus[key] = dictA[key]
        else:
            D_minus[key] = dictA[key] - dictB[key]
    return D_minus


def list_plus(N_list):
    sum = 0
    for ele in N_list:
        sum += ele
    return sum

def get_filename(input_list):
    Name = []
    for line in open(input_list):
        items = line.strip().split("/")
        Name.append(items[-1])
    return Name

# print dict
def print_dict(D, output):
    fout = open(output, 'w')
    for key in D:
        print >> fout, key, D[key]
    fout.close()

# to compute chi_square statistics of all input files    
def compute_chi_square(input_list, V, output_dir):
    D_list = []
    Num_list = []
    Name = get_filename(input_list)
    print Name
   
    print "appear count"
    for line in open(input_list):
        print line.strip()
        [D, num] = appear_count(V, line.strip()) 
        D_list.append(D)
        Num_list.append(num)
    
    D_all = dict_plus(D_list)
    Num_all = list_plus(Num_list)

    print "begin to comput Chi_square"
    for i in range(len(D_list)):
        
        D1 = D_list[i]
        num1 = Num_list[i]
        D2 = dict_minus(D_all, D1)
        num2 = Num_all - num1

        Chi = Chi_square(D1, num1, D2, num2)
        output = output_dir + "/" + Name[i]
        print output 
        print_dict(Chi, output)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print "Usage: python ChiSquare.py input_list stopword_file output_dir"
        exit(0)

    input_list = sys.argv[1]
    stopword_file = sys.argv[2]
    output_dir = sys.argv[3]

    print "get wordlist"
    V = get_wordlist(input_list, stopword_file)
    #V = get_wordlist("../companydata2/66ddd.txt", "../all.stop")
    print "get wordlist done"
    
    compute_chi_square(input_list, V, output_dir)
    #compute_chi_square("../companydata2/66ddd.txt", V, "..")



