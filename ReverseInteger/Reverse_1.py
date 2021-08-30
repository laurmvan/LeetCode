number = -1354
print(number)
neg = False
tooBig = False

if (number <= pow(2,31)-1 & number >= pow(-2,31)): #check if 32 bit integer
	tooBig = True #can delete
	print ("return 0")

if number < 0: #check if negative
	neg = True
	print ("negative")

number = abs(number)
l1 = [int(x) for x in str(number)] # make number a string to be interated

l1.sort(reverse=True)#note sort changes list directly and doesn't return val
#sorted doesn't change list but returns sorted value
print(l1)
print(type(l1))

# elif number >= 0:
# 	l1 = [int(x) for x in str(number)] # make number a string to be interated
# 	neg = False	

# l1 = [int(x) for x in str(number)] # make number a string to be interated
# print(l1)
# print(type(l1))

# l1.sort(reverse=True)#note sort changes list directly and doesn't return val
# #sorted doesn't change list but returns sorted value
# # print (l1)

# l1 = sorted(l1) #note sort changes list directly and doesn't return val
# #sorted doesn't change list but returns sorted value

# print(l1)