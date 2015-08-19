from random import randint

def get_randomdigit_Liquido(length):
	# call digits_allowed function
	number_digits = length
	# find max range by executing 10 to the number of digis minus 1
	random_integer = randint(0, (10**number_digits)-1)

	# insert 0's using a list format (my bull_cow function works off of a list of three strings)
	magic_number = random_integer
	magic_list = [i for i in str(magic_number)]
	magic_input = length - len(magic_list)
	[magic_list.insert(0, '0') for i in range(magic_input)]
	return magic_list

print(get_randomdigit_Liquido(3))