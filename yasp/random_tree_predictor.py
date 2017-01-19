# nombre de selection de chaque type
# nombre de hotkey1
# vitesse de jeu

from sklearn import tree
import random
from csvHandler import *
from  sklearn.cross_validation import train_test_split
from  sklearn.cross_validation import cross_val_predict

from sklearn.metrics import accuracy_score
from features import *
fieldnames = ["s","sBase","sMineral","hotkey00","hotkey01","hotkey02","hotkey10","hotkey11","hotkey12","hotkey20","hotkey21","hotkey22","hotkey30","hotkey31","hotkey32","hotkey40","hotkey41","hotkey42","hotkey50","hotkey51","hotkey52","hotkey60","hotkey61","hotkey62","hotkey70","hotkey71","hotkey72","hotkey80","hotkey81","hotkey82","hotkey90","hotkey91","hotkey92"]
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier

features_labels = extract_rows_from_CSV()
Y = features_labels["labels"]
X = calculate_simple_features(features_labels["data"])
generate_features_csv(Y,X)




def produce_random_tree_by_race():

	clf = RandomForestClassifier(n_estimators=50)
	clf = clf.fit(X, Y)
	data_test = extract_rows_from_CSV('../../datayasp/test.csv')
	X_test = calculate_simple_features(data_test["data"])
	Y_test = data_test["labels"]
	predictions = clf.predict(X_test)
	write_to_submit_CSV(Y_test,predictions)
	


def test_random_tree_by_race():
	features_labels = extract_rows_from_CSV()
	Y = features_labels["labels"]
	X = calculate_simple_features(features_labels["data"])
	#compute_most_used_hotkey_feature(X)
	#compute_relative_frequency_hotkey_feature(X)
	generate_features_csv(Y,X)
	clf = RandomForestClassifier(n_estimators=70)
	predicted = cross_val_predict(clf, X, Y, cv=10)
	print metrics.accuracy_score(Y, predicted) 
	

test_random_tree_by_race()