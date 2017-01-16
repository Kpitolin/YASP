import csv

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

#generate_features_csv()
generate_features_lists()

