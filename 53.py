j=int(input())
sum=0
r=0
while j>0:
  r=j%10
  j=j//10
  sum=sum+r
print(sum)
