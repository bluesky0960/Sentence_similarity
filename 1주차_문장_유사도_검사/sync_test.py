f = open("sync_test.txt",'rt', encoding= 'UTF8')

wordDic = {}
wordDic2 = {}
wordDic3 = {}

keyString = ""
keyString2 = ""

count_big = 0
count_small = 0

short_sentence_size_big = 0
short_sentence_size_small = 0

# 문장 2개 읽기
line1 = f.readline()
line2 = f.readline()

# 음절 배열(small), 어절 배열(big) 나누기
line1_small = line1.replace(' ','').replace(',','').replace('.','').replace('?','').replace('!','').replace('\n','')
line1_big = line1.split(' ')

line2_small = line2.replace(' ','').replace(',','').replace('.','').replace('?','').replace('!','').replace('\n','')
line2_big = line2.split(' ')

# 더 짧은 문장의 음절 갯수
if(len(line1_small)>=len(line2_small)):
    short_sentence_size_small = len(line2_small)
else:
    short_sentence_size_small = len(line1_small)

# 첫번째 문장 음절로 wordDic2 생성(특수문자 제외)
for ch in range(len(line1_small)):
    if line1_small[ch].isalnum():
        wordDic2[line1_small[ch]] = 0

# 두번째 문장 음절이 첫번째 문장의 wordDic2에 포함되어 있는지 확인
for ch in range(len(line2_small)):
    if line2_small[ch].isalnum():
        if line2_small[ch] in wordDic2.keys():
            wordDic2[line2_small[ch]] += 1

# 첫번째 문장의 wordDic2에서 value값이 0이 아닌 개수 세기(공통 음절의 갯수)
for ch in wordDic2.values():
    if(ch != 0):
        count_small += ch

print("공통 음절의 갯수: ", count_small,"개")
print("공통 음절에 대한 유사도", round(count_small/short_sentence_size_small * 100, 2),"%")

# 더 짧은 문장의 어절 갯수
if(len(line1_big) >= len(line2_big)):
    short_sentence_size_big = len(line2_big)
else:
    short_sentence_size_big = len(line1_big)

# 첫번째 문장 어절로 dictionary형태로 생성(특수 문자 제외)
for ch in range(len(line1_big)):
    for c in line1_big[ch]:
        if c.isalnum():
            keyString += c
    wordDic[keyString] = 0
    keyString = ""

# 두번째 문장의 어절이 첫번째 문장의 dictionary에 포함되었는지 확인
# 만약 포함되어 있다면 value값을 1로 바꿔준다.
for ch in range(len(line2_big)):
    for c in line2_big[ch]:
        if c.isalnum():
            keyString2 += c
    if(keyString2 in wordDic.keys()):
        wordDic[keyString2] += 1
    keyString2 = ""


# 첫번째 문장의 wordDic에서 value값이 0이 아닌 개수 세기(공통 어절의 갯수)
for ch in wordDic.values():
    if(ch != 0):
        count_big += ch

print("공통 어절의 갯수: ", count_big,"개")
print("공통 어절에 대한 유사도", round(count_big/short_sentence_size_big * 100, 2),"%")
