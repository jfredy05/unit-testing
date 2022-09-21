import unittest

class TestMultiplication(unittest.TestCase):
    def runTest(self):
        self.assertEqual((3*5), 12)


class TestAddition(unittest.TestCase):
    def runTest(self):
        self.assertEqual((1+5), 6)


class TestDivision(unittest.TestCase):
    def runTest(self):
        self.assertEqual((7/0), 1)


class SimpleTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, 1)
    
    @unittest.skip("Temporarily skips test")
    def test_2(self):
        self.assertEqual(2, 2)
    
    def prueba_3(self):
        self.assertEqual(3, 3)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMultiplication())
    suite.addTests([TestAddition(), TestDivision()])
    
    # Llamar la clase SimpleTest
    suite = unittest.makeSuite(SimpleTest, 'test') # Inicia con test
    suite.addTests([TestAddition(), TestDivision(), TestMultiplication()])
    
    # unittest.TextTestRunner().run(suite)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    
    print("\nErrors: ", result.errors)
    print("\nFailures: ", result.failures)
    print("\nSkipped tests: ", result.skipped)
    print("\n# of tests: ", result.testsRun)
    print("\nWas it a successful test?: ", result.wasSuccessful())
