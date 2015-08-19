from random import randint

# P1 input based off of the given text file... append number of marbles taken to temporary list used to access each game sequence
def P1_turn(marbles, sub_value, temp_sequence):
	if marbles <= int(sub_value):
		sub_value = marbles
		marbles -= marbles
	else:
		marbles = marbles - int(sub_value)
	temp_sequence.append(sub_value)
	return marbles

# P2 input based off of random integer... append number of marbles taken to a temporary list used to access each game sequence
def P2_turn(marbles, temp_sequence):	
	if marbles <= 3:
		marbles_taken = 1
	else:
		marbles_taken = randint(1,3)
	marbles -= marbles_taken
	temp_sequence.append(marbles_taken)
	return marbles
	
# read in input from text file and get into a list of list format
def read_file():
	with open("seventeen_input.txt") as f_in:
		f_in_list = []
		f_in = f_in.read().split("\n")
		[f_in_list.append(line.split(",")) for line in f_in]
		return f_in_list

def play_game():
	f_in_list = read_file()

	# create empty variables for use in future
	final_dict = {}
	winner = []
	P1_win = 0
	P2_win = 0

	# loop through top list in order to access inner lists
	for index, value in enumerate(f_in_list):

		# reset marbles to 17 and temp_sequence to empty list
		marbles = 17
		temp_sequence = []

		# loop through inner list in order to pull out values within each list
		for sub_index, sub_value in enumerate(value):

			# Call for Player 1 input-- if marbles = 0, then break and account for winner and number of wins
			marbles = P1_turn(marbles,sub_value, temp_sequence)
			if marbles == 0:
				winner.append("P2")
				P2_win += 1
				break
			# Call for Player 2 input-- if marbles = 0, then break and account for winner and number of wins
			marbles = P2_turn(marbles, temp_sequence)
			if marbles == 0:
				winner.append("P1")
				P1_win += 1
				break

		# after loop through inner list has finished, add the game sequence to final_dict at the appropriate key
		final_dict[index] = temp_sequence

	# once both for loops have finished, return a tuple-- 1) P1 win count 2) P2 win count 3) list of each game winner 4) dictionary of each game sequence
	return P1_win, P2_win, winner, final_dict


#############################################################################
##################### call functions below through main(): ###################
##############################################################################
def main():
	# access tuple (of four items) returned by play_game to use to write final outcome
	factors = play_game()
	P1_win = factors[0]
	P2_win = factors[1]
	winner = factors[2]
	final_dict = factors[3]

	with open("seventeen_output.txt", "w") as f_out:
		# write each game sequence using for loop, then write the total number of times P1 and P2 won
		for key, value in final_dict.items():
			f_out.write(("Game #" + str(key+1) + ". Play Sequence: " + ("-".join(str(s) for s in value)) + ". " + winner[key] +  " wins.\n"))
		f_out.write("\nPlayer 1 won " + str(P1_win) + " times; Player 2 won " + str(P2_win) + " times.")

if __name__ == '__main__':
    main()
