import unittest
import rectangle_perimeter
import sys


class TestArea(unittest.TestCase):
    
    @unittest.skip('Temporarily skips error test')
    def test_error(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter(10, 5)
    
    @unittest.skipIf(sys.version_info[0] < 3,
                     'This test requires Python 3 or higher')
    def test_error(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter(10, 5)
            
    @unittest.skipUnless(sys.platform.startswith('win'),
                     'Requires Windows')
    def test_error(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter(10, 5)

if __name__ == '__main__':
    unittest.main()
