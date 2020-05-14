from konlpy.tag import Komoran
import sys
import time
import math

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

def getUpNum(dic1, dic2):
    
    up_num = 0

    for ch in stc:
        if((ch in stc_dic) and (ch in read_dic)):
            up_num += stc_dic[ch] * read_dic[ch]
    return up_num

def getPercentList(read, percent, list_length):
    
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

argc = sys.argv

komoran = Komoran()

f = open(argc[1], 'rt')
list_length = -(int(argc[2]))

stc_dic = {}
read_dic = {}

stc = input()
start = time.time()
stc = komoran.morphs(stc)

percent_list = []

for ch in stc:
    if(ch not in stc_dic):
        stc_dic[ch] = 1
    else:
        stc_dic[ch] += 1

while True:

    percent = 0

    read = f.readline()
    if not read:
        break
    read1 = komoran.morphs(read)

    for ch in read1:
        if(ch not in read_dic):
            read_dic[ch] = 1
        else:
            read_dic[ch] += 1

    percent = cos_sim(getUpNum(stc_dic, read_dic), getUnderNum(stc_dic, read_dic))
    getPercentList(read, round(percent,2), list_length)


for i in range(list_length):
    if(i >= len(percent_list)):
        break
    print(percent_list[i][0].replace('\n',''),': ', percent_list[i][1],'%')

print("time: ", time.time() - start)
