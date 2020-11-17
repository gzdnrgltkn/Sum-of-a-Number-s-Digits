n = int(input())
digits=0
ldigits=[]
toplam=0
while n > 0:
 digits=n%10
 ldigits.append(digits)
 n //= 10
toplam=sum(ldigits)
print(toplam)
    
