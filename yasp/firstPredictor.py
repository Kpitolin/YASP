import random
import math
from sklearn.model_selection import train_test_split
from sklearn import tree
import csvHandler
import features
import random_tree_predictor_by_race
from sklearn.ensemble import RandomForestClassifier

#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn.metrics import accuracy_score, jaccard_similarity_score, f1_score
from sklearn.tree import DecisionTreeClassifier
fieldnames = ["s","sBase","sMineral","hotkey00","hotkey01","hotkey02","hotkey10","hotkey11","hotkey12","hotkey20","hotkey21","hotkey22","hotkey30","hotkey31","hotkey32","hotkey40","hotkey41","hotkey42","hotkey50","hotkey51","hotkey52","hotkey60","hotkey61","hotkey62","hotkey70","hotkey71","hotkey72","hotkey80","hotkey81","hotkey82","hotkey90","hotkey91","hotkey92"]





def produce_new_test(n_estimators_rf=50):

	features_list = csvHandler.extract_rows_from_CSV()
	first_twenty_seconds_fl = csvHandler.extract_first_20_second_rows_from_data(features_list["data"])
	# raw_data = features.old_compute_simple_features(features_list["data"])
	raw_data = features.old_compute_simple_features(first_twenty_seconds_fl)
	features.add_multiple_features(raw_data, features.compute_hotkeys_distribution_feature(features_list["data"]))

	features.add_single_feature(raw_data, features.extract_string_feature(features_list["data"],"sBase"))
	features.add_single_feature(raw_data, features.extract_string_feature(features_list["data"],"sMineral"))
	features.add_single_feature(raw_data, features.extract_race_feature(features_list["data"]))
	features.add_single_feature(raw_data, features.compute_user_mean_speed_feature(features_list["data"]))

	Y = features_list["labels"]
	X = raw_data


	clf = RandomForestClassifier(n_estimators=n_estimators_rf)
	clf = clf.fit(X, Y)


	data_test = csvHandler.extract_rows_from_CSV('../../datayasp/test.csv', False)["data"]
	data_labels = csvHandler.extract_rows_from_CSV('../../datayasp/test.csv',False)["labels"]
	first_twenty_seconds_fl = csvHandler.extract_first_20_second_rows_from_data(data_test)

	features_test = features.old_compute_simple_features(first_twenty_seconds_fl)
	features.add_multiple_features(features_test, features.compute_hotkeys_distribution_feature(data_test))
	features.add_single_feature(features_test, features.extract_string_feature(data_test,"sBase"))
	features.add_single_feature(features_test, features.extract_string_feature(data_test,"sMineral"))
	features.add_single_feature(features_test, features.extract_race_feature(data_test))
	features.add_single_feature(features_test, features.compute_user_mean_speed_feature(data_test))
	X_test = features_test
	Y_test = data_labels
	predictions = clf.predict(X_test)

	csvHandler.write_to_submit_CSV(Y_test,predictions)

	

def test_with_new_features(n_estimators_rf = 50):



	features_list = csvHandler.extract_rows_from_CSV()
	first_twenty_seconds_fl = csvHandler.extract_first_20_second_rows_from_data(features_list["data"])
	# raw_data = features.old_compute_simple_features(features_list["data"])
	raw_data = features.old_compute_simple_features(first_twenty_seconds_fl)
	features.add_multiple_features(raw_data, features.compute_hotkeys_distribution_feature(features_list["data"]))

	features.add_single_feature(raw_data, features.extract_string_feature_in_interval(features_list["data"],"s",1,4))
	features.add_single_feature(raw_data, features.extract_string_feature(features_list["data"],"sBase"))
	features.add_single_feature(raw_data, features.extract_string_feature(features_list["data"],"sMineral"))
	features.add_single_feature(raw_data, features.extract_race_feature(features_list["data"]))
	features.add_single_feature(raw_data, features.compute_user_mean_speed_feature(features_list["data"]))

	Y = features_list["labels"]
	X = raw_data

	print X
	clf = RandomForestClassifier(n_estimators=n_estimators_rf)
	clf = clf.fit(X, Y)


	print "Cross val: " + str(cross_val_score(clf,X,Y, cv=10))




# Zineb old method
def test_with_classic_features():

	features_labels = csvHandler.extract_rows_from_CSV()
	Y = features_labels["labels"]
	X = features.calculate_simple_features(features_labels["data"])
	csvHandler.generate_features_csv(Y,X)

	X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 5, random_state=int(random.uniform(0,100)))

	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(X_train, Y_train)
	data_test = csvHandler.extract_rows_from_CSV('../../datayasp/train.csv')["data"][:400]

	data_labels = csvHandler.extract_rows_from_CSV('../../datayasp/train.csv')["labels"][:400]

	features_test = features.calculate_simple_features(data_test)
	players_test = data_labels
	predictions = clf.predict(X_test)
	#write_to_submit_CSV(players_test,predictions)
	#print f1_score(Y_test, predictions, labels=[x for x in range(0,400)], average= 'macro')
	print accuracy_score(Y_test, predictions)
	# print jaccard_similarity_score(Y_test, predictions)


if __name__ == "__main__":
	# produce_new_test(65)
	# print "Classic"
	# test_with_classic_features()
	print "New 65"
	test_with_new_features(65)	

	# print "random_tree_predictor_by_race"
	# random_tree_predictor_by_race.test_random_tree_by_race()
	# features_list = csvHandler.extract_rows_from_CSV()


	# features.compute_user_mean_speed_feature(features_list["data"])