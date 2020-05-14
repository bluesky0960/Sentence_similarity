from konlpy.tag import Kkma
from konlpy.tag import Hannanum
from konlpy.tag import Komoran
from konlpy.tag import Okt

import sys

kkma = Kkma()
hannanum = Hannanum()
komoran = Komoran()
okt = Okt()

analize_list = [kkma, hannanum, komoran, okt]
analize_list_name = ["Kkma_Class", "Hannanum_Class", "Komoran_Class", "Okt_Class"]

count_name = 0

f = open("sync_test2.txt",'rt')

read1 = f.readline()
read2 = f.readline()

for i in analize_list:

    dic = {}
    count = 0
    long_length = 0

    if len(i.morphs(read1)) >= len(i.morphs(read2)):
        long_length = len(i.morphs(read1))
    else:
        long_length = len(i.morphs(read2))

    for ch in range(len(i.morphs(read1))):
        if i.morphs(read1)[ch] not in dic:
            dic[i.morphs(read1)[ch]] = 0

    for ch in range(len(i.morphs(read2))):
        if i.morphs(read2)[ch] in dic:
            dic[i.morphs(read2)[ch]] += 1
            count += 1

    sorted_dic = sorted(dic.items(), key = (lambda x:x[1]),reverse = True)
    
    print(analize_list_name[count_name])
    print("중복이 많은 형태소 상위 3개: ", sorted_dic[0],', ',sorted_dic[1],', ',sorted_dic[2])
    print("총 중복 형태소 개수: ", count, "개")
    print("긴 문장의 형태소 개수: ", long_length, "개")
    print("유사도(총 중복 형태소 개수/긴 문장의 형태소 개수): ", round(count/long_length * 100, 2), "%")
    print("\n")
    count_name += 1

f.close()