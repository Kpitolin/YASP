import unittest, os
import yasp.csvHandler



# class csvHandlerTestCase(unittest.TestCase):


# 	def setUp(self):
		

# 	def tearDown(self):
# 		folderpath= "."
# 		pattern_file_title =  r"(partialIndex*|InvertedFile|Offsets)"
# 		files = [join(folderpath, f) for f in listdir(folderpath) if isfile(join(folderpath, f)) and re.match(pattern_file_title, f)]
# 		for filename in files:
# 			self.delete_file(filename)


	# # If the event occured at the current minute, we consider it
	# def test_extract_first_20_second_rows_from_data(self):
	# 	# remove the first element (title rows)
	# 	testArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Bernard"], ["Row 2", "Jean"]]
	# 	truthArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Patrick"], ["Row 2", "Jean"],["Row 3", "Bernard"]]
	# 	self.assertEqual(yasp.csvHandler.computePrecisionAndRecall(testArray,truthArray),{"precision": 1/3,"recall": 1/4})


	# # If the event occured at the current minute, we consider it
	# def test_extract_same_prop_each_user_from_data(self):
	# 	testArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Bernard"], ["Row 2", "Jean"],["Row 3", "Jean"]]
	# 	truthArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Patrick"], ["Row 2", "Jean"],["Row 3", "Bernard"], ["Row 4", "popo"]]
	# 	self.assertEqual(yasp.csvHandler.computePrecisionAndRecall(testArray,truthArray),{"precision": 1/4,"recall": 2/5})

	# # If the event occured at the current minute, we consider it
	# def test_extract_rows_from_CSV(self):
	# 	testArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Bernard"], ["Row 2", "Jean"],["Row 3", "Jean"]]
	# 	truthArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Patrick"], ["Row 2", "Jean"],["Row 3", "Bernard"], ["Row 4", "popo"]]
	# 	self.assertEqual(yasp.csvHandler.computePrecisionAndRecall(testArray,truthArray),{"precision": 1/4,"recall": 2/5})

	# # If the event occured at the current minute, we consider it
	# def test_computePrecisionAndRecall_same_count(self):


