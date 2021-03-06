import unittest

def reverse(x):
    neg = False
    
    if x < 0: #check if negative
        neg = True
        
    x = abs(x)
    l1 = [int(x) for x in str(x)] #make number a string to be interated
    l1.reverse() #reverses elements in a list

    strings = [str(integer) for integer in l1] #makes list of string integers
    a_string = "".join(strings) #combines list of integers (type string) into one string
    x2 = int(a_string) 
    if (x2 > pow(2,31)-1 or x2 < pow(-2,31) or x2 == 0): #check if 32 bit integer
        return 0

    if (neg==True):#converts string to int

        return x2*-1

    else:
        return x2

num = reverse(-12300)
print(num)


#----------------------TEST CASES-----------------------------
class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverse(-123),-321)

    def test_2(self):
        self.assertEqual(reverse(123),321)

    def test_3(self):
        self.assertEqual(reverse(120),21)

    def test_4(self):
        self.assertEqual(reverse(0),0)

    def test_5(self):
        self.assertEqual(reverse(1009001),1009001)

    def test_6(self):
        self.assertEqual(reverse(100900),9001)

    def test_7(self):
        self.assertEqual(reverse(901000),109)

if __name__ == '__main__':
    unittest.main(verbosity=2)