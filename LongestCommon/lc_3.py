import unittest

def longestCommonPrefix(strs):
    if len(strs) == 0: return ""

    substring = strs[0]  

    for word in strs:
        while (len(substring)!=0):
            count = len(substring)
            if word[0:count] == substring:
                break
            else:
                substring = substring[0:-1]
    
    if (len(substring)==0): return ""
    return substring

print(longestCommonPrefix(["rave","ra","racecar","pie"]))


#----------------------TEST CASES-----------------------------
class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(longestCommonPrefix(["flower","flow","flight"]),"fl")

    def test_2(self):
        self.assertEqual(longestCommonPrefix(["dog","racecar","car"]),"")

    def test_3(self): #shouldn't this be "rac??"
        self.assertEqual(longestCommonPrefix(["dog","racecar","rack"]),"")

    def test_4(self):
        self.assertEqual(longestCommonPrefix(["",""]),"")

    def test_5(self):
        self.assertEqual(longestCommonPrefix([""]),"")

    def test_6(self):
        self.assertEqual(longestCommonPrefix(["a"]),"a")

    def test_6(self):
        self.assertEqual(longestCommonPrefix(["a","an"]),"a")

if __name__ == '__main__':
    unittest.main(verbosity=2)