import unittest

def isValid(s):
    # print(s.index("i"))

    dict_match = {"(":")",")":"(","{":"}","}":"{","[":"]","]":"["}

    # for symb in s:
    #     subtring = s
    #     while (len(substring) != 0):
    #         if ()

        # print(symb)

    # can't have a matching bracket if it's an odd length, at least one wouldn't have a match
    # if (len(s)%2!=0 or len(s)==0): 
    #     return False 

    # # check if first half of string = second half of string reversed
    # half = int(len(s) / 2)
    # comp1 = s[0:half]
    # # print (comp1)
    # comp2 = s[half:]
    # rev = comp2[::-1]
    # rev = rev.replace(")","(")
    # if (comp1 == rev):
    #     return True

    # return False

print(isValid("()[]"))


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

# if __name__ == '__main__':
#     unittest.main(verbosity=2)