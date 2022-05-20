m=int(input('enter marks: '))
n=int(input('enter marks: '))
o=int(input('enter marks: '))
b=m+n+o
a=b/300
#average 
print(a)
if a>=40  :
	if n>=33 and m >=33 and o >=33:
		print("pass with overall percet",a*100,"%")
	else :
		pass

else:
	print("fail due to interal subject ",a*100,"%")
