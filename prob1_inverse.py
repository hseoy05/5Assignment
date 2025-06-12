def EEA(a,b):
    s1, t1 = 1, 0
    s2, t2 =0, 1

    while(b>0):
        q, p= a//b, a%b
        a, b=b, p

        s=s1-q*s2
        t=t1-q*t2

        s1, s2 = s2, s
        t1, t2 = t2, t

    return a,s1,t1

def inverse(n,a):
    a,s,t=EEA(a,n)
    if(a!=1):
        print("곱셈 역원 없음")
    else:
        print(f"곱셈 역원은{s}")
    
n = int(input("Enter n: "))
a = int(input("Enter a: "))

inverse(n,a)
