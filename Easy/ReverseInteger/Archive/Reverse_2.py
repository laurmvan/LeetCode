x = pow(2,31)
neg = False

if (x <= pow(2,31)-1 & x >= pow(-2,31)): #check if 32 bit integer
	print ("return",0)

if x < 0: #check if negative
	neg = True
	print ("negative")

x = abs(x)
l1 = [int(x) for x in str(x)] # make number a string to be interated
l1.sort(reverse=True) # reverse sort list of integers
#note sort changes list directly and doesn't return val
#sorted doesn't change list but returns sorted value
strings = [str(integer) for integer in l1] #makes list of string integers
a_string = "".join(strings) #combines list of integers (type string) into one string
x2 = int(a_string) #converts string to int

if(neg==True):
	print ("return", x2 *-1)

else:
	print("return", x2)
