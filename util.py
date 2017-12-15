#coding:utf-8 
import os
import sys
import random


def load_list(file):
    L = []
    for line in open(file):
        L.append(line.strip())
    return L

def load_dict(file):
    D = {}
    for line in open(file):
        D[line.strip()] = 1
    return D

def merge_company_desc(D, comp_desc, col_idx, output):
    cnt = 0
    fout = open(output, 'w')
    for line in open(comp_desc):
        items = line.strip().split("\t")
        key = items[col_idx-1]
        if key in D:
            print >> fout, line.strip() 
        cnt += 1
        if cnt % 1000000 == 1:
            print cnt
    
    fout.close()


def longest(file):
    D = {}
    T = {}
    for line in open(file):
        items = line.strip().split("\t")
        if len(items) < 3:
            continue
        if len(items[1]) < 2:
            continue
        if len(items[2]) < 10:
            continue
        if not D.has_key(items[0]):
            D[items[0]] = items[2]
            T[items[0]] = items[1]
        elif len(items[2]) > len(D[items[0]]):
            D[items[0]] = items[2]
            T[items[0]] = items[1]

    return D, T

def longest_lessmemory(file, output):
    D = {}
    cnt = 0
    for line in open(file):
        cnt += 1
        if cnt % 100000 == 1:
            print cnt
        items = line.strip().split("\t")
        if len(items) < 3:
            continue
        if len(items[1]) < 2:
            continue
        if len(items[2]) < 10:
            continue
        if not D.has_key(items[0]) or len(items[2]) > D[items[0]]:
            D[items[0]] = len(items[2])
           
    cnt = 0 
    fout = open(output, 'w')
    for line in open(file):
        cnt += 1
        if cnt % 100000 == 1:
            print cnt
        items = line.strip().split("\t")
        if len(items) < 3:
            continue
        if len(items[1]) < 2:
            continue
        if len(items[2]) < 10:
            continue
        key = items[0]
        length = len(items[2])
        if D.has_key(key) and D[key] == length:
            print >> fout, line.strip()
            D.pop(key)
        
    fout.close()

def sample(input, output, num):
    cnt = 0
    for line in open(input):
        cnt += 1
        if cnt % 1000000 == 1:
            print cnt
    
    L = [i for i in range(1,cnt+1)]
    random.shuffle(L)

    D = {}
    for i in range(num):
        D[L[i]] = 1

    cnt = 0
    fout = open(output, 'w')
    for line in open(input):
        cnt += 1
        if cnt % 1000000 == 1:
            print cnt
        if not cnt in D:
            continue
        items = line.strip().split("\t")
        # begin
        if len(items) < 3:
            continue
        if len(items[2]) < 50:
            continue
        # end
        print >> fout, line.strip()
        D.pop(cnt)

def remain_seg(input, output):
    fout = open(output, 'w')
    cnt = 0
    for line in open(input):
        cnt += 1
        if cnt % 3 == 2:
            #print >> fout, line.strip()
            print >> fout, line[:-1]
    fout.close()

def stop_uniq(stop_file, input, output):
    # stop word set
    S = {}
    for line in open(stop_file):
        S[line[:-1]] = 1
    
    fout = open(output, 'w') 
    for line in open(input):
        items = line.strip().split(" ")

        D = {}
        for item in items:
            if item in S:
                continue
            D[item] = 1

        print >> fout, " ".join(D.keys())
        D.clear()

    fout.close()

# tongji cipin
def word_count(input, output):
    
    D = {}
    for line in open(input):
        items = line.strip().split(" ")
        for item in items:
            if not D.has_key(item):
                D[item] = 1
            else:
                D[item] += 1
   
    fout = open(output, 'w') 
    for key in sorted(D.items(), lambda x, y: cmp(x[1], y[1]), reverse=True):
        print >> fout, key[0] + " " + str(key[1])
    '''
    for key in D:
        print key, D[key]
    '''

# return the times word t appears (one line/ company) in class c
def appear_count(word_dict_file, file):
    D = {}
    for line in open(word_dict_file):
        items = line.strip().split(" ")
        D[items[0]] = 0

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

def load_vocabulary(voc_file):
    V = {}
    for line in open(voc_file):
        items = line.strip().split(" ")
        if len(items) == 2:
            V[items[0]] = items[1]
        else:
            V[items[0]] = 1
    return V


    
