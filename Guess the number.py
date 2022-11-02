import random

print('*_WELCOME TO GUESS THE NUMBER_*')
print()
diff=str(input('Choose difficulty: Easy Normal Insane'))

if diff=='Easy':
    number=random.randint(10,20) #this generates a random number b/w 10 and 20
    ctr = 0
    while ctr < 5: #specifies amount of guesses a player has!
        guess=int(input('Guess a number in the range 10...20:'))
        if guess == number:
            print('YOU WIN!!')

            break     #this makes the loop terminate either when the number has been guessed or when the player fails to do so.

        else:
            ctr += 1
        if not ctr < 5:
            print('You lose, \n the number was',number)

elif diff=='Normal':
    number=random.randint(10,50) #this generates a random number b/w 10 and 50
    ctr = 0
    while ctr < 10: #specifies amount of guesses a player has!
        guess=int(input('Guess a number in the range 10...50:'))
        if guess == number:
            print('YOU WIN!!')
        

            break     #this makes the loop terminate either when the number has been guessed or when the player fails to do so.

        else:
            ctr += 1
        if not ctr < 10:
            print('You lose, \n the number was',number)
            print('Good Game!')

elif diff=='Insane':
    number=random.randint(10,50) #this generates a random number b/w 10 and 100
    ctr = 0
    while ctr < 5: #specifies amount of guesses a player has!
        guess=int(input('Guess a number in the range 10...50:'))
        if guess == number:
            print('YOU WIN!!')

            break     #this makes the loop terminate either when the number has been guessed or when the player fails to do so.
        else:
            ctr += 1
        if not ctr < 3:
            print('You lose, \n the number was',number)

else:
    print('Invalid Option!!')
 
