import unittest

def romanToInt(s):
    sum=0
    s2 = s
    dict_a = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000} #add
    dict_s = {"IV":4,"IX":9,"XL":50,"XC":90,"CD":400,"CM":900} #subtract

    for key in dict_s:
        if key in s2:
            sum+=dict_s[key]
            s2 = s2.replace(key,"") #remove from string

    for i in s2: #adding remaining values
        sum+=dict_a[i]

    return sum


print(romanToInt("III"))


#----------------------TEST CASES-----------------------------
class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(romanToInt("III"),3)

    def test_2(self):
        self.assertEqual(romanToInt("IV"),4)

    def test_3(self):
        self.assertEqual(romanToInt("IX"),9)

    def test_4(self):
        self.assertEqual(romanToInt("LVIII"),58)

    def test_5(self):
        self.assertEqual(romanToInt("MCMXCIV"),1994)

    def test_6(self):
        self.assertEqual(romanToInt("MMMXLV"),3045)


if __name__ == '__main__':
    unittest.main(verbosity=2)