import unittest
from student import Student


class TestStudent(unittest.TestCase):
    
    def test_mail(self):
        
        stu_1 = Student("Fredy", "Garcia", 25000)
        
        self.assertEqual(stu_1.mail, "Fredy.Garcia@xyz.com")
        
        stu_1.first = "John"
        
        self.assertEqual(stu_1.mail, "John.Garcia@xyz.com")
    
    def test_fullname(self):
        
        stu_1 = Student("Fredy", "Garcia", 25000)
        
        self.assertEqual(stu_1.fullname, "Fredy Garcia")
        
        stu_1.first = "John"
        
        self.assertEqual(stu_1.fullname, "John Garcia")
    
    def test_stipend_hike(self):
        
        stu_1 = Student("Fredy", "Garcia", 25000)
        stu_1.apply_hike()

        self.assertEqual(stu_1.stipend, 26250)

if __name__ == "__main__":
    unittest.main()
