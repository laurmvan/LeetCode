import unittest

def isValid(s):
    # can't have a matching bracket if it's an odd length, at least one wouldn't have a match
    if (len(s)%2!=0 or len(s)==0): 
        return False 

    dict_match = {"(":")",")":"(","{":"}","}":"{","[":"]","]":"["}

    s = list(s)

    for i in range(len(s)):
        while (i + 1 < len(s)):
            # print (dict_match[s[i]])
            print(s)
            if (s[i + 1] == dict_match[s[i]]):
                print("remove")
                s.pop(i)
                s.pop(i)
                
                # s.pop(i+1)
                print (s)
                continue
            else: break
                # print(s[i],s[i+1])


    # return False

print(isValid("([])[()]()([()])"))


# #----------------------TEST CASES-----------------------------
# class TestStringMethods(unittest.TestCase):
#     def test_1(self):
#         self.assertEqual(isValid("()"),True)

#     def test_2(self):
#         self.assertEqual(isValid("()[]{}"),True)

#     def test_3(self): #shouldn't this be "rac??"
#         self.assertEqual(isValid("(]"),False)

#     def test_4(self):
#         self.assertEqual(isValid("([)]"),False)

#     def test_5(self):
#         self.assertEqual(isValid("()[{}]"),True)

#     def test_6(self):
#         self.assertEqual(isValid("(][{}]"),False)

#     def test_7(self):
#         self.assertEqual(isValid("([])()"),True)

# if __name__ == '__main__':
#     unittest.main(verbosity=2)