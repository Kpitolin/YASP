

def extract_race_feature(raw_features):
	"""
	You must provide it with extract_rows_from_CSV()["data"]
	"""
	feature_list = []
	for i in range(0,len(raw_features)):
		feature_list.append(len(raw_features[i][0]))

	return feature_list

def add_single_feature(data, single_feature_list):
	"""
	Add a feature  [valueGameData1, valueGameData2,...] to the list of features
	"""

	for i in range(0,len(single_feature_list)):
		data[i].append(single_feature_list[i])

	return data

def extract_string_feature(data_list, string_feature):
	"""
	You must provide extract_rows_from_CSV()["data"] as data_list 
	string_feature is s or sBase or sMineral or a hotkey
	"""
	feature_list = []
	for i in range(0,len(data_list)):
		count_of_features = 0
		for feature in data_list[i]:
			if string_feature == feature:
				count_of_features = count_of_features + 1
		feature_list.append(count_of_features)
			# print feature_list
	return feature_list


# Features computation to determine specialization of experts




def compute_hotkeys_distribution_feature(list_of_feature_list):
	"""
	Hotkeys distribution

	List of [[nb_hotkey0_used,nb_hotkey1_used, nb_hotkey2_used, nb_hotkey3_used, ... ] ,...]
	"""
	list_of_hotkey_dict = []
	for lists in list_of_feature_list:
		hotkey_dic = {}

		for feature in lists:

			# We verify the element is a used hotkey 
			if "hotkey" in feature and "2" in feature :
				feature = feature [:-1]
				if feature in hotkey_dic:
					hotkey_dic[feature] = hotkey_dic[feature] + 1
				else:
					hotkey_dic[feature] = 1

		hotkey_list = []
		for x in xrange(0,10):
			if "hotkey" + str(x) in hotkey_dic:
				hotkey_list.insert(x, hotkey_dic["hotkey" + str(x)]) 
			else:
				hotkey_list.insert(x,0) 

		list_of_hotkey_dict.append(hotkey_list)


	return list_of_hotkey_dict

# The following methods were not tested

	
def compute_user_mean_speed_feature(feature_list):
	"""
	Compute user speed

	Format of list [action1,frame1, ...]
	Returns a float with the mean speed
	"""
	return len(feature_list)-1/2*(int(feature_list[-1]) - int(feature_list[2]))


def compute_repetition_pattern_of_hotkeys_feature():
	"""
	Repetition pattern of hotkeys
	"""
	return

if __name__ == "__main__":

	print compute_hotkeys_distribution_feature([["hotkey22", "hotkey22"], ["hotkey32", "hotkey42"], ["hotkey62", "hotkey92"]])
