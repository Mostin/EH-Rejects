def main():
	print("This game was developed by EH-Rejects, hope you enjoy")
	print("")
	name = input("What is your name? ")
	print("")
	print("""Hello %s""" % name)
	print("You will be asked questions and have to use the EH-Rejects Cryptography suite to work out the answers.")
	count = 0
	a, b, c, d, e, f, g, h, i, j, k, l, m, n, o = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	correct = 0
	progress = 1
	import random
	replay = True
	repeat = True
	while repeat == True:
		ran_q = random.randrange(1, 5)
		count += 1
		if count == 1:
			a = ran_q
		if count == 2:
			b = ran_q
		if count == 3:
			c = ran_q
		if count == 4:
			d = ran_q
		if count == 5:
			e = ran_q
		if (ran_q != a and ran_q != b and ran_q != c and ran_q != d and ran_q != e):
			question_num = ran_q
			repeat = True
			print(question_num)
			if question_num == 1:
				answer = "David Cameron"
				guess = input("Using our tool, decrypt this cipher 'Hhmmm Gcfwvve' ")
				progress += 1
				if guess == answer:
					correct += 1
					print("Correct well done %s" % name)
				else:
					print("Unlucky try again.")
			if question_num == 2:
				answer = "Gvmiwxtr"
				guess = input("Using our tool, encrypt the word 'Coventry' and enter your output as the answer.")
				progress += 1
				if guess == answer:
					correct += 1
					print("Correct well done %s" % name)
				else:
					print("Unlucky try again")
			if question_num == 3:
				answer = "gyptcsikstop wdmvx"
				guess = input("Encrypt the title of our online blog http://ehrejects.wordpress.com and enter your output as the answer.")
				progress += 1
				if guess == answer:
					correct += 1
					print("Correct well done %s" % name)
				else:
					print("Unlucky try again")
			if question_num == 4:
				answer = "One-time pad"
				guess = input("Which type of encryption is virtually impossible to break if used correctly?")
				progress += 1
				if guess == answer:
					correct += 1
					print("Correct well done %s" % name)
				else:
					print("Unlucky try again")
			if question_num == 5:
				answer = "Bacon and egg Sandwich"
				guess = input("What did Jack have for breakfast?")
				progress += 1
				if guess == answer:
					correct += 1
					print("Correct well done %s" % name)
				else:
					print("Unlucky try again")
main()
