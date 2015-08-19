# Instructions
'''

seventeen1

'''

# import

import sys
from random import randint

# body

def seventeen1():
	# set variables for later use... 'marbles' is marbles left in jar; 'turn' is flag for person's turn; 'winner' flag for who wins
	marbles = 17
	turn = 1
	winner = None

	# continue as long as marbles is greater than 0
	while marbles >= 0:
		print "Number of marbles left in jar: " + str(marbles) + "\n"
		# ifelse for whether computer or humans turn... if no marbles left then print winner and end game
		if marbles == 0:
			print "There are no marbles left"
			print winner
			break
		# Computer
		elif (turn % 2)==0:
			turn += 1
			winner = "You win!"
			marbles = computer_turn(marbles)
		# Human
		elif (turn % 2)==1:		
			marbles = human_turn(marbles)
			winner = "Computer wins!"
			turn += 1
			

# function for user input
def human_turn(marbles):	
	while True:
		marbles_taken = raw_input("Your turn: How many marbles will you remove (1-3)?")
		# use try/except to make sure the number is a digit
		try:
			int(marbles_taken)
		except:
			print("Sorry, that is not a valid option. Try again!")
			print "Number of marbles left in jar: " + str(marbles) + "\n"
		# checks to see if user input in valid... if so, set new marbles value to marbles minus user input
		else:
			marbles_taken = int(marbles_taken)
			if (marbles_taken >= 1) and (marbles_taken <= 3) and (marbles_taken <= marbles):
				marbles = marbles - marbles_taken
				print "You removed " + str(marbles_taken) + " marbles."
				return marbles
			else:
				print("Sorry, that is not a valid option. Try again!")
				print "Number of marbles left in jar: " + str(marbles) + "\n"

# function for computer's turn... runs on randint unless value is less than or equal to 3
def computer_turn(marbles):
	# ifelse depending on number of marbles left
	if marbles <= 3:
		marbles_taken = 1
	else:
		marbles_taken = randint(1,3)

	marbles -= marbles_taken
	print "Computer's turn..."
	print "Computer removed " + str(marbles_taken) + " marbles."
	return marbles

##############################################################################
##################### call functions below through main(): ###################
##############################################################################
def main():
	print("\nLet's play the game of Seventeen!")
	seventeen1()

if __name__ == '__main__':
    main()