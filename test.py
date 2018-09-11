import unittest
from calculator import Calculator


class ModuleTest(unittest.TestCase):

    def setUp(self):
        self.cal = Calculator(8,4)

    def tearDown(self):
        pass

    def test_add(self):
        result = self.cal.add()
        self.assertEqual(result,12)

    def test_sub(self):
        result = self.cal.sub()
        self.assertEqual(result,4)

    # def test_mul(self):
    #     result = self.cal.mul()
    #     self.assertEqual(result, 32)

    def test_div(self):
        result = self.cal.div()
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
    # suit = unittest.TestSuite()
    # suit.addTest(ModuleTest("test_add"))
    # suit.addTest(ModuleTest("test_sub"))
    # suit.addTest(ModuleTest("test_mul"))
    # suit.addTest(ModuleTest("test_div"))
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suit)