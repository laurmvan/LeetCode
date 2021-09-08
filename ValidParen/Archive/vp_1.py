import unittest

def isValid(s):

    # can't have a matching bracket if it's an odd length, at least one wouldn't have a match
    if (len(s)%2!=0): 
        return False 

    # check if first half of string = second half of string reversed
    half = int(len(s) / 2)
    comp = s[0:half]
    rev = comp[::-1]
    print (comp,rev)

    if (comp == rev):
        return True

    return False

print(isValid("(){][}"))


#----------------------TEST CASES-----------------------------
class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(isValid("()"),True)

    def test_2(self):
        self.assertEqual(isValid("()[]{}"),True)

    def test_3(self): #shouldn't this be "rac??"
        self.assertEqual(isValid("(]"),False)

    def test_4(self):
        self.assertEqual(isValid("([)]"),False)

if __name__ == '__main__':
    unittest.main(verbosity=2)