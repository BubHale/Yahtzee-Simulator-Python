from random import randint

roll_dice = []
my_dice = []
score = 0
category = [1,2,3,4,5,6]
potential_low_score = [0]*6
histogram = [0]*6
potential_high_score = [0]*7
straight_scoring_checker = [False]*6
scoring_category_checker = [False]*13

def check_one(i):
    if (i == 0 and histogram[i] >= 1):
        straight_scoring_checker[i] = True
    return
def check_two(i):
    if (i == 1 and histogram[i] >= 1):
        straight_scoring_checker[i] = True
    return
def check_three(i):
    if (i == 2 and histogram[i] >= 1):
        straight_scoring_checker[i] = True
    return
def check_four(i):
    if (i == 3 and histogram[i] >= 1):
        straight_scoring_checker[i] = True
    return
def check_five(i):
    if (i == 4 and histogram[i] >= 1):
        straight_scoring_checker[i] = True
    return
def check_six(i):
    if (i == 5 and histogram[i] >= 1):
        straight_scoring_checker[i] = True
    return
def calculate_two(i, two_exist):
    if (histogram[i] == 2):
        two_exist = True
    return
def calculate_three_of_a_kind(list, i, three_exist):
    if (histogram[i] > 2):
        potential_high_score[0] = sum(list)
        if (histogram[i] == 3):
           three_exist = True
    return
def calculate_four_of_a_kind(list, i):
    if (histogram[i] > 3):
        potential_high_score[1] = sum(list)
    return
def calculate_full_house(i, two_exist, three_exist):
    if (two_exist == True and three_exist == True):
        potential_high_score[2] = 25
    return
def calculate_small_straight():
    if (straight_scoring_checker[0] == True and
        straight_scoring_checker[1] == True and
        straight_scoring_checker[2] == True and
        straight_scoring_checker[3] == True or
        straight_scoring_checker[1] == True and
        straight_scoring_checker[2] == True and
        straight_scoring_checker[3] == True and
        straight_scoring_checker[4] == True or
        straight_scoring_checker[2] == True and
        straight_scoring_checker[3] == True and
        straight_scoring_checker[4] == True and
        straight_scoring_checker[5] == True
        ):
        potential_high_score[3] = 30
    return
def calculate_large_straight():
    if (straight_scoring_checker[0] == True and 
        straight_scoring_checker[1] == True and
        straight_scoring_checker[2] == True and
        straight_scoring_checker[3] == True and
        straight_scoring_checker[4] == True or
        straight_scoring_checker[1] == True and
        straight_scoring_checker[2] == True and
        straight_scoring_checker[3] == True and
        straight_scoring_checker[4] == True and
        straight_scoring_checker[5] == True
        ):
        potential_high_score[4] = 40
    return
def calculate_chance(list):
    potential_high_score[5] = (sum(list))
    return
def calculate_yahtzee(i):
    if histogram[i] >= 5:
        potential_high_score[6] = 50
    return
def print_potential_score():
    print("Current potential low point opportunities:")
    index = 0
    for i in potential_low_score:
        print("Index:"+str(index+1)+str(category[index])+"'s "+str(potential_low_score[index])+" points")
        index = index+1
    index = 0
    print("Current potential high point opportunities:")
    for i in potential_high_score:
        if (index == 0):
            print("Index:"+str(index+7)+" Three of a kind:"+str(potential_high_score[index])+" points")
        if (index == 1):
            print("Index:"+str(index+7)+" Four of a kind:"+str(potential_high_score[index])+" points")
        if (index == 2):
            print("Index:"+str(index+7)+" Full House:"+str(potential_high_score[index])+" points")
        if (index == 3):
            print("Index:"+"A"+" Small Straight:"+str(potential_high_score[index])+" points")
        if (index == 4):
            print("Index:"+"B"+" Large Straight:"+str(potential_high_score[index])+" points")
        if (index == 5):
            print("Index:"+"C"+" Chance:"+str(potential_high_score[index])+" points")
        if (index == 6):
            print("Index:"+"D"+" YAHTZEE:"+str(potential_high_score[index])+" points")
        index = index+1
    return
def pick_potential_score():
    print_potential_score()
    user_input = input("Enter the index of the potential score you want to add to your score")
    while (user_input.upper() != '1' and user_input.upper() != '2' and
           user_input.upper() != '3' and user_input.upper() != '4' and
           user_input.upper() != '5' and user_input.upper() != '6' and
           user_input.upper() != '7' and user_input.upper() != '8' and
           user_input.upper() != '9' and user_input.upper() != 'A' and
           user_input.upper() != 'B' and user_input.upper() != 'C' and
           user_input.upper() != 'D'
           ):
        user_input = input("Acceptable entries are: Indexes 1-9, 'A', 'B', 'C', or 'D' you entered:"+user_input+" please try again:")
    if user_input.upper() == "1":
        if scoring_category_checker[0] == False:
            scoring_category_checker[0] = True
            score = score + potential_low_score[0]
    elif user_input.upper() == "2":
        if scoring_category_checker[1] == False:
            scoring_category_checker[1] = True
            score = score + potential_low_score[1]
    elif user_input.upper() == "3":
        if scoring_category_checker[2] == False:
            scoring_category_checker[2] = True
            score = score + potential_low_score[2]
    elif user_input.upper() == "4":
        if scoring_category_checker[3] == False:
            scoring_category_checker[3] = True
            score = score + potential_low_score[3]
    elif user_input.upper() == "5":
        if scoring_category_checker[4] == False:
            scoring_category_checker[4] = True
            score = score + potential_low_score[4]
    elif user_input.upper() == "6":
        if scoring_category_checker[5] == False:
            scoring_category_checker[5] = True
            score = score + potential_low_score[5]
    elif user_input.upper() == "7":
        if scoring_category_checker[6] == False:
            scoringscoring_category_checker[6] = True
            score = score + potential_high_score[0]
    elif user_input.upper() == "8":
        if scoring_category_checker[7] == False:
            scoringscoring_category_checker[7] = True
            score = score + potential_high_score[1]
    elif user_input.upper() == "9":
        if scoring_category_checker[8] == False:
            scoringscoring_category_checker[8] = True
            score = score + potential_high_score[2]
    elif user_input.upper() == "A":
        if scoring_category_checker[9] == False:
            scoringscoring_category_checker[9] = True
            score = score + potential_high_score[3]
    elif user_input.upper() == "B":
        if scoring_category_checker[10] == False:
            scoringscoring_category_checker[10] = True
            score = score + potential_high_score[4]
    elif user_input.upper() == "C":
        if scoring_category_checker[11] == False:
            scoringscoring_category_checker[11] = True
            score = score + potential_high_score[5]
    elif user_input.upper() == "D":
        if scoring_category_checker[12] == False:
            scoringscoring_category_checker[12] = True
            score = score + potential_high_score[6]
    histogram = [0,0,0,0,0,0]
    potential_high_score = [0,0,0,0,0,0,0]
    potential_low_score = [0,0,0,0,0,0]
    my_dice.clear()
    roll_dice.clear()

    return
def potential_scoring_logic():
    straight_scoring_checker = [False, False, False, False, False, False]
    two_exist = False
    three_exist = False
    histogram = [0,0,0,0,0,0]
    potential_high_score = [0,0,0,0,0,0,0]
    potential_low_score = [0,0,0,0,0,0]

    temp_dice = roll_dice + my_dice
    temp_dice.sort()
    index_one = 0
    for i in category:
        index_two = 0
        for j in temp_dice:
            if temp_dice[index_two] == category[index_one]:
                potential_low_score[index_one] = potential_low_score[index_one] + category[index_one]
                histogram[index_one] = histogram[index_one] + 1
            index_two = index_two + 1
        index_one = index_one+1
    index_one = 0
    for i in histogram:
        check_one(index_one)
        check_two(index_one)
        check_three(index_one)
        check_four(index_one)
        check_five(index_one)
        check_six(index_one)

        calculate_two(index_one, two_exist)
        calculate_three_of_a_kind(temp_dice, index_one, three_exist)
        calculate_four_of_a_kind(temp_dice, index_one)
        calculate_full_house(index_one, two_exist, three_exist)
        calculate_small_straight()
        calculate_large_straight()
        calculate_chance(temp_dice)
        calculate_yahtzee(index_one)
    temp_dice.clear()

def print_dice(list):
    index = 1
    for i in list:
        print("Index:"+str(index)+" "+str(list[index-1])) #This line adds 1 to i instead of just printing i + 1
        index = index + 1
    return
def my_dice_to_roll_dice(index, user_input, pile_input):
    if (pile_input.upper() == 'B' and len(my_dice) > 0):
        while index-1 > len(my_dice)-1 or index-1 < 0:
            print_dice(my_dice)
            user_input("That is not a valid index in your pile please try again:")
            index = int(user_input)
        roll_dice.append(my_dice[index-1])
        my_dice.pop(index-1)
    elif (pile_input.upper() == 'B' and len(my_dice) > 0):
        print("You can't transfer from that pile since it is empty; the specified index will be transferred from roll dice instead.")
        pile_input = "A"
        if (pile_input.upper() == 'A' and len(roll_dice) > 0):
            while index-1 > len(roll_dice) or index-1 < 0:
                print_dice(roll_dice)
                user_input("That is not a valid index in roll pile please try again:")
                index = int(user_input)
            my_dice.append(roll_dice[index-1])
            roll_dice.pop(index-1)
    return
def roll_dice_to_my_dice(index, user_input, pile_input):
    if pile_input.upper() == "A" and len(roll_dice) > 0:
        while index-1 > len(roll_dice)-1 or index-1 < 0:
            print_dice(roll_dice)
            user_input = input("That is not a valid index in roll pile please try again:")
        my_dice.append(roll_dice[index-1])
        roll_dice.pop(index-1)
    elif pile_input.upper() == "A" and len(roll_dice) == 0:
        print("You can't transfer from that pile since it is empty; the specified index will be transferred from your dice instead.")
        pile_input = "B"
        if pile_input.upper == "B" and len(my_dice) > 0:
            while index-1 > len(my_dice) and index-1 < 0:
                print_dice(my_dice)
                user_input = input("That is not a valid index in your pile please try again:")
            roll_dice.append(my_dice[index-1])
            my_dice.pop(index-1)
            pile_input = "A"
    return
def reroll_logic(int):
    while int < 3:
        potential_scoring_logic()
        print_potential_score()
        user_input = input("Enter the index of the dice you want to keep or push back to roll pile; Enter R to reroll or Enter C to pick score:")
        while (user_input.upper() != "R" and user_input.upper() != "C" and
               user_input.upper() != "1" and user_input.upper() != "2" and
               user_input.upper() != "3" and user_input.upper() != "4" and
               user_input.upper() != "5"
               ):
            user_input = input("Acceptable entries are 'R', 'C', or Indexes 1-5. You entered:"+user_input+" please try again:")
        if (user_input.upper() == "R"):
            index = 0
            for i in roll_dice:
                roll_dice[i] = randint(1,6)
            int = int + 1
            sort(roll_dice)
            sort(my_dice)
            print("Your dice:")
            print_dice(my_dice)
            print("Roll dice:")
            print_dice(roll_dice)
            if int == 3:
                potential_scoring_logic()
                pick_potential_score()
        elif(user_input.upper() == "C"):
            pick_potential_score()
            int = 3
        else:
            user_index = int(user_input)
            pile_input = input("Enter 'A' if your transferring an index from roll pile to your pile; Enter 'B' if you're transferring an index from your pile to the roll pile:")
            while (pile_input != "A" and pile_input != "B"):
                pile_input = input("Only acceptable entries are 'A'(rollpile->yourpile) or 'B'(yourpile->rollpile) please try again:")
            roll_dice_to_my_dice(index, user_input, pile_input)
            my_dice_to_roll_dice(index, user_input, pile_input)
            sort(my_dice)
            sort(roll_dice)
            print("Your dice:")
            print_dice(my_dice)
            print("Roll dice:")
            print_dice(roll_dice)
       
    return
def first_roll_logic(str,int):
    if str.upper() == "R":
        for i in range(5):
            roll_dice.append(randint(1,6))
        int = int+1
        roll_dice.sort()
        print("Roll dice:")
        print_dice(roll_dice)
    return
def play_yahtzee():
    for i in range(13):
        num_roll = 0
        print("Round:"+str(i+1))
        print("Score:"+str(score))
        user_input = input("Press R to roll dice:")
        while user_input.upper() != "R":
            user_input = input("Only acceptable entry is 'R'; you entered:"+user_input+" please try again:")
        first_roll_logic(user_input,num_roll)
        reroll_logic(num_roll)
    print("Your score to end the game is:"+str(score))


    return

play_yahtzee()