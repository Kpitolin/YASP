from features import *
from sklearn import tree
from csvHandler import *
#from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
fieldnames = ["s","sBase","sMineral","hotkey00","hotkey01","hotkey02","hotkey10","hotkey11","hotkey12","hotkey20","hotkey21","hotkey22","hotkey30","hotkey31","hotkey32","hotkey40","hotkey41","hotkey42","hotkey50","hotkey51","hotkey52","hotkey60","hotkey61","hotkey62","hotkey70","hotkey71","hotkey72","hotkey80","hotkey81","hotkey82","hotkey90","hotkey91","hotkey92"]


features_labels = extract_rows_from_CSV()
Y = features_labels["labels"]
X = calculateFeatures(features_labels["data"])
generate_features_csv(Y,X)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 5)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, Y_train)
data_test = extract_rows_from_CSV('../../datayasp/test.csv')
features_test = calculateFeatures(data_test["data"])
players_test = data_test["labels"]
predictions = clf.predict(X_test)
#write_to_submit_CSV(players_test,predictions)
print accuracy_score(Y_test, predictions)
