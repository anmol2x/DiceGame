import random
import sqlite3

# Displaying a menu to choice from...
def menu_choice():
    print('\nOption 1: Display rules')
    print('Option 2: Start new game')
    print('Option 3: Display top 5 Players')
    print('Option 4: Quit')
    choice= int(input('What would you like to do?'))
    while int(choice) < 1 or int(choice) > 4:
        print('That is not a valid choice.')
        print('Please enter a number between 1 and 3:')
        choice=input()
    return choice
  
#Subroutines to display rules
def displayRules():
    print('\nThe rules of the game are as follows:')
    print('  Players take turms to throw two dice.')
    print("  If the throw is a 'double', i.e. two 2s, two 3s, etc.,")
    print("  the player's score reverts to zero and their turn ends")
    print('  (etc,)\n')

# saving winner name and score in a file named winners.txt
def save_to_file(player, score):
    file = open("winners.txt", 'a')
    file.write(player + ", " + str(score) + "\n")
    file.close()

def diplay_top_5():
    file = open("winners.txt", 'r')
    # reading lines from the file...
    data = file.readlines()

    # getting name and thier scores into the tuples...
    names_and_scores = [(l.strip().split(',')[0], int(l.strip().split(',')[1])) for l in data]

    # Sorting the tuple py names...
    names_and_scores.sort(key=lambda x: x[1], reverse=True)

    # Printing top 5 values from the list...
    print("\nTop 5 players and scores and given below:")
    for i in range(5):
        print("Player: ", names_and_scores[i][0], "  Score: ", names_and_scores[i][1])

#Subroutine for each player to take a turn
def playerTurn(player,score):
    print('\nYour turn, ',player)
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print('You rolled ',die1, ' and ',die2)
    
    total_score = die1 + die2

    # If total of this round is even number then add 10 points more else subract 5 points...
    if total_score%2 == 0:
        total_score = total_score + 10
    else:
        total_score = total_score - 5
    
    # If user scored a double then roll one extra die add its score to the round's total...
    if die1 == die2:
        die_extra = random.randint(1,6)
        print("wow you rolled a double extra die score is : ", die_extra)
        total_score = total_score + die_extra
    
    # Check score if less than 0 then make it 0...
    if total_score < 0:
        total_score = 0

    print(player, "'s this rounds score is ", total_score)

    return total_score

# Function to play Game...
def playGame():
    # Getting player one form user and validating that player...
    player1 = input("\nEnter Player1's name: ")
    while not valid_player(player1):
        player1 = input("This player is not authorized to play.\nAgain enter Player1's name: ")

    # Getting player two from the user and validating it as well...
    player2 = input("Enter Player2's name: ")
    while not valid_player(player2) or player1 == player2:
        if player1 == player2:
            player2 = input("Player1 and Player2 can not be same.\nAgain enter Player2's name: ")
        else:
            player2 = input("This player is not authorized to play.\nAgain enter Player2's name: ")

    score1 = 0
    score2 = 0

    # Playing game for 5 rounds...
    for i in range(5):
        print("\n\nCurrent round is: ", i+1)

        # Playing player1's turn of this round...
        score1 = score1 + playerTurn(player1,score1)
        print(player1, "'s total score = ", score1)

        # Playing player2's turn of this round...
        score2 = score2 + playerTurn(player2,score2)
        print(player2, "'s total score = ", score2)

        any_key = input("Press enter to continue...")

    # rolling one die untill the score are not equal...
    while score1 == score2:
        # roll a die for player...
        die = random.randint(1,6)
        # add to player1's score...
        score1 = score1 + die

        # player's turn to roll the dice...
        die = random.randint(1,6)
        # add to player2's score...

    # Checking for the winner...
    if score1 > score2:
        print("\nPlayer 1 ", player1, " is the winner of this game with points: ", score1)
        save_to_file(player1, score1)
    else:
        print("\nPlayer 2 ", player2, " is the winner of this game with points: ", score2)
        save_to_file(player2, score2)

def insert_players(con):
    cur = con.cursor()
    cur = con.execute("insert into Students(name) values('Alex')")
    cur = con.execute("insert into Students(name) values('Maxwell')")

def authorized_players(con):
    cur = con.cursor()
    for i in cur.execute("SELECT * FROM Students"):
        print(i[0])

def valid_player(name):
    cur = con.cursor()
    for i in cur.execute("SELECT * FROM Students"):
        if i[0] == name:
            return True
    
    return False

if __name__ == "__main__":
    # Connecting to database...
    con = sqlite3.connect('database.sqbpro')
    insert_players(con)

    # Taking user's choice...
    option = menu_choice()

    # while choice is not 4 which is exit continue...
    while option != 4:
        # Displaying rules of the game...
        if option == 1:
            displayRules()
        # stating the game to play...
        elif option == 2:
            playGame()
        # Diplaying top 5 players...
        else:
            diplay_top_5()
        # Asking for the menu again...
        option = menu_choice()

    print('Goodbye!')

