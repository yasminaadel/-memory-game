list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_of_char = ['A', 'B', 'K', 'Z', 'B', 'M', 'M', 'C', 'Q', 'O', 'N', 'C', 'Q', 'L', 'N', 'Z', 'O', 'L', 'K', 'A']
list_of_stars = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']

# score of player1=index0
# score of player2=index1
score = [0, 0]
round_between_players = 0
Player_num = 1

while (list_of_numbers != list_of_stars):
    print("WELCOME" + str(list_of_numbers))
    print("PLAYER#" + str(Player_num)+"- score " + str(score[Player_num - 1]))
    num1 = int(input("Enter two numbers you want to choose from list:"))
    num2 = int(input())

#check a number is valid or not
    if (num1 > 20 and num1 < 1):
        print("write a valid number")
    elif (num2 > 20 and num2 < 1) :
        print("write a valid number")
    elif (list_of_numbers[num1-1] == '*'):
        print("write a valid number")
    elif (list_of_numbers[num2-1] == '*'):
        print("write a valid number")
    elif (list_of_numbers[num1-1] == list_of_numbers[num2-1]):
        print("write a valid number")
    else:
        round_between_players += 1
        list_of_numbers[num1 - 1] = list_of_char[num1 - 1]
        list_of_numbers[num2 - 1] = list_of_char[num2 - 1]
        print("WELCOME:" + str(list_of_numbers))
        if (list_of_char[num1 - 1] == list_of_char[num2 - 1]):
            list_of_numbers[num1 - 1] = '*'
            list_of_numbers[num2 - 1] = '*'
            score[Player_num - 1] += 1
        else:
            list_of_numbers[num1 - 1] = num1
            list_of_numbers[num2 - 1] = num2

        if (round_between_players % 2 == 0):
            Player_num = 1
        else:
            Player_num = 2

# Score of players
if (score[0] > score[1]):
    print("player1 is win")
elif (score[0] < score[1]):
    print("player2 is win")
else:
    print("Two players are draw")
