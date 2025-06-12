import re
from collections import defaultdict

s ="BCBCCLBSTGIGSRATCXRKEIOBVFSHNCERSRURQKBGDWMMHWSBGPXGKLFJCVGFZTIGVJFONWKODGQEHRPQLURMWKHRCVNSXRKVHRAGEHEPAZBDFGPSKPUWCVJQNWXEMFFOYUCWLCTRHSMPWFYKLRDKLGJSBSNVWXLKESDCGETYPVPTSTGKVOGPJHSRWKWYLVIOXQHFFWCFWFYKCJAKJNTCVJGXSSLVFOPSNCTVCFXSNSPZJOPUZHIYFUWXEPLAOPQLGPYELZDGGJOXBIIONSCKSCAJFCVQVFAOCVKVOETFKSLIESOBUFTKLGNZIGPUSZCPUSXRPRHSMPSMDFGDWNAGEHEPABCBCCLBSTGIGSRAYONCUKOLJKJVOBEFZVCIVGYDNRKWCFZQSLGVBQGPVSBGPXOXBDLGSLGJGKBOZBSQVIODGQEOWMPXCDFGIGDFGJSXCYGFYETRACLQKCXJARHDPCTHOBCSFYYFVFCRWUSXRDFRIDTFAKATFGCRJVDOLKEGEJCSIDYNJCVYKUHRCIICELFNCBIHFFDFGLBSTGIGSRAJTERWISKQCEODGQEOVJGRROPKEFOQGRFMFCERZPQWSCQKFBKJVIOSLKEU"
l = len(s)

#key 후보
#LBSTGIGSRA
#ODGQE
#SXR LKE VIO
#DFG STG GIG

#-----------------암호키 후보들 찾기-------------------
def checkKasiski():
    attempt=3
    while(True):
        temp={}
        for i in range(l-(attempt-1)):
            trigram=s[i:i+attempt]
            temp[trigram] = temp.get(trigram, 0) + 1
        trigram_s = sorted(temp.items(), key=lambda x: x[1], reverse=True)

        if not trigram_s or trigram_s[0][1] <=1:
            break

        value = trigram_s[0][1]
        key=[]
        group_trigram={}

        for i in trigram_s:
            if i[1]==value:
                key.append(i[0])
            else:
                if (value>=3):
                    group_trigram[tuple(key)]=value
                key.clear()
                value = i[1]
                key.append(i[0])
        if(value>=3):
            group_trigram[tuple(key)]= value
        key.clear()

        if group_trigram:
            print(str(attempt), end=": ")
            for i in group_trigram.items():
                for j in i[0]:
                    print(str(j), end = ' ')
                print(': ' + ' - ' + str(i[1]))
            print()
        else:
            break
        attempt+=1
        print()
    return True

#checkKasiski() -> 반복되는거 찾는 함수 실행행
#---------------------------------------------------------

#------------------- GCD ---------------------------------
def GCD(a,b):
    if(b>a):
        a, b = b, a
    if(b==0):
        return a
    return GCD(b,a%b)
#---------------------------------------------------------

#------------------ d 계산 --------------------------------
def findD(cipher_str):
    matches = list(re.finditer(cipher_str, s))
    ml = len(matches)
    dl=0
    d=[]
    for i in range(1,ml):
        d.append(matches[i].start()-matches[i-1].start())
        dl+=1
    startValue=d[0]
    for i in range(1,dl):
        gcdValue = GCD(startValue,d[i])
        startValue=gcdValue
    return gcdValue
#----------------------------------------------------------

#-------- splitString ---------------
def splitString(n):
    lst = [s[i:i+n] for i in range(0, len(s), n)]
    return lst
#------------------------------------

#------------ print 세로로 -------------
def printC(d):
    print("distance: "+ str(d))
    for l in splitString(d):
        for c in l:
            print(c+" ", end="")
        print()
    print("\n")
#-------------------------------------

#----------- count Alpha num ------------------
def countAlpha(d, n):
    dct = defaultdict(int)
    #n번째 열의 문자 빈도 수 세기
    num = n-1
    while(num<=l):
        if(num>=l):
            break
        dct[s[num]] +=1
        num+=d
    return dict(sorted(dct.items(), key = lambda item: item[1], reverse=True))
#----------------------------------------------

#------------ 복호화 function -----------------------------
def origin(Elist, num):
    for i in range(l):
        c = s[i]
        M = chr((ord(c) - Elist[i%num]+26)%26+ord('A'))
        print(M, end="")
#----------------------------------------------------------





#---------------------- main func ----------------------
#find distance
keyCandidate = {"LBSTGIGSRA","ODGQE","SXR", "LKE", "VIO","DFG","STG", "GIG"}

dCandidate = set()
for key in keyCandidate:
    dCandidate.add(findD(key))
print("d Candidates: " + str(dCandidate))

#find 빈도수가 가장 많은 암호 문자를 e라고 볼 것
# 세로로 나열한 암호문값값
printC(5)
print()
#각 열의 빈도수가 높은 순으로 딕셔너리 나열열
for i in range(5):
    print(i+1, ":\n", str(countAlpha(5,i+1)), end='\n\n')


#---------------- real test ---------------
#e t a o i n s h r
resultList=[]

DISTANCE = 50
C_ALPHA = 'T'

for i in range(DISTANCE):
    llst=countAlpha(DISTANCE,i+1)
    keyList = sorted(llst.items(), key=lambda x:x[1], reverse=True)
    Cs = keyList[0][0]
    resultList.append((ord(Cs)-ord(C_ALPHA))%26)

for n in resultList:
    print(chr(n+ord('A')), end=" ")
print()

origin(resultList, 5)




    

