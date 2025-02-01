# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input().strip())
b = int(input().strip())
m = int(input().strip())

def pow(a,b,m):
    power = a**b
    modulus = power % m
    print(power)
    print(modulus)
    
    
pow(a,b,m)