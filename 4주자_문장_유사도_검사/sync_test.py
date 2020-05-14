from multiprocessing import Process
from konlpy.tag import Komoran
from konlpy.tag import Okt
from konlpy.tag import Kkma

import time
import os
import sys
import math

start_time = time.time()

def cos_sim(A,B):
    return A/B * 100

def getUnderNum(dic1, dic2):
    
    under_num1 = 0
    under_num2 = 0

    for val in dic1.values():
        under_num1 += val**2

    for val in dic2.values():
        under_num2 += val**2

    return math.sqrt(under_num1 * under_num2)

def getUpNum(dic1, dic2, input_stc):
    
    up_num = 0

    for ch in input_stc:
        if((ch in dic1) and (ch in dic2)):
            up_num += dic1[ch] * dic2[ch]
    return up_num

def getPercentList(read, percent, list_length, percent_list):
    
    while True:
        if(len(percent_list) == list_length):
            if(percent >= percent_list[list_length - 1][1]):
                percent_list[list_length - 1] = [read,percent]
                percent_list.sort(key = lambda x:x[1],reverse = True)
                break
            else:
                break
        else:
            percent_list.append([read, percent])
            percent_list.sort(key = lambda x:x[1], reverse = True)
            break
    return percent_list

def analize_text(dict_stc,input_stc, an_type, percent_list):

    proc = os.getpid()
    
    if an_type == '-okt':
        konlpy_type = Okt()
    elif an_type == '-komoran':
        konlpy_type = Komoran()
    elif an_type == '-kkma':
        konlpy_type = Kkma()
    else:
        konlpy_type = Komoran()

    read_dic = {}
    input_dic = {}
    
    input_stc = konlpy_type.morphs(input_stc)

    for ch in input_stc:
        if(ch not in input_dic):
            input_dic[ch] = 1
        else:
            input_dic[ch] += 1

    for i in range(len(dict_stc)):
        percent = 0
        read1 = konlpy_type.morphs(dict_stc[i])
        for ch in read1:
            if(ch not in read_dic):
                read_dic[ch] = 1
            else:
                read_dic[ch] += 1

        percent = cos_sim(getUpNum(input_dic, read_dic, input_stc), getUnderNum(input_dic, read_dic))
        getPercentList(dict_stc[i], round(percent,2), 2, percent_list)
        read_dic = {}

    print("Process ID: ", proc)

    for i in range(2):
        if(i >= len(percent_list)):
            break
        print(percent_list[i][0].replace('\n',''),': ', percent_list[i][1],'%')

if __name__ == '__main__':

    percent_list = []

    read1 = []
    read2 = []
    read3 = []
    read4 = []

    dict_read = [read1, read2, read3, read4]
    dict_num = 0

    argc = sys.argv

    f = open(argc[1], 'rt')
    an_type = argc[2]
    input_stc = input("입력 문장: ")

    while True:
        read = f.readline().replace('\n','')

        if read == '':
            read = f.readline().replace('\n','')

        if not read: 
            break

        dict_read[dict_num].append(read)
        dict_num += 1

        if(dict_num > 3):
            dict_num = 0

    procs = []
    proc1 = Process(target = analize_text, args = (read1, input_stc, an_type, percent_list))
    proc2 = Process(target = analize_text, args = (read2, input_stc, an_type, percent_list))
    proc3 = Process(target = analize_text, args = (read3, input_stc, an_type, percent_list))
    proc4 = Process(target = analize_text, args = (read4, input_stc, an_type, percent_list))

    procs.append(proc1)
    procs.append(proc2)
    procs.append(proc3)
    procs.append(proc4)

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()

    print("--- %s seconds ---" %(time.time()-start_time))
    f.close()
