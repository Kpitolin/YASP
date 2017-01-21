import unittest, os
import yasp.features



class features_test_case(unittest.TestCase):


	# If the event occured at the current minute, we consider it
	def test_features_add_single_feature_empty_list(self):
		# remove the first element (title rows)
		testArray = [[0, 1], [1,7], [2,3]]
		self.assertEqual(yasp.features.add_single_feature(testArray,[]), testArray)

	def test_features_add_single_feature_mormal_case(self):
		# remove the first element (title rows)
		testArray = [[0, 1], [1,7], [2,3]]
		featureArray = [ 9,4, 6]
		self.assertEqual(yasp.features.add_single_feature(testArray,featureArray), [[0, 1,9], [1,7, 4], [2,3, 6]])


	# If the event occured at the current minute, we consider it
	def test_features_add_multiple_features_values_lacking(self):
		testArray = [[0, 1], [1,7], [2,3]]
		featureArray = [ [90, 100], [50, 20], [30]]
		self.assertEqual(yasp.features.add_multiple_features(testArray,featureArray), [[0, 1, 90, 100], [1,7, 50, 20], [2,3, 30,0]])

	# If the event occured at the current minute, we consider it
	def test_features_add_multiple_features_arrays_lacking(self):
		testArray = [[0, 1], [1,7], [2,3]]
		featureArray = [[90, 100], [50, 20]]
		self.assertEqual(yasp.features.add_multiple_features(testArray,featureArray), [[0, 1, 90, 100], [1,7, 50, 20], [2,3, 0,0]])


	# def test_old_compute_simple_features(self):
	# 	pass


	# def test_compute_relative_frequency_hotkey_feature(self):
	# 	pass


	# def test_compute_most_used_hotkey_feature(self):
	# 	testArray = [["Terran", "1"], ["Zerg","7"], ["Protoss","3"]]
	# 	featureArray = [ ["hotkey20", "hotkey22"], ["hotkey70", "hotkey92"], ["hotkey02"]]
	# 	self.assertEqual(yasp.features.compute_most_used_hotkey_feature(testArray,featureArray))

	def test_compute_user_mean_speed_feature_normal(self):
		array  = [['s', '6256', 's', '6281', 's', '6289', 'hotkey12', '6332', 's', '6343'], ['s', '6647', 'hotkey12', '6672', 'hotkey62', '6697'], 
		['s', '6472', 's', '6486', 'hotkey20', '6492', 'hotkey12', '6514']]
		self.assertEqual(yasp.features.compute_user_mean_speed_feature(array), [6,6,10])

	def test_compute_user_mean_speed_feature_first_frame_missing(self):
		array  = [['s', 's','s'], ['s', 's', 's'], ['s', 's','s']]
		self.assertEqual(yasp.features.compute_user_mean_speed_feature(array), [0,0,0])

	def test_compute_user_mean_speed_feature_unsufficient_length(self):
		array  = [['s'], ['s'], ['s']]
		self.assertEqual(yasp.features.compute_user_mean_speed_feature(array), [0,0,0])

	def test_findIndexOfFirstFrame_normal_case(self):
		self.assertEqual(yasp.features.findIndexOfFirstFrame(['s', '6256', 's', '6281', 's', '6289', 'hotkey12', '6332', 's', '6343']), 1)


	def test_findIndexOfFirstFrame_no_frame_number_case(self):
		self.assertEqual(yasp.features.findIndexOfFirstFrame(["/Life/","Terran","s"]), -1)


	def test_compute_hotkeys_distribution_feature_normal_case(self):
		self.assertEqual(yasp.features.compute_hotkeys_distribution_feature([["hotkey21", "hotkey22"], ["hotkey21", "hotkey20"], ["hotkey62", "hotkey92"]]), 
			[[0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,1]])

	def test_extract_string_feature(self):
		array  = [['s', '6256', 's', '6281', 's', '6289', 'hotkey12', '6332', 's', '6343'], ['s', '6647', 'hotkey12', '6672', 'hotkey62', '6697'], 
		['s', '6472', 's', '6486', 'hotkey20', '6492', 'hotkey12', '6514']]
		self.assertEqual(yasp.features.extract_string_feature(array, "s"), [4,1,2])


	def test_features_extract_string_feature_in_interval_normal(self):
		array  = [['s', '6256', 's', '6281', 's', '6289', 'hotkey12', '6332', 's', '6343'], ['s', '6647', 'hotkey12', '6672', 'hotkey62', '6697'], 
		['s', '6472', 's', '6486', 'hotkey20', '6492', 'hotkey12', '6514']]
		self.assertEqual(yasp.features.extract_string_feature_in_interval(array,"s",0,4), [3,0,2])

	def test_features_extract_string_feature_in_interval_no_occurence(self):
		array  = [['s', '6256', 's', '6281', 's', '6289', 'hotkey12', '6332', 's', '6343'], ['s', '6647', 'hotkey12', '6672', 'hotkey62', '6697'], 
		['s', '6472', 's', '6486', 'hotkey20', '6492', 'hotkey12', '6514']]
		self.assertEqual(yasp.features.extract_string_feature_in_interval(array,"sBase",0,4), [0,0,0])


