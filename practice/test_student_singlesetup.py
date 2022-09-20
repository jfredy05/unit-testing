import unittest
from student import Student


class TestStudent(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        print('\n setupClass \n')
        cls.stu_1 = Student("Fredy", "Garcia", 25000)
    
    @classmethod
    def tearDownClass(cls) -> None:
        print('\n TearDownClass \n')