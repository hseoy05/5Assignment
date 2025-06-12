def gcd(a, b):
    while (b!=0):
        temp = a
        a = b
        b = temp % b
    return a

a = int(input("Enter a: "))
b = int(input("Enter b: "))

while (a < 0 or b < 0 or a < b):
    print("Invalid input.")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

result = gcd(a, b)

print("GCD is", result)