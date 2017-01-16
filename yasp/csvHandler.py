import csv

# Extracts from the csv each row of data




def extractRowsFromCSV():
	"""
	 ExtractRowsFromCSV
	 This method extracts data from the CSV : [PLAYER_NAME, PLAYER_RACE, actions ...]
	"""
	
	arrayOfData  = []
	with open('../../datayasp/train.csv') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			arrayOfData.append(row)
		print arrayOfData[2]
	return arrayOfData