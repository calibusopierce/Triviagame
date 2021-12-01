print('Hi there, Welcome to General Trivia Game! ')

answer = input('Are you ready to play? (yes/no): ')
score = 0
questions = 15

if answer.lower() == 'yes':
	print("\n\tLet's start!")

	answer = input ('\n1. What is the title of last Avenger Movie? \n\t(a)Age of Ultron \n\t(b)End Game \n\t(c)Infinity War \n\t(d)Civil War \n')
	if answer.lower() == 'b':
		score += 1
		print('\nCorrect +1')
	else:
		print('Incorrect')

	answer = input ('\n2. Which of the Following is an Odd Number? \n\t(a)365 \n\t(b)550 \n\t(c)32 \n\t(d)44 \n')
	if answer.lower() == 'a':
		score += 1
		print('\nCorrect +1')
	else:
		print('Incorrect')

	answer = input ('\n3. What is the name of the artist that painted Mona Lisa? \n\t(a)Vincent Van Gogh \n\t(b)Leonardo da Vinci \n\t(c)Pablo Picasso \n\t(d)Michelangelo \n')
	if answer.lower() == 'b':
		score += 1
		print('\nCorrect +1')
	else:
		print('Incorrect')

	answer = input ('\n4. In what country is Absolut vodka made? \n\t(a)Russia \n\t(b)Italy \n\t(c)Sweden \n\t(d)Poland \n')
	if answer.lower() == 'c':
		score += 1
		print('\nCorrect +1')
	else:
		print('Incorrect')

	answer = input ('\n5. In Roman numerals, what number does "D" represent? \n\t(a)50 \n\t(b)100 \n\t(c)200 \n\t(d)500 \n')
	if answer.lower() == 'd':
		score += 1
		print('\nCorrect +1')
	else:
		print('Incorrect')

	answer = input ('\n6. What color is cerulean? \n\t(a)Blue \n\t(b)Red \n\t(c)Green \n\t(d)Yellow \n')
	if answer.lower() == 'a':
		score += 1
		print('\nCorrect +1')
	else:
		print('Incorrect')

	answer = input ('\n7. What is the better-known word for "aubergine"? \n\t(a)Cucumber \n\t(b)Zucchini \n\t(c)Potato \n\t(d)Eggplant \n')
	if answer.lower() == 'd':
		score += 1
		print('\nCorrect +1')
	else:
		print('Incorrect')

	answer = input ('\n8. How many colored squares are there on a Rubiks Cube? \n\t(a)44 \n\t(b)53 \n\t(c)43 \n\t(d)54 \n')
	if answer.lower() == 'd':
		score += 1
		print('\nCorrect +1')
	else:
		print('Incorrect')

	answer = input ('\n9. In what movies is the Okinawan sword-maker Hattori Hanzo a character? \n\t(a)Samurai X \n\t(b)Rurouni Kenshin \n\t(c)Killbill \n\t(d)Ronin \n')
	if answer.lower() == 'c':
		score += 1
		print('\nCorrect +1')
	else:
		print('Incorrect')

	answer = input ('\n10. Which popular candy bar is named after the makers favorite horse? \n\t(a)Mars \n\t(b)Snickers \n\t(c)Twix \n\t(d)Hersheys \n')
	if answer.lower() == 'b':
		score += 1
		print('\nCorrect +1')
	else:
		print('Incorrect')

	answer = input ("\n11. Aside from red sun radiation, Which of the following is Superman's Weakness? \n\t(a)Kryptonite \n\t(b)Vibranium \n\t(c)Adamantite \n\t(d)Redstone \n")
	if answer.lower() == 'a':
		score += 1
		print('\nCorrect +1')
	else:
		print('Incorrect')

	answer = input ("\n12. Who is Donald Duck's Girlfriend? \n\t(a)Donna \n\t(b)Diana \n\t(c)Daisy \n\t(d)Dahlia \n")
	if answer.lower() == 'c':
		score += 1
		print('\nCorrect +1')
	else:
		print('Incorrect')	

	answer = input ("\n13. Which country is called Pearl of the Orient Sea? \n\t(a)Indonesia \n\t(b)Japan \n\t(c)Thailand \n\t(d)Philippines \n")
	if answer.lower() == 'd':
		score += 1
		print('\nCorrect +1')
	else:
		print('Incorrect')

	answer = input ("\n14. What is the capital of Canada? \n\t(a)Ottawa \n\t(b)Toronto \n\t(c)Montreal \n\t(d)Vancouver \n")
	if answer.lower() == 'a':
		score += 1
		print('\nCorrect +1')
	else:
		print('Incorrect')

	answer = input ("\n15. Which actor played the role of Edward Scissorhands? \n\t(a)John Mayer \n\t(b)Johnny Depp \n\t(c)Daniel Radcliffe \n\t(d)Leonardo DiCaprio \n")
	if answer.lower() == 'b':
		score += 1
		print('\nCorrect +1')	
	else:
		print('Incorrect')
	
	print(f'\n\t Thank you for answering you got {score} questions correctly' )
	if score == 15:
		print(f'You are truly a God tier!')
	elif score >= 14:
		print(f'You are Amazing!')
	elif score >= 11:
		print(f'You passed, Keep it up! ')
	elif score <= 10:
		print(f'You failed, try again next time! ')
else:
	print('\n\tThank you for your timely response!')
