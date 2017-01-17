import csv
from sklearn import tree
import csvHandler
# Handles all kinds of operations for CSV files

def extractLabels(rows):
	"""
	Utils methods to extract labels out of the training set
	"""
	rows = rows[1:]
	arrayOfLabels  = []
	i = 0
	for row in rows:
		arrayOfLabels.append(row[0])
		i = i+1
	return arrayOfLabels

def generateResultRows(rows):
	"""
	Format a row to the expect format : rowId, battlenetUrl
	"""
	rows = rows[1:]
	arrayOfLabels  = []
	i = 0
	for row in rows:
		arrayOfLabels.append(["Row"+str(i), row[0]])
		i = i+1
	return arrayOfLabels


def extractRowsFromCSV(filename = '../../datayasp/train.csv'):
	"""
	Training CSV - > [['battleneturl',['s',17, ...]],...]
	"""
	arrayOfData  = []

	with open(filename) as csvfile:
		reader = csv.reader(csvfile, delimiter=';')
		for row in reader:
			arrayOfData.append(row)

		i = 0
		for i in range(0,len(arrayOfData)):
			arrayOfActions = arrayOfData[i][1].split(',')
			arrayOfData[i][1]= arrayOfActions
	return arrayOfData


# Extracts from the csv each row of data
fieldnames = ["user","speed","s","sBase","sMineral","hotkey00","hotkey01","hotkey02","hotkey10","hotkey11","hotkey12","hotkey20","hotkey21","hotkey22","hotkey30","hotkey31","hotkey32","hotkey40","hotkey41","hotkey42","hotkey50","hotkey51","hotkey52","hotkey60","hotkey61","hotkey62","hotkey70","hotkey71","hotkey72","hotkey80","hotkey81","hotkey82","hotkey90","hotkey91","hotkey92"]


def generate_features_csv():
	"""
	 generate_features_csv
	 This method count the number of each specific action for every game and the speed of the player
	 It creates a new csv
	"""

	with open('../../datayasp/train.csv') as csv_input:
		with open('../../datayasp/train_count.csv', 'w') as csv_output:
			reader = csv.reader(csv_input, delimiter=',')
			writer = csv.DictWriter(csv_output, fieldnames=fieldnames,dialect='excel')
			features_map = {}
			next(reader, None)
			writer.writeheader()
			for row in reader:
				for field in fieldnames:
					if len(row)>3:
						features_map[field] = row.count(field)
						features_map["speed"] = len(row)-1/2*(int(row[-1]) - int(row[2]))
						features_map["user"] = row[0].split(";")[0]
				writer.writerow(features_map)


def generate_features_array(array):
	"""
	generate_features_csv
	This method count the number of each specific action for every game and the speed of the player
	It creates a new csv
	"""

	with open('../../datayasp/train_count.csv', 'w') as csv_output:
		writer = csv.DictWriter(csv_output, fieldnames=fieldnames,dialect='excel')
		features_map = {}
		writer.writeheader()
		for row in array:
			for field in fieldnames:
				if len(row)>2:
					features_map[field] = row.count(field)
					features_map["speed"] = len(row)-1/2*(int(row[-1]) - int(row[2]))
					features_map["user"] = row[0].split(";")[0]
			writer.writerow(features_map)


def generate_features_lists():
	"""
	generate_features_lists
	This method read the csv and create a list with the layer and a list with the features
	"""

	players = []
	features = []
	with open('../../datayasp/train_count.csv') as csv_file:
		reader = csv.reader(csv_file, delimiter=',')
		next(reader, None)
		for row in reader:
			players.append(row[0])
			features.append(row[1:len(row)])
			print(players[-1])
			print(features[-1])

	return {"players":players,"features":features}



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



def writeToSubmitCSV(arrayOfResults):
	"""
	Writes the submit  CSV
	"""
	with open('../../datayasp/results.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		writer.writerow(['row ID','battleneturl'])
		for array in arrayOfResults:
			writer.writerow(array)


if __name__ == "__main__":
	# generate_features_csv()
	# generate_features_lists()



	# print extractLabels(extractRowsFromCSV())	testArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Bernard"], ["Row 2", "Jean"]]
	# truthArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Patrick"], ["Row 2", "Jean"],["Row 3", "Bernard"]]
	# print computePrecisionAndRecall(testArray, truthArray)
	print extractRowsFromCSV()

