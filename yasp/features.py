import math
import functools


def extract_race_feature(raw_features):
	"""
	You must provide it with extract_rows_from_CSV()["data"]
	"""
	feature_list = []
	for i in range(0,len(raw_features)):
		if raw_features[i][0] == "Protoss":
			feature_list.append(0)

		elif raw_features[i][0] == "Zerg":
			feature_list.append(1)

		elif raw_features[i][0] == "Terran":
			feature_list.append(2)

	return feature_list

def extract_coordination_feature(raw_features, min_distance_hotkeys = 6):
	"""
	You must provide it with extract_rows_from_CSV()["data"]
	"""

	feature_list = []
	for i in range(0,len(raw_features)):
		duration_list = []

		for j in range(0,len(raw_features[i])):
			# Take the second to be last char
			first_hotkey = 0
			last_hotkey  = 0
			if "hotkey" in raw_features[i][j] and "hotkey" in raw_features[i][j-2]:
				last_hotkey = int(raw_features[i][j][-2])
				first_hotkey = int(raw_features[i][j-2][-2])

				if last_hotkey-first_hotkey > min_distance_hotkeys:
					first_frame = int(raw_features[i][j-1]) * 30
					last_frame = int(raw_features[i][j+1]) * 30
					duration_list.append(last_frame - first_frame) 
		if duration_list:
			feature_list.append(min(duration_list))
		else:
			feature_list.append(0)


				

	return feature_list

def add_single_feature(data, single_feature_list):
	"""
	Add a feature  [valueGameData1, valueGameData2,...] to the list of features
	"""

	for i in range(0,len(single_feature_list)):
		data[i].append(single_feature_list[i])
	return data

def add_multiple_features(data, multiple_features_list, default_value = 0):
	"""
	The first value must have the right number of features
	Add a feature  [valueGameData1, valueGameData2,...] to the list of features or default value if it's lacking 
	(for the entire row or just some features)
	The features must be sorted in the final order
	"""

	count_of_data_elements = len(data)
	count_of_features_elements = len(multiple_features_list[0])

	for i in range(0,count_of_data_elements):

		for j in range(0,count_of_features_elements):

			if i < len(multiple_features_list):
				if  j < len(multiple_features_list[i]):
					data[i].append(multiple_features_list[i][j])
				else:
					data[i].append(default_value)
			else:
				data[i].append(default_value)


	return data

def extract_string_feature_in_interval(data_list, string_feature, first_action_index, nb_actions):
	"""
	You must provide extract_rows_from_CSV()["data"] as data_list 
	string_feature is s or sBase or sMineral or a hotkey
	"""
	
	feature_list = []
	for i in range(0,len(data_list)):
		count_of_features = 0
		if first_action_index + (nb_actions-1)*2 < len(data_list[i]):
			for j in range(first_action_index,(first_action_index+(nb_actions-1)*2)+1):
				if string_feature == data_list[i][j]:
					count_of_features = count_of_features + 1
		feature_list.append(count_of_features)
				# print feature_list
	return feature_list



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
			if "hotkey" in feature and feature.endswith("2"):
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

def findIndexOfFirstFrame(game_feature_list):

	"""
	If the first frame is found, it resturns its index, otherwise, -1
	"""
	for i in range(len(game_feature_list)):
		if game_feature_list[i].isdigit():
			return i

	return -1

	
def compute_user_mean_speed_feature(raw_features):
	"""
	Compute user speed

	Format of list [action1,frame1, ...]
	Returns a float with the mean speed or 0 if computation is impossible
	"""
	features = []

	for feature_list in raw_features:
		index_first_frame = findIndexOfFirstFrame(feature_list)
		if len(feature_list)>2 and not index_first_frame == -1:
			features.append((2*(len(feature_list)-1) * 30) / (int(feature_list[-1]) - int(feature_list[index_first_frame])))
		else:
			features.append(0)

	return features





def compute_most_used_hotkey_feature(features):

	for game in features:
		hotkey = 0
		max_usage =0
		for i in range(4,len(game)-1):
			if i%3 == 0:
				if max_usage<(game[i]+game[i+1]+game[i+2]):
					max_usage = game[i]+game[i+1]+game[i+2]
					hotkey = (i-6)/3
		game.append(hotkey)


def compute_relative_frequency_hotkey_feature(features):

	for game in features:
		sum = reduce((lambda x, y: x + y), game[7::3])
		for i in range(6,len(game)-1):
			if sum !=0:
				game.append(game[i]*100/sum)
			else :
				game.append(0)



fieldnames = ["s","sBase","sMineral","hotkey00","hotkey01","hotkey02","hotkey10","hotkey11","hotkey12","hotkey20","hotkey21","hotkey22","hotkey30","hotkey31","hotkey32","hotkey40","hotkey41","hotkey42","hotkey50","hotkey51","hotkey52","hotkey60","hotkey61","hotkey62","hotkey70","hotkey71","hotkey72","hotkey80","hotkey81","hotkey82","hotkey90","hotkey91","hotkey92"]


def calculate_simple_features(data):

	"""
	Doesn't compute speed anymore
	"""
	features = []
	i=0
	for game in data:
		if game:
			game_features = []
			if game[0] == "Protoss": 
				game_features.append(0)
			elif game[0] == "Zerg": 
				game_features.append(1)
			else : 
				game_features.append(2)
			for field in fieldnames:
				game_features.append(game.count(field))
			features.append(game_features)
			i=i+1	
		features.append(game_features)
	return features

def old_compute_simple_features(data):
	features = []
	for game in data:
		game_features = []
		if game[0] == "Protoss": 
			game_features.append(0)
		elif game[0] == "Zerg": 
			game_features.append(1)
		else : 
			game_features.append(2)
		for field in fieldnames:
			game_features.append(game.count(field))
		features.append(game_features)
	return features
	


def add_line_number(features):
	for i in range(len(features)):
		features[i].append(i)

if __name__ == "__main__":

	#print add_multiple_features([[0,10,12],[15,20,30]],[[45,64],[9]])
	print compute_hotkeys_distribution_feature([["hotkey21", "hotkey22"], ["hotkey21", "hotkey20"], ["hotkey62", "hotkey92"]])
