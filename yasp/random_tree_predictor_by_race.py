from sklearn import tree
import random
import csvHandler
import features
from  sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, jaccard_similarity_score

fieldnames = ["s","sBase","sMineral","hotkey00","hotkey01","hotkey02","hotkey10","hotkey11","hotkey12","hotkey20","hotkey21","hotkey22","hotkey30","hotkey31","hotkey32","hotkey40","hotkey41","hotkey42","hotkey50","hotkey51","hotkey52","hotkey60","hotkey61","hotkey62","hotkey70","hotkey71","hotkey72","hotkey80","hotkey81","hotkey82","hotkey90","hotkey91","hotkey92", "mostusedhotkey"]

from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

def split_train_data(X,Y):
	dic = {
	0: {"labels" :[],"features":[]},
	1: {"labels" :[],"features":[]} , 
	2: {"labels" :[],"features":[]}
	}
	for i in range(len(Y)):
		dic[X[i][0]]["labels"].append(Y[i])
		dic[X[i][0]]["features"].append(X[i])
	return dic

def train_splitted_data(dic):
	for i in dic:
		dic[i]["clf"] = RandomForestClassifier(n_estimators=65)
		dic[i]["clf"].fit(dic[i]["features"], dic[i]["labels"])

def predict_race(features, dic, predictions):
	predicted_race = dic[features[0]]["clf"].predict([features])
	predictions=predictions.append(predicted_race[0])


def produce_random_tree_by_race():

	features_list = csvHandler.extract_rows_from_CSV()
	first_twenty_seconds_fl = csvHandler.extract_first_20_second_rows_from_data(features_list["data"])
	# raw_data = features.old_compute_simple_features(features_list["data"])
	raw_data = features.old_compute_simple_features(first_twenty_seconds_fl)
	features.add_multiple_features(raw_data, features.compute_hotkeys_distribution_feature(features_list["data"]))

	# features.add_single_feature(raw_data, features.extract_string_feature(features_list["data"],"sBase"))
	features.add_single_feature(raw_data, features.extract_coordination_feature(features_list["data"]))
	# features.add_single_feature(raw_data, features.extract_string_feature(features_list["data"],"sMineral"))
	features.add_single_feature(raw_data, features.extract_race_feature(features_list["data"]))
	features.add_single_feature(raw_data, features.compute_user_mean_speed_feature(features_list["data"]))

	Y = features_list["labels"]
	X = raw_data
	dic = split_train_data(X,Y)
	train_splitted_data(dic)

	data_test = csvHandler.extract_rows_from_CSV('../../datayasp/test.csv', False)["data"]
	data_labels = csvHandler.extract_rows_from_CSV('../../datayasp/test.csv',False)["labels"]
	first_twenty_seconds_fl = csvHandler.extract_first_20_second_rows_from_data(data_test)

	features_test = features.old_compute_simple_features(first_twenty_seconds_fl)
	features.add_multiple_features(features_test, features.compute_hotkeys_distribution_feature(data_test))
	# features.add_single_feature(features_test, features.extract_string_feature(data_test,"sBase"))
	features.add_single_feature(features_test, features.extract_coordination_feature(data_test))

	# features.add_single_feature(features_test, features.extract_string_feature(data_test,"sMineral"))
	features.add_single_feature(features_test, features.extract_race_feature(data_test))
	features.add_single_feature(features_test, features.compute_user_mean_speed_feature(data_test))


	X_test = features_test
	Y_test = data_labels
	predictions = []
	for x in X_test:
		predict_race(x,dic,predictions)
	csvHandler.write_to_submit_CSV(Y_test,predictions)


def test_random_tree_by_race():
	features_labels = extract_rows_from_CSV()




	X = calculate_simple_features(features_labels["data"])
	print X
	compute_most_used_hotkey_feature(X)
	Y = features_labels["labels"]
	generate_features_csv(Y,X)
	X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 5, random_state=int(random.uniform(0,100)))	

	dic = split_train_data(X_train,Y_train)
	train_splitted_data(dic)
	predictions = []
	for x in X_test:
		predict_race(x,dic,predictions)
	print accuracy_score(Y_test, predictions)

if __name__ == "__main__":

	produce_random_tree_by_race()
