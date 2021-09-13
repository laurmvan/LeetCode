import unittest

def isPalindrome(x):
    if x < 0: return False 
    i = x
    count=0
    l1=[]
    while (i >= 10): # one "/" does exact value and two "//" does floor division
        count+=1
        l1.append((i//10)%10)
        i = (i//10)
    # l1.reverse()  
    l1.insert(0,x%10)  
    print(l1)
    for x in range(len(l1)):
        print(x)
        # print (i)
        # print (count)
    # print(10 ** count + i)
    

    # print(x//10) 
    # if x < 0: #check if negative
    #     return False
    
    # l1 = [int(x) for x in str(x)] #make number a string to be interated
    # l2 = l1[::-1] #another way to reverse a list (other than l1.reverse()) using slicing   
    
    # if (l1 == l2): return True

    # else: return False

print(isPalindrome(2121))


# #----------------------TEST CASES-----------------------------
# class TestStringMethods(unittest.TestCase):
#     def test_1(self):
#         self.assertEqual(isPalindrome(121),True)

#     def test_2(self):
#         self.assertEqual(isPalindrome(-121),False)

#     def test_3(self):
#         self.assertEqual(isPalindrome(10),False)

#     def test_4(self):
#         self.assertEqual(isPalindrome(-101),False)

#     def test_5(self):
#         self.assertEqual(isPalindrome(1000021),False)

# if __name__ == '__main__':
#     unittest.main(verbosity=2)