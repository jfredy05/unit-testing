import unittest
from student import Student


class TestStudent(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        print('\n setupClass \n')
    
    @classmethod
    def tearDownClass(cls) -> None:
        print('\n TearDownClass \n')

    def setUp(self) -> None:
        print('\n Setup \n')
        self.stu_1 = Student("Fredy", "Garcia", 25000)
        
    def tearDown(self) -> None:
        pass

    def test_mail(self):
        self.assertEqual(self.stu_1.mail, "Fredy.Garcia@xyz.com")
        self.stu_1.first = "John"
        self.assertEqual(self.stu_1.mail, "John.Garcia@xyz.com")
    
    def test_fullname(self):
        self.assertEqual(self.stu_1.fullname, "Fredy Garcia")
        self.stu_1.first = "John"
        self.assertEqual(self.stu_1.fullname, "John Garcia")
    
    def test_stipend_hike(self):
        self.stu_1.apply_hike()
        self.assertEqual(self.stu_1.stipend, 26250)

if __name__ == "__main__":
    unittest.main()