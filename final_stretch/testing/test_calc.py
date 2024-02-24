import unittest
import praticetesting

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(praticetesting.add(10,5),15)
        self.assertEqual(praticetesting.add(-1,1),0) 
        self.assertEqual(praticetesting.add(-1,-1),-2) 

    def test_substract(self):
        self.assertEqual(praticetesting.substract(10,5),5)
        self.assertEqual(praticetesting.substract(-1,1),-2) 
        self.assertEqual(praticetesting.substract(-1,-1),0) 

    def test_multiply(self):
        self.assertEqual(praticetesting.multiply(10,5),50)
        self.assertEqual(praticetesting.multiply(-1,1),-1) 
        self.assertEqual(praticetesting.multiply(-1,-1),1) 

    def test_divide(self):
        self.assertEqual(praticetesting.divide(10,5),2)
        self.assertEqual(praticetesting.divide(-1,1),-1) 
        self.assertEqual(praticetesting.divide(-1,-1),1) 


        with self.assertRaises(ValueError):
            praticetesting.divide(10,0)

if __name__ == '__main__':
    unittest.main()        