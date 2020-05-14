import sys

def getBigram(read1, read2):

    dic = {}
    dic2 = {}

    dic_length = 0
    dic2_length = 0

    for i in range(len(read1)):
        if(i+1 >= len(read1)):
            break
        else:
            dic[read1[i]+read1[i+1]] = 0
            dic_length +=1

    for i in range(len(read2)):
        if(i+1>=len(read2)):
            break
        else:
            if (read2[i]+read2[i+1]) in dic.keys():
                dic[read2[i]+read2[i+1]] += 1
            dic2_length += 1

    short_length = getShortLength(dic_length, dic2_length)

    return dic, short_length

def getTrigram(read1, read2):

    dic = {}
    dic2 = {}

    dic_length = 0
    dic2_length = 0

    for i in range(len(read1)):
        if(i+2 >= len(read1)):
            break
        else:
            dic[read1[i]+read1[i+1]+read1[i+2]] = 0
            dic_length += 1

    for i in range(len(read2)):
        if(i+2>=len(read2)):
            break
        else:
            if (read2[i]+read2[i+1]+read2[i+2]) in dic.keys():
                dic[read2[i]+read2[i+1]+read2[i+2]] += 1
            dic2_length += 1

    short_length = getShortLength(dic_length, dic2_length)

    return dic, short_length

def getPercent(dic, short_length):
    score = 0
    for ch in dic.values():
        if(ch != 0):
            score += ch
    score = score/short_length * 100
    return score

def getShortLength(len1, len2):

    short_length = 0

    if(len1>=len2):
        short_length = len2
    else:
        short_length = len1

    return short_length

argc = sys.argv

f = open("sync_test2.txt",'rt')

read1 = f.readline()
read2 = f.readline()

read1 = read1.replace(' ','').replace('\n','')
read2 = read2.replace(' ','').replace('\n','')

if(len(argc) != 1):

    if( '-2' in argc[1]):

        similar, short_len = getBigram(read1,read2)
        score = round(getPercent(similar, short_len), 2)
        print("Bigram: ", score, "%")

    elif('-3' in argc[1]):

        similar, short_len = getTrigram(read1, read2)
        score = round(getPercent(similar, short_len), 2)
        print("Trigram: ", score, "%")

    elif('-5' in argc[1]):

        similar1, short_len1 = getBigram(read1, read2)
        similar2, short_len2 = getTrigram(read1, read2)
        similar1.update(similar2)

        short_len = short_len1+short_len2
        score = round(getPercent(similar1, short_len), 2)
        print("Bigram + Trigram: ", score, "%")

    else:

        similar, short_len = getBigram(read1,read2)
        score = round(getPercent(similar, short_len), 2)
        print("Bigram: ", score, "%")

else:

    similar, short_len = getBigram(read1,read2)
    score = round(getPercent(similar, short_len), 2)
    print("Bigram: ", score, "%")

f.close()