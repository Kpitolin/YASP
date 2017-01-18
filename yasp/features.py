from sklearn import tree
import csvHandler



# Features computation to determine specialization of experts

def compute_user_mean_speed_feature(feature_list):
	"""
	Compute user speed

	Format of list [action1,frame1, ...]
	Returns a float with the mean speed
	"""
	return len(feature_list)-1/2*(int(feature_list[-1]) - int(feature_list[2]))



def compute_hotkeys_distribution_feature(list_of_feature_list):
	"""
	Hotkeys distribution
	"""
	list_of_hotkey_dict = []
	for lists in list_of_feature_list:
		hotkey_dic = {}

		for feature in lists:

			# We verify the element is a used hotkey 
			if "hotkey" in feature and "2" in feature :
				feature = feature [:-1]
				print feature
				if feature in hotkey_dic:
					hotkey_dic[feature] = hotkey_dic[feature] + 1
				else:
					hotkey_dic[feature] = 1

		hotkey_list = []
		for x in xrange(0,9):
			if "hotkey" + str(x) in hotkey_dic:
				print "hotkey" + str(x)
				hotkey_list.insert(hotkey_dic["hotkey" + str(x)],x) 
			else:
				hotkey_list.insert(0,x) 

		list_of_hotkey_dict.append(hotkey_list)


	return list_of_hotkey_dict

	


def compute_repetition_pattern_of_hotkeys_feature():
	"""
	Repetition pattern of hotkeys
	"""
	return

if __name__ == "__main__":

	print compute_hotkeys_distribution_feature([["hotkey22", "hotkey22"], ["hotkey32", "hotkey42"], ["hotkey62", "hotkey92"]])
