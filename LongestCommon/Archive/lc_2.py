import unittest

def longestCommonPrefix(strs):
    if len(strs) <= 1:
        return strs[0]
    
    d1 = {} 

    for word in strs:
        if (len(word) > 2 and word[0:2] in d1):
            d1[word[0:2]]+=1
        elif (len(word) > 2):
            d1[word[0:2]]=1
        elif (word in d1):
            d1[word]+=1 
        else:
            d1[word]=1


    new_dict = sorted(d1, key = lambda word: word, reverse = True)

    if (len(new_dict) == 1):
        return new_dict[0]
    if (d1[new_dict[0]] == d1[new_dict[1]]):
            return ""
    else: return new_dict[0]


print(longestCommonPrefix(["dog","racecar","rack"]))


#----------------------TEST CASES-----------------------------
class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(longestCommonPrefix(["flower","flow","flight"]),"fl")

    def test_2(self):
        self.assertEqual(longestCommonPrefix(["dog","racecar","car"]),"")

    def test_3(self): #shouldn't this be "rac??"
        self.assertEqual(longestCommonPrefix(["dog","racecar","rack"]),"ra")

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