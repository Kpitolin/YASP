import csv
import time
from sklearn import tree
import csvHandler
# Handles all kinds of operations for CSV files

fieldresults = ["row ID" , "battleneturl"]




def extract_first_20_second_rows_from_data(raw_data):
	"""
	Takes extract_rows_from_CSV()["data"] in input
	"""

	data_array  = []


	for user_data in raw_data:
		selected_data  = []
		selected_data.append(user_data[0])
		for i in range(2,len(user_data)):
			if i%2 == 0 and int(user_data[i]) < 600 :
				selected_data.append(user_data[i-1])
				selected_data.append(user_data[i])
		data_array.append(selected_data)

			
	return data_array



def extract_same_prop_each_user_from_data(filename = '../../datayasp/train.csv', filterIncompleteRows = True):
	"""
	Takes extract_rows_from_CSV()["data"] in input
	"""

	label_array  = []
	data_array  = []

	name_count = 0
	name_dic = {}

	with open(filename) as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(reader, None)
		for row in reader:
			if (filterIncompleteRows and len(row) > 2) or not filterIncompleteRows:
				if row[0].split(";")[0] in name_dic:
					name_dic[row[0].split(";")[0]] = name_dic[row[0].split(";")[0]] + 1
				else:
					name_dic[row[0].split(";")[0]] = 1

	max_number_of_occurences = min(name_dic.values())

	regulated_name_occurence_dic = dict.fromkeys(name_dic.keys(), max_number_of_occurences)

	with open(filename) as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(reader, None)
		for row in reader:
			if (filterIncompleteRows and len(row) > 2) or not filterIncompleteRows:
				if regulated_name_occurence_dic[row[0].split(";")[0]] > 0:
					regulated_name_occurence_dic[row[0].split(";")[0]] = regulated_name_occurence_dic[row[0].split(";")[0]] - 1
					label_array.append(row[0].split(";")[0])
					row[0] = row[0].split(";")[1]
					data_array.append(row)
				else:
					next(reader, None)

	return {"labels":label_array, "data":data_array}




def extract_rows_from_CSV(filename = '../../datayasp/train.csv', filterIncompleteRows = True):
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
			if (filterIncompleteRows and len(row) > 2) or not filterIncompleteRows:
				label_array.append(row[0].split(";")[0])
				row[0] = row[0].split(";")[1]
				data_array.append(row)
	return {"labels":label_array, "data":data_array}


# Extracts from the csv each row of data
fieldnames = ["user","race","speed","s","sBase","sMineral","hotkey00","hotkey01","hotkey02","hotkey10","hotkey11","hotkey12","hotkey20","hotkey21","hotkey22","hotkey30","hotkey31","hotkey32","hotkey40","hotkey41","hotkey42","hotkey50","hotkey51","hotkey52","hotkey60","hotkey61","hotkey62","hotkey70","hotkey71","hotkey72","hotkey80","hotkey81","hotkey82","hotkey90","hotkey91","hotkey92", "line"]


def generate_features_csv(labels, features):
	"""
	 generate_features_csv
	 This method count the number of each specific action for every game and the speed of the player
	 It creates a new csv
	"""
	with open('../../datayasp/train_count' + str(time.time())+'.csv', 'w') as csv_output:
		writer = csv.writer(csv_output)
		writer.writerow(fieldnames)
		for i in range(len(labels)):
			if i < len(features):
				writer.writerow([labels[i]]+features[i])
			else:
				writer.writerow([labels[i]])


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
	# labels_features = extract_rows_from_CSV()
	# generate_features_csv(labels_features["label"], labels_features["data"])
	print str(extract_same_prop_each_user_from_data()["labels"])

