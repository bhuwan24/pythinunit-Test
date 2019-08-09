import unittest
import calc

class Testcalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.calc_add(10,5),15)
    def test_div(self):
        self.assertEqual(calc.calc_div(20,10),2)





if __name__=='__main__':
    unittest.main()
