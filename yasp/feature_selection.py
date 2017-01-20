
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.datasets import make_classification

import csvHandler
import features


# Build a classification task using 3 informative features


features_list = csvHandler.extract_rows_from_CSV()
first_twenty_seconds_fl = csvHandler.extract_first_20_second_rows_from_data(features_list["data"])
# raw_data = features.old_compute_simple_features(features_list["data"])
raw_data = features.old_compute_simple_features(first_twenty_seconds_fl)
features.add_multiple_features(raw_data, features.compute_hotkeys_distribution_feature(features_list["data"]))

# features.add_single_feature(raw_data, features.extract_string_feature_in_interval(features_list["data"],"s",1,4))
features.add_single_feature(raw_data, features.extract_string_feature(features_list["data"],"sBase"))
features.add_single_feature(raw_data, features.extract_string_feature(features_list["data"],"sMineral"))
features.add_single_feature(raw_data, features.extract_race_feature(features_list["data"]))
features.add_single_feature(raw_data, features.compute_user_mean_speed_feature(features_list["data"]))

Y = features_list["labels"]
X = raw_data

# Create the RFE object and compute a cross-validated score.
svc = SVC(kernel="linear")
# The "accuracy" scoring is proportional to the number of correct
# classifications
rfecv = RFECV(estimator=svc, step=1, cv=StratifiedKFold(2),
              scoring='accuracy')
rfecv.fit(X, Y)

print("Optimal number of features : %d" % rfecv.n_features_)

# Plot number of features VS. cross-validation scores
plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (nb of correct classifications)")
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
plt.show()