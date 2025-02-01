n = int(input().strip())

def weird(n):
    if n%2 == 1:
        print("Weird")
    elif n in range(2,6):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
    else:
        print("Not Weird")


weird(n)
    
    