from sklearn import tree
import random
from csvHandler import *
from features import *
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
		dic[i]["clf"] = RandomForestClassifier(n_estimators=100)
		dic[i]["clf"].fit(dic[i]["features"], dic[i]["labels"])

def predict_race(features, dic, predictions):
	predicted_race = dic[features[0]]["clf"].predict([features])
	predictions=predictions.append(predicted_race[0])


def produce_random_tree_by_race():
	features_labels = extract_rows_from_CSV()
	Y = features_labels["labels"]
	X = calculate_simple_features(features_labels["data"])
	dic = split_train_data(X,Y)
	train_splitted_data(dic)
	data_test = extract_rows_from_CSV('../../datayasp/test.csv',  False)
	X_test = calculate_simple_features(data_test["data"])
	Y_test = data_test["labels"]
	predictions = []
	for x in X_test:
		predict_race(x,dic,predictions)
	write_to_submit_CSV(Y_test,predictions)


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

	test_random_tree_by_race()
