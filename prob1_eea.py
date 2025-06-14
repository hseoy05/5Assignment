def EEA(a,b):
    s1, s2 =1, 0
    t1, t2 =0, 1

    while(b>0):
        q, p = a//b, a%b
        a, b=b, p
        s=s1-q*s2
        t=t1-q*t2
        s1, s2 = s2, s
        t1, t2 = t2, t
    return a,s1,t1

a = int(input("Enter a: "))
b = int(input("Enter b: "))

while(a<b or b<0):
    print("Invalid value") 
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

a, s, t = EEA(a,b)

print(f"GCD: {a}, s: {s}, t: {t}")
