import csvHandler

def computePrecisionAndRecallFromFiles(filename_test, filename_truth):


	# we extract lists from the csv  
	testArray = extractRowsFromCSV(filename_test)
	truthArray = extractRowsFromCSV(filename_truth)
	return computePrecisionAndRecall(testArray,truthArray)


def computePrecisionAndRecall(testArray, truthArray):
	"""
	p = tp/tp+fp
	r = tp/tp+fn
	Assumes both files are following the format :
	row ID,battleneturl
	Row0,/Stork/
	"""
	# remove the first element (title rows)
	testArray = testArray[1:]
	truthArray = truthArray[1:]
	testArrayCount = len(testArray)
	truthArrayCount = len(truthArray)

	tp = 0
	truth_index = 0
	prediction_index = 0

	while testArray:
		
		if testArray[prediction_index][0] == truthArray[truth_index][0]:
			if testArray[prediction_index][1] == truthArray[truth_index][1]:
				tp = tp + 1
			testArray = testArray[prediction_index+1:]
			prediction_index = prediction_index - 1


		truthArray = truthArray[truth_index+1:]
		truth_index = truth_index - 1

		prediction_index = prediction_index + 1
		truth_index = truth_index + 1

	
	return {"precision": tp/testArrayCount, "recall":  tp/truthArrayCount}