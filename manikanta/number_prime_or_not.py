n=int(input("enter anumber:"))
for x in range(2,n):
    if(n%x==0):
        print(n,"is not a prime number")
        break
    else:
        print(n,"is prime number")

