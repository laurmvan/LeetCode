
nums = [4,4,8]
target = 12
result = []
count1 = 0
nums_dict = {}

for i in nums:
	nums_dict[count1] = i
	count1 = count1 + 1

for i in nums_dict:
	for x in nums_dict:
		if(x == i):
			continue
		if(nums_dict[i]+nums_dict[x] == target):
			result = [x,i]

print(result)