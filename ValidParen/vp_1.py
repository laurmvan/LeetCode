import unittest

def isValid(s):







print(isValid("()"))


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

# if __name__ == '__main__':
#     unittest.main(verbosity=2)