import unittest

def isPalindrome(x):
    neg = False
    
    if x < 0: #check if negative
        return False
    
    l1 = [int(x) for x in str(x)] #make number a string to be interated
    
    if (l1 == )

    print(l1)
    l2 = l1[::-1] #another way to reverse a list (other than reverse()) using slicing
    # l1.reverse()
    print(l1)
    # l1.reverse() #reverses elements in a list

    # strings = [str(integer) for integer in l1] #makes list of string integers
    # a_string = "".join(strings) #combines list of integers (type string) into one string
    # x2 = int(a_string) #converts string to int

    # if (x2 > pow(2,31)-1 or x2 < pow(-2,31) or x2 == 0): #check if 32 bit integer
    #     return 0

    # if (neg==True):
    #     return x2*-1

    # else:
    #     return x2

print(isPalindrome(12))


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

#     # def test_5(self):
#     #     self.assertEqual(isPalindrome(1009001),1009001)

#     # def test_6(self):
#     #     self.assertEqual(isPalindrome(100900),9001)

#     # def test_7(self):
#     #     self.assertEqual(isPalindrome(901000),109)

# if __name__ == '__main__':
#     unittest.main(verbosity=2)