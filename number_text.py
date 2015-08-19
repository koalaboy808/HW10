def number_text(text):	

	with open(text) as f_in:
		f1_2 = open("new_small.txt", "w")
		count = 1
		for line in f_in:
			f1_2.write(str(count) + " " + line )
			count += 1

number_text("small.txt")