nums = [1,4,4]
target = 8
length = len(nums)

for i in range(length):
	if (i+1>length):
		break
	if(nums[i]+nums[i+1]==target):
		result = [i, i+1]
		print(result)
	print(i)

# for i in nums:
# 	for x in nums:
# 		if(nums.index(x)==nums.index(i)):
# 			print("same index")
# 		if(x + i == target):
# 			result = [nums.index(x), nums.index(i)]
# 			print(result)
# 			break

# while count < length:
# 	for i in nums:
# 		for x in nums:
# 			if(nums.index(x)!=nums.index(i)):
# 				if(x+i==target):
# 					print("solution")
# 	# print(nums[count])
# 	# print(nums[length-count])
# 	print (count)
# 	count+=1
# for i in nums:
# 	print(nums.index(i))
# 	for x in nums:
# 		print(nums.index(x))
# 		if (nums.index(x)!=nums.index(i)):
# 			print("skipped",x)
# 			if(x + i == target):
# 				result = [nums.index(x), nums.index(i)]



# print(nums[1])
# while count < (len(nums)-1):
# 	print(count)
# 	for i in nums:
# 		for x in nums:
# 			if (nums.index(x)!=nums.index(i)):
# 				if(nums[count] + nums[count] == target):
# 					result = [nums.index(nums[count]), nums.index(nums[count])]
# 					print(result)
# 					print(count)
# 					break
# 			if(x + i == target):
# 				result = [nums.index(x), nums.index(i)]
# 				print(result)
# 				break
# 		count+=1


# print(nums[1])

# for i in nums:
# 	for x in nums:
# 		if(x!=i):
# 			print("made it to loop")
# 			if(x + i == target):
# 				result = [nums.index(x), nums.index(i)]
# 				print(result)
# 				break

# for i in range((len(nums)-1)):
# 	print(i)
# 	if(nums[i] + nums[i]+1 == target):
# 		print(nums.index(i+1))
# 		print(nums.index(i))
# 		result = [nums.index(x), nums.index(i)]
# 		print(result)


			
