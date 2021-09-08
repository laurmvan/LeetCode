import unittest

def isValid(s):
    # can't have a matching bracket if it's an odd length, at least one wouldn't have a match
    if (len(s)%2!=0 or len(s)==0): 
        return False 

    dict_match = {"(":")",")":"(","{":"}","}":"{","[":"]","]":"["}

    for symb in s:
        s_list = list(s)
        print(s_list)
        while (len(s_list) >= 0):
            if (len(s_list) < 2):
                break
            # if(s_list[s_list.index(symb)])
            print(s_list.index(symb))
            s_list=s_list[0:-1]




    # return False

print(isValid("([])()"))


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