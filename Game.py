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
		ran_q = random.randrange(1, 20)
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
		if count == 6:
			f = ran_q
		if count == 7:
			g = ran_q
		if count == 8:
			h = ran_q
		if count == 9:
			i = ran_q
		if count == 10:
			j = ran_q
		if count == 11:
			k = ran_q
		if count == 12:
			l = ran_q
		if count == 13:
			m = ran_q
		if count == 14:
			n = ran_q
		if count == 15:
			o = ran_q
		if (ran_q != a and ran_q != b and ran_q != c and ran_q != d and ran_q != e and ran_q != f and ran_q != g and ran_q != h and ran_q != i and ran_q != j and ran_q != k and ran_q != l and ran_q != m and ran_q != n and ran_q != o):
			question_num = 1
			repeat = False
			print(question_num)
			if question_num == 1:
				answer = "David Cameron"
				guess = input("Who is a wanker? ")
				progress += 1
				if guess == answer:
					correct += 1
					print("Correct well done %s" % name)
				else:
					print("wrong fuckface")
main()
