import random
import math
import features
from sklearn import tree
from csvHandler import *
from  sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
fieldnames = ["s","sBase","sMineral","hotkey00","hotkey01","hotkey02","hotkey10","hotkey11","hotkey12","hotkey20","hotkey21","hotkey22","hotkey30","hotkey31","hotkey32","hotkey40","hotkey41","hotkey42","hotkey50","hotkey51","hotkey52","hotkey60","hotkey61","hotkey62","hotkey70","hotkey71","hotkey72","hotkey80","hotkey81","hotkey82","hotkey90","hotkey91","hotkey92"]

def calculateFeatures(data):
	features = []
	for game in data:
		game_features = []
		if game[0] == "Protoss": 
			game_features.append(0)
		elif game[0] == "Zerg": 
			game_features.append(1)
		else : 
			game_features.append(2)
		if len(game)>3:
			game_features.append(2*(int(game[-1]) - int(game[2]))/(len(game)-1))
		else : 
			game_features.append(0)
		
		for field in fieldnames:
			game_features.append(game.count(field))
		features.append(game_features)
	return features


features_list = extract_rows_from_CSV()
data_hotkeys = features.compute_hotkeys_distribution_feature(features_list["data"])
print data_hotkeys[0]

features.add_single_feature(data_hotkeys, features.extract_string_feature(features_list["data"],"sBase"))
print data_hotkeys[0]

features.add_single_feature(data_hotkeys, features.extract_string_feature(features_list["data"],"sMineral"))
print data_hotkeys[1]

features.add_single_feature(data_hotkeys, features.extract_race_feature(features_list["data"]))
print data_hotkeys[0]


# #features_labels = extract_rows_from_CSV()
# Y = features_list["labels"]
# X = calculateFeatures(data_hotkeys)

# X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = .33, random_state=int(random.uniform(0,100)))

# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(X_train, Y_train)
# data_test = extract_rows_from_CSV('../../datayasp/test.csv')
# features_test = features.compute_hotkeys_distribution_feature(data_test["data"])
# players_test = data_test["labels"]
# predictions = clf.predict(X_test)
# #write_to_submit_CSV(players_test,predictions)
# print accuracy_score(Y_test, predictions)
 
