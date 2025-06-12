import re
from collections import defaultdict
from collections import Counter

s ="BCBCCLBSTGIGSRATCXRKEIOBVFSHNCERSRURQKBGDWMMHWSBGPXGKLFJCVGFZTIGVJFONWKODGQEHRPQLURMWKHRCVNSXRKVHRAGEHEPAZBDFGPSKPUWCVJQNWXEMFFOYUCWLCTRHSMPWFYKLRDKLGJSBSNVWXLKESDCGETYPVPTSTGKVOGPJHSRWKWYLVIOXQHFFWCFWFYKCJAKJNTCVJGXSSLVFOPSNCTVCFXSNSPZJOPUZHIYFUWXEPLAOPQLGPYELZDGGJOXBIIONSCKSCAJFCVQVFAOCVKVOETFKSLIESOBUFTKLGNZIGPUSZCPUSXRPRHSMPSMDFGDWNAGEHEPABCBCCLBSTGIGSRAYONCUKOLJKJVOBEFZVCIVGYDNRKWCFZQSLGVBQGPVSBGPXOXBDLGSLGJGKBOZBSQVIODGQEOWMPXCDFGIGDFGJSXCYGFYETRACLQKCXJARHDPCTHOBCSFYYFVFCRWUSXRDFRIDTFAKATFGCRJVDOLKEGEJCSIDYNJCVYKUHRCIICELFNCBIHFFDFGLBSTGIGSRAJTERWISKQCEODGQEOVJGRROPKEFOQGRFMFCERZPQWSCQKFBKJVIOSLKEU"
l = len(s)

#찾아본 결과: 우연히 rarra 돌려봤는데 korea 로 시작할거같아 끼워맞춰봄 ㅎ
#ROKYC
#KOREAUNIVERSITYCONTINUEDTOEXPANDITSACADEMICOFFERINGSANDSOLIDIFYITSREPUTATIONTHROUGHOUTTHETWENTIETHCENTURYINTHEYEARSFOLLOWINGKOREASLIBERATIONFROMJAPANESERULEINNINETEENFORTYFIVETHEINSTITUTIONTRANSFORMEDFROMASMALLCOLLEGEINTOAFULLFLEDGEDUNIVERSITYADDINGNUMEROUSFACULTIESANDGRADUATESCHOOLSTOMEETTHEGROWINGNEEDSOFANEWLYINDEPENDENTNATIONBYTHEMIDCENTURYKOREAUNIVERSITYHADESTABLISHEDCOLLEGESOFLAWMEDICINEENGINEERINGANDBUSINESSADMINISTRATIONAMONGOTHERSTHESENEWPROGRAMSNOTONLYATTRACTEDABROADERSTUDENTBODYFROMACROSSTHEPENINSULABUTALSOLAIDTHEGROUNDWORKFORTHEUNIVERSITYSFUTUREASANATIONALLEADERINRESEARCHANDPROFESSIONALTRAINING
#_------------

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
def origin(keyShifts):
    result=""
    for i in range(l):
        shift = keyShifts[i%len(keyShifts)]
        c = s[i]
        M = chr( (ord(c) - ord('A')-shift) % 26 + ord('A'))
        result+=M
    return result
#----------------------------------------------------------




#---------------------- main func ----------------------
#find distance
keyCandidate = {"LBSTGIGSRA","ODGQE","SXR", "LKE", "VIO","DFG","STG", "GIG"}

dCandidate = set()
for key in keyCandidate:
    dCandidate.add(findD(key))
print("d Candidates: " + str(dCandidate))

DISTANCE = 5
#find 빈도수가 가장 많은 암호 문자를 e라고 볼 것
# 세로로 나열한 암호문값
#printC(DISTANCE)
print()
#각 열의 빈도수가 높은 순으로 딕셔너리 나열
for i in range(DISTANCE):
    print(i+1, ":\n", str(list(countAlpha(DISTANCE,i+1).items())[:4]), end='\n\n')

#암호화 문 내에 등장한 알파벳 빈도 비율 구하기
def letterPercentage(string):
    total = l//DISTANCE
    counter = Counter(string)
    freqDict={}
    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        freqDict[c] = round((counter.get(c,0)/total), 2)
    return  dict(sorted(freqDict.items(), key=lambda item: item[1], reverse=True))

columnRatePercent=[]
for i in range(DISTANCE):
    columnText = ''.join([s[j] for j in range(i, l, 5)])
    columnRatePercent.append(letterPercentage(columnText))

for i in range(DISTANCE):
    print(str(i+1), ": ", list(columnRatePercent[i].items())[:4])
#---------------- real test ---------------
#e t a o i n s h r
resultList=[]

C_ALPHA = input("C_Alpha: ").strip().upper()
if len(C_ALPHA)!= DISTANCE:
    print("키 길이 오류")
    exit()
resultList=[(ord(c) - ord('A')) for c in C_ALPHA]
print()

print("shift list: ", resultList)
print(origin(resultList))
