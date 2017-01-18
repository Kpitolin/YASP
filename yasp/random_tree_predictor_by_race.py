from sklearn import tree
from csvHandler import *
from features import *
from  sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

fieldnames = ["s","sBase","sMineral","hotkey00","hotkey01","hotkey02","hotkey10","hotkey11","hotkey12","hotkey20","hotkey21","hotkey22","hotkey30","hotkey31","hotkey32","hotkey40","hotkey41","hotkey42","hotkey50","hotkey51","hotkey52","hotkey60","hotkey61","hotkey62","hotkey70","hotkey71","hotkey72","hotkey80","hotkey81","hotkey82","hotkey90","hotkey91","hotkey92"]

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
		dic[i]["clf"] = RandomForestClassifier(n_estimators=50)
		dic[i]["clf"].fit(dic[i]["features"], dic[i]["labels"])

def predict_race(features, dic, predictions):
	predicted_race = dic[features[0]]["clf"].predict([features])
	predictions=predictions.append(predicted_race[0])


features_labels = extract_rows_from_CSV()
Y = features_labels["labels"]
X = calculate_simple_features(features_labels["data"])
dic = split_train_data(X,Y)
train_splitted_data(dic)
#X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 5)

data_test = extract_rows_from_CSV('../../datayasp/test.csv')
X_test = calculate_simple_features(data_test["data"])
Y_test = data_test["labels"]
predictions = []
for x in X_test:
	predict_race(x,dic,predictions)
write_to_submit_CSV(Y_test,predictions)
print accuracy_score(Y_test, predictions)



