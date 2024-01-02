import unittest
import shape as s

class Check(unittest.TestCase):
   
    def test_check_ans(self):
        a = s.Rectangle(coo=[[-4, -3], [-4, -3], [3, 1], [3, -3]], name="Rectangle")
        ans = a.isValid()
        self.assertEqual(ans, False)

if __name__ == '__main__':
    unittest.main()