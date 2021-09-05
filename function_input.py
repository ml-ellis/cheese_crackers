def cheese_and_crackers(ratio, cheese_count, crackers):

    # calculate the number of crackers needed for the given cheese_count
    crackers_needed_for_cheese = int(cheese_count / ratio)
    # decide if there are any crackers leftover
    crackers_leftover = crackers - crackers_needed_for_cheese

    #case in which you have leftover crackers and need more cheese
    if (crackers_leftover > 0):
        print(f"You have {crackers_leftover} crackers leftover. You need {ratio*crackers_leftover} more cheeses")

    #case in which you have leftover cheese and need more crackers
    elif (crackers < crackers_needed_for_cheese):
        print(f"You have {(crackers_needed_for_cheese - crackers)*ratio} cheeses leftover. You need {crackers_needed_for_cheese - crackers} more crackers.")
    #case in which you select the correct amount of cracker to cheese per your ratio
    else:
        print("You have chosen a sufficient amount of snack :)")




cheese_count = int(input("How much cheese do you want?\n"))
crackers = int(input("How many crackers do you want?\n"))
ratio = int(input("How many cheeses do you usually apply to each cracker?\n"))

cheese_and_crackers(ratio, cheese_count, crackers)
