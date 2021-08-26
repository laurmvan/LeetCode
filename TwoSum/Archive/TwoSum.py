nums = [2,7,11,15]
target = 13
result = []
target2 = target

for i in nums:
	if target2 == 0:
		break
	if i < target:
		result.append(nums.index(i))
		target2 = target2 - i
		print(target2)
		print(result)
		continue
		if target2 % i == 0:
			result.append(nums.index(i))
			target2 = target2 - i
			print(target2)
			print(result)
			break


print(result)
