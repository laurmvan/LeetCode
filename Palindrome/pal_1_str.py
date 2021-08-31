import unittest

def isPalindrome(x):
    neg = False
    
    if x < 0: #check if negative
        return False
    
    l1 = [int(x) for x in str(x)] #make number a string to be interated
    l2 = l1[::-1] #another way to reverse a list (other than l1.reverse()) using slicing   
    
    if (l1 == l2): return True

    else: return False

print(isPalindrome(121))


#----------------------TEST CASES-----------------------------
class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(isPalindrome(121),True)

    def test_2(self):
        self.assertEqual(isPalindrome(-121),False)

    def test_3(self):
        self.assertEqual(isPalindrome(10),False)

    def test_4(self):
        self.assertEqual(isPalindrome(-101),False)

if __name__ == '__main__':
    unittest.main(verbosity=2)