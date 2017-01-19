import csv
from sklearn import tree
import csvHandler
# Handles all kinds of operations for CSV files

fieldresults = ["row ID" , "battleneturl"]

def extract_rows_from_CSV(filename = '../../datayasp/train.csv'):
	"""
	Training CSV - > label_array:['gamer1','gamer2...]
					data_array:[['s',17, ...]['sBase',456,...]
	"""
	label_array  = []
	data_array  = []
	with open(filename) as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(reader, None)
		for row in reader:
			label_array.append(row[0].split(";")[0])
			row[0] = row[0].split(";")[1]
			data_array.append(row)
	return {"labels":label_array, "data":data_array}


# Extracts from the csv each row of data
fieldnames = ["user","race"",speed","s","sBase","sMineral","hotkey00","hotkey01","hotkey02","hotkey10","hotkey11","hotkey12","hotkey20","hotkey21","hotkey22","hotkey30","hotkey31","hotkey32","hotkey40","hotkey41","hotkey42","hotkey50","hotkey51","hotkey52","hotkey60","hotkey61","hotkey62","hotkey70","hotkey71","hotkey72","hotkey80","hotkey81","hotkey82","hotkey90","hotkey91","hotkey92"]


def generate_features_csv(labels, features):
	"""
	 generate_features_csv
	 This method count the number of each specific action for every game and the speed of the player
	 It creates a new csv
	"""
	with open('../../datayasp/train_count.csv', 'w') as csv_output:
		writer = csv.writer(csv_output)
		for i in range(len(labels)):
			writer.writerow([labels[i]]+features[i])

def write_to_submit_CSV(players,arrayOfResults):
	"""
	Writes the submit  CSV
	"""
	with open('../../datayasp/results.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldresults)
		writer.writeheader()
		for i in range(len(arrayOfResults)):
			writer.writerow({"row ID": players[i], "battleneturl":arrayOfResults[i]})


if __name__ == "__main__":
	# generate_features_csv()
	# generate_features_lists()



	# print extractLabels(extractRowsFromCSV())	testArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Bernard"], ["Row 2", "Jean"]]
	# truthArray = [["row ID","battleneturl"], ["Row 0", "Patrick"], ["Row 1", "Patrick"], ["Row 2", "Jean"],["Row 3", "Bernard"]]
	# print computePrecisionAndRecall(testArray, truthArray)
	labels_features = extract_rows_from_CSV()
	generate_features_csv(labels_features["label"], labels_features["data"])


