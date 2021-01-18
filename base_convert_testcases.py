import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")
        self.assertEqual(convert(0,2),"0")
        self.assertEqual(convert(30,2),"11110")
    def test_base4(self):
        self.assertEqual(convert(30,4),"132")
        self.assertEqual(convert(15,4),"33")
        self.assertEqual(convert(1113,4),"101121")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")
        self.assertEqual(convert(510,16),"1FE")
        self.assertEqual(convert(35466,16),"8A8A")
        self.assertEqual(convert(7643,16),"1DDB")
        self.assertEqual(convert(11259375,16),"ABCDEF")
    
    def test_base11(self):
        self.assertEqual(convert(100,11),"91")
        self.assertEqual(convert(1110,11),"91A")
        self.assertEqual(convert(1352,11),"101A")
     
if __name__ == "__main__":
        unittest.main()