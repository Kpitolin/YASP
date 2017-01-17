from sklearn import tree
import csvHandler


# nombre de selection de chaque type
# nombre de hotkey1
# vitesse de jeu

# X = [[0, 0], [1, 1]]
# Y = [0, 1]
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(X, Y)
# clf.predict([[2., 2.]])


features_list = csvHandler.generate_features_list()
labels = csvHandler.extractLabels(csvHandler.extractRowsFromCSV())
toPredict = csvHandler.generate_features_array(csvHandler.extractRowsFromCSV()[2][1:])

clf = tree.DecisionTreeClassifier()

print features_list[0]
print labels[0]
# clf = clf.fit(features_list, labels)
# clf.predict(toPredict)