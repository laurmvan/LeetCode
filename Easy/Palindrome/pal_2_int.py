import unittest

def isPalindrome(x):
    if x > 0:
        temp = x
        rev_int_elements = []
        while temp > 0:
            digit = temp % 10
            rev_int_elements.append(digit)
            temp = temp // 10
        org_int_elements = rev_int_elements[::-1]
        return rev_int_elements == org_int_elements
    elif x == 0:
        return True
    else:
        return False 

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

    def test_5(self):
        self.assertEqual(isPalindrome(1000021),False)

if __name__ == '__main__':
    unittest.main(verbosity=2)