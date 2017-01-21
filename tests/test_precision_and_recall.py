import unittest, os
import yasp.precision_and_recall



class precision_and_recall_test_case(unittest.TestCase):




	# If the event occured at the current minute, we consider it
	def test_computePrecisionAndRecall_different_count(self):
		# remove the first element (title rows)
		testArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Bernard"], ["Row 2", "Jean"]]
		truthArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Patrick"], ["Row 2", "Jean"],["Row 3", "Bernard"]]
		self.assertEqual(yasp.precision_and_recall.computePrecisionAndRecall(testArray,truthArray),{"precision": 1/3,"recall": 1/4})


	# If the event occured at the current minute, we consider it
	def test_computePrecisionAndRecall_same_count(self):
		testArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Bernard"], ["Row 2", "Jean"],["Row 3", "Jean"]]
		truthArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Patrick"], ["Row 2", "Jean"],["Row 3", "Bernard"], ["Row 4", "popo"]]
		self.assertEqual(yasp.precision_and_recall.computePrecisionAndRecall(testArray,truthArray),{"precision": 1/4,"recall": 2/5})

