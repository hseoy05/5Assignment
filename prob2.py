string="TPBFI{N3CTFD3_2_TIPGKFXI4GP!}"

def Caeser(k):
    result=""
    i=1
    for c in string:
        if c.isupper():
            result+=chr((ord(c)-65+k)%26+65)
        elif c.islower():
            result+=chr((ord(c)-97+k)%26+97)
        else:
            result+=c
    return result

for i in range(26):
    s = Caeser(i)
    print(f"{i+1}: {s}")