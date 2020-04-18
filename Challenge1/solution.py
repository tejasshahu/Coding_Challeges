# function to get unique values 
def unique(list1): 
	# intilize a null list
	unique_list = []
    # traverse for all elements 
	for x in list1:
        # check if exists in unique_list or not 
		if x not in unique_list:
			unique_list.append(x)
	return unique_list

def create_mocktail(mocktail_possible, sorted_flavours, required_calories, 
					flavour_calories, available=[]):
	"""
	mocktail_possible: int value default 0
	sorted_flavours: sorted list containing all the available flavours
	sorted_unique_flavours: unique sorted list of flavours
	required_calories: in value which is friend's max calories intake
	flavour_calories: dictionary which has the name of flavour as dictionary key and
					specific flavour's calories as dictionary value
	"""
	possible = 0
	total = sum(available)
    # check if the available sum is equals to required_calories
	if total == required_calories and mocktail_possible == False:
		mocktail_possible += 1
		cocktail = ""
		for k in available:
			for key, value in flavour_calories.items():
				if value == k:
					cocktail = "".join((cocktail, key))
		print(cocktail)
		return mocktail_possible
	if total >= required_calories:
		return possible
	for i in range(len(sorted_flavours)):
		if possible == 1:
			break
		else:
			element = flavour_calories[sorted_flavours[i]]
			remaining = sorted_flavours[i+1:]
			possible = create_mocktail(mocktail_possible, remaining, 
				required_calories, flavour_calories, available + [element])
	return possible


file = open("./sampleinput.txt", "r")
# first line is number of invited guest
content = file.readlines()
# first line is number of invited friends
ppl = int(content[0])
for i in range(1, ppl*3, 3):
	list1 = content[i].split()
	number_of_flavour = int(list1[0])
	calories = [int(i) for i in list1[1:]]
	flavours = content[i+1]
	flavours_list = []
	# here len(flavours)-1 is done because last element is \n (newline) while 
	# reading from any file
	for k in range(0, len(flavours) - 1):
		flavours_list.append(flavours[k])
	sorted_flavours = sorted(flavours_list)
	sorted_unique_flavours = unique(sorted_flavours)
	flavour_calories = dict(zip(sorted_unique_flavours, calories))
	# friend's required calories
	required_calories = int(content[i+2])
	mocktail_possible = 0
	result = create_mocktail(mocktail_possible, sorted_flavours, 
		required_calories, flavour_calories)
	if result == 0:
		print("SORRY, YOU JUST HAVE WATER")