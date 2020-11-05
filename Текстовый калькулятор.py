number = { 'zero': 0,
	'one': 1,
	'two': 2,
	'three': 3,
	'four': 4,
	'five': 5,
	'six': 6,
	'seven': 7,
	'eight': 8,
	'nine': 9,
	'ten': 10,
	'eleven': 11,
	'twelve': 12,
	'thirteen': 13,
	'fourteen': 14,
	'fifteen': 15,
	'sixteen': 16,
  	'seventeen': 17,
  	'eighteen': 18,
  	'nineteen': 19,
  	'twenty': 20,
  	'thirty': 30,
  	'forty': 40,
  	'fifty': 50,
  	'sixty': 60,
  	'seventy': 70,
  	'eighty': 80,
  	'ninety': 90,
  	'hundred': 100,
  	'thousand': 1000,
  	}

operations = {'plus': '+',
	'minus': '-',
	'multiplyby': '*'
	}

def output(result):
	if result<0:
		print('minus', end=' ')
	result=abs(result)
	if result==10000:
		return print('ten thousand')
	n=[0,0,0,0]

	for i in range(3,-1,-1):
		n[i]=result%10
		result//=10
	
	if n[0]>0:
		for (k,v) in number.items():
			if v==n[0]:
				n1=k
				print(n1, 'thousand', end=' ')
	if n[1]>0:
		for (k,v) in number.items():
			if v==n[1]:
				n2=k
				print(n2, 'hundred', end=' ')

	n=n[2:]
	n=[str(x) for x in n]
	n3=int(''.join(n))
	f=False
	for (k,v) in number.items():
			if v==n3:
				print(k)
				f=True
	if f==False:
		n4=(n3//10)*10
		n5=n3%10
		for (k,v) in number.items():
			if v==n4:
				print(k, end=' ')
		for (k,v) in number.items():
			if v==n5:
				print(k)

stroka=input('Enter what to do: ').split()
#print(stroka)
c=stroka.copy()
for i in range(len(c)):
	for keys in number.keys():
		if c[i]==keys:
			c[i]=number[keys]
print(c)
istr2=0
n=0
if type(c[0])==str:
	for i in range(1,len(c)-1):
		if type(c[i])==str and n==0:
			istr2=i
			n+=1
else:
	for i in range(len(c)):
		if type(c[i])==str and n==0:
			istr2=i
			n+=1
#print('Index of operation: ', istr2)
number1=c[:istr2]
for i in range(len(number1)):
	for keys in operations.keys():
		if number1[i]==keys:
			number1[i]=operations[keys]
s1=0
for i in range(len(number1)-1,-1,-1):
	if type(number1[i])==int:
		s1+=number1.pop(i)
number1.append(str(s1))
number1=''.join(number1)
number1=int(number1)


istrlast=0
n=0
for i in range(len(c)-1,-1,-1):
	if type(c[i])==str and n==0:
		istrlast=i
		n+=1
number2=sum(c[istrlast+1:])


#print(number1, type(number1))
#print(number2, type(number2))
result=0
c=c[istr2:istrlast+1]
#print(c)
if c==['multiply', 'by']:
	result=number1*number2
if c==['multiply', 'by', 'minus']:
	result=-(number1*number2)
if c==['plus']:
	result=number1+number2
if c==['minus']:
	result=number1-number2
if c==['plus', 'minus']:
	result=number1-number2

output(result)
