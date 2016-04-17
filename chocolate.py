#http://codingbat.com/prob/p190859
#We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) 
#and big bars (5 kilos each). Return the number of small bars to use, assuming we always 
#use big bars before small bars. Return -1 if it can't be done.


import unittest
def make_chocolate(small,big,goal):
	bigBars= goal//5
	smallBars=goal%5

	if bigBars>big:
		smallBars=smallBars+(bigBars-big)*5
	if(smallBars>small):
		return -1
	return smallBars


class MyTest(unittest.TestCase):
    def test(self):
		self.assertEqual(make_chocolate(4, 1, 9), 4)
		self.assertEqual(make_chocolate(4, 1, 10) ,-1)
		self.assertEqual(make_chocolate(4, 1, 7), 2)
		self.assertEqual(make_chocolate(6, 2, 7) ,2 )
		self.assertEqual(make_chocolate(4, 1, 5) ,0 )
		self.assertEqual(make_chocolate(4, 1, 4) ,4 )
		self.assertEqual(make_chocolate(5, 4, 9) ,4 )
		self.assertEqual(make_chocolate(9, 3, 18), 3)
		self.assertEqual(make_chocolate(3, 1, 9) ,-1 )
		self.assertEqual(make_chocolate(1, 2, 7) ,-1)
		self.assertEqual(make_chocolate(1, 2, 6) ,1 )
		self.assertEqual(make_chocolate(1, 2, 5) ,0 )
		self.assertEqual(make_chocolate(6, 1, 10), 5)
		self.assertEqual(make_chocolate(6, 1, 11) ,6 )
		self.assertEqual(make_chocolate(6, 1, 12) ,-1)
		self.assertEqual(make_chocolate(6, 1, 13) ,-1)
		self.assertEqual(make_chocolate(6, 2, 10), 0)
		self.assertEqual(make_chocolate(6, 2, 11) ,1 )
		self.assertEqual(make_chocolate(6, 2, 12), 2)
		self.assertEqual(make_chocolate(60, 100, 550) ,50)
		self.assertEqual(make_chocolate(1000, 1000000, 5000006), 6)
		self.assertEqual(make_chocolate(7, 1, 12), 7)
		self.assertEqual(make_chocolate(7, 1, 13) ,-1)
		self.assertEqual(make_chocolate(7, 2, 13), 3)

if __name__ == '__main__':
	unittest.main()

