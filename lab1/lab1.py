#function that performs / operation
def costPerWeek (num_weeks, num_classes, tuition):
	return  (tuition / num_classes) / (num_weeks)

#function that performs / operation
def costPerClass (weekly_classes, weekly_cost):
	return  (weekly_cost / weekly_classes)

def main():
	#assigns a user input to variable weeksStr
	weeksStr = input("Please enter the number of weeks this semester:  ")
	#assigns a user input to variable classesStr
	classesStr = input("Enter the number of classes you are taking:  ")
	#assigns a user input to variable classesStr
	tuitionStr = input("Please enter your tuition:  ")
	#assigns a user input to variable classes_per_weekStr
	classes_per_weekStr = input("Enter the number of times you have class each week:  ")
	#assigns variable weeks the value of integer form of weeksStr
	weeks = int(weeksStr)
	#assigns varibale classes the value of inter form of classesStr
	classes = int(classesStr)
	#assigns variable tuition the value of integer form of tuitionStr
	tuition = int(tuitionStr)
	#assigns variable classes_per_week the value of integer form of classes_per_weekStr
	classes_per_week = int(classes_per_weekStr)
	#for debug only
	#prints the values of weeks classes and tuition with preceeding messages
	print("Weeks:", weeks, "Classes:", classes, "Tuition:",tuition)
	#calls costPerWeek with the values the user inputted earlier for weeks classes and tuition and assigns the result to variable cost_per_week
	cost_per_week = costPerWeek(weeks, classes, tuition)
	#prints cost per week with a preceeding message
	print("Cost per week:", cost_per_week)
	#calls costPerClass with classes_per_week and cost_per_week as arguments and assigns what gets returned to cost_per_class
	cost_per_class = costPerClass(classes_per_week, cost_per_week)
	#prints cost per class with a preceeding message
	print("Cost per class:", cost_per_class)
	
main()
