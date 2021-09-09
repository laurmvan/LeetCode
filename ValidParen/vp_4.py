import unittest

def isValid(s):
    # can't have a matching bracket if it's an odd length, at least one wouldn't have a match
    if (len(s)%2!=0 or len(s)==0): 
        return False 

    dict_match = {"(":")",")":"(","{":"}","}":"{","[":"]","]":"["}

    s = list(s)

    for i in range(len(s)):
        if (i + 1 < len(s)):
            # print (dict_match[s[i]])
            print(s)
            if (s[i + 1] == dict_match[s[i]]):
                print("remove")
                s.pop(i)
                s.pop(i)
                # s.pop(i+1)
                print (s)
                # print(s[i],s[i+1])

    # for symb in s:
    #     s_list = list(s)
    #     while (len(s_list) >= 0):
    #         if (len(s_list) < 2):
    #             break
    #         # if(s_list[s_list.index(symb)])
    #         if (len(s_list) >= 2 and s_list.index(symb) != len(s_list)):
    #             if (s_list.index(symb))

    #         print(s_list.index(symb))
    #         print(symb)
    #         s_list=s_list[0:-1]




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