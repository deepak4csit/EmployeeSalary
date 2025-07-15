def factors(n):
    i=2
    while i<=n/2:
        if(n%i==0):
            print(i)
        i=i+1


print("Enter a Number ")
n=int(input())
factors(n)

