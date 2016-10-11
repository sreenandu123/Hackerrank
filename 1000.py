n=int(raw_input())
i=0
while(True):
	if 2**i>n:
		break
	i+=1
m=2**(i-1)
print (n-m)*2+1