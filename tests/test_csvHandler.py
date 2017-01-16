import unittest, os
import yasp.csvHandler



class csvHandlerTestCase(unittest.TestCase):


	#def setUp(self):
		

	#def tearDown(self):
	

	# If the event occured at the current minute, we consider it
	def test_computePrecisionAndRecall_different_count(self):
		# remove the first element (title rows)
		testArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Bernard"], ["Row 2", "Jean"]]
		truthArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Patrick"], ["Row 2", "Jean"],["Row 3", "Bernard"]]
		self.assertEqual(yasp.csvHandler.computePrecisionAndRecall(testArray,truthArray),{"precision": 1/3,"recall": 1/4})


	# # If the event occured at the current minute, we consider it
	def test_computePrecisionAndRecall_same_count(self):
		testArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Bernard"], ["Row 2", "Jean"],["Row 3", "Jean"]]
		truthArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Patrick"], ["Row 2", "Jean"],["Row 3", "Bernard"]]
		self.assertEqual(yasp.csvHandler.computePrecisionAndRecall(testArray,truthArray),{"precision": 1/4,"recall": 1/4})

	# # If the event occured at the current minute, we consider it
	# def test_computePrecisionAndRecall_same_count(self):
