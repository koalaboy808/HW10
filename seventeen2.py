from random import randint

def P1_turn(marbles, sub_value, f_out):
	if marbles <= int(sub_value):
		sub_value = marbles
		marbles -= marbles
	else:
		marbles = marbles - int(sub_value)

	f_out.write(str(sub_value) + "-")
	return marbles

def P2_turn(marbles, f_out):	
	if marbles <= 3:
		marbles_taken = 1
	else:
		marbles_taken = randint(1,3)
	marbles -= marbles_taken
	f_out.write(str(marbles_taken) + "-")
	return marbles
		
def read_file():
	with open("seventeen_input.txt") as f_in:
		# read in input and split into list of strings by line
		f_in_list = []
		f_in = f_in.read().split("\n")
		# loop through list of strings and split into lists within lists by ","
		[f_in_list.append(line.split(",")) for line in f_in]
		return f_in_list

def new_file():
	f_in_list = read_file()

	with open("seventeen_output.txt", "w") as f_out:
		f_out.write("Game on!")
		computer_win = 0
		human_win = 0

		for index, value in enumerate(f_in_list):
			marbles = 17
			f_out.write("\nGame# " + str(index+1) + ". Play Sequence: ",)

			# loop through second list to pull out values within each list
			for sub_index, sub_value in enumerate(value):
				#Player 1 first
				marbles = P1_turn(marbles,sub_value, f_out)
				if marbles == 0:
					f_out.write(". Winner: P2")
					human_win += 1
					break
				#Player 2 second
				marbles = P2_turn(marbles, f_out)
				if marbles == 0:
					f_out.write(". Winner: P1")
					computer_win += 1
					break
		f_out.write("\nPlayer 1 won " + str(computer_win) + "times; Player 2 won " + str(human_win) + " times.")


#############################################################################
##################### call functions below through main(): ###################
##############################################################################
def main():
	new_file()

if __name__ == '__main__':
    main()
