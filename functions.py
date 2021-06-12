"""A collection of function for doing my project."""

###A FUNCTION THAT WELCOMES THE PLAYER TO THE GAME 
def Welcome_To_The_Game():
    """A printed statement that welcomes the player"""

    print('Welcome to Mallory\'s great guessing game. Type yes if you would like to play!')
    player_choice = input()
    
    if player_choice == 'yes':
        instructions()
    else:
        Welcome_To_The_Game()
    
###A FUNCTION THAT STATES INSTRUCTIONS
def instructions():
    """A printed statement of the instructions and an empty text box that advances to level one"""
    
    print('I am a number... if you guess my number correctly, you may move onto the next level, if you guess incorrectly, you will have to restart that level. There are 5 levels total. Good Luck!')
    start_the_game = input('Type Anything Here To Start Level 1:')
    
    level_1()
    
###LEVEL 1 FUNCTION 
def level_1():
    """correct_answer: answer to the question.
    Prompt: the prompt given to the player"""
 
    correct_answer = '14'
    prompt = 'Level 1... I am an even 2-digit number that is less than 8 + 8 but more than 6 + 6. What number am I?'
    
    print(prompt)
   
    """player_answer: empty text box for player to enter their guess.
    If player enters the correct answer, an empty text box opens to advance to the next level.
    If the guess is incorrect, an empty text box opens to retry the level."""
    
    player_answer = input('Type Your Answer Here:')
    
    if player_answer == correct_answer:
        print('WoW! You guessed what number I am! Let\'s try another...')
        move_on = input('Type Anything Here To Advance:')
        
        level_2()
        
    else:
        print('Bummer, you did not guess what number I am...')
        try_again = input('Type Anything Here To Try Again:')
        
        level_1()
        
###LEVEL 2 FUNCTION 
def level_2():
    
    correct_answer = '10'
    prompt = 'Level 2... To find out what number I am, start with 4 then add the number that comes after 9 and finally subtract the number you started with.'
    
    print(prompt)
    
    player_answer = input('Type Your Answer Here:')
    
    if player_answer == correct_answer:
        print('Okay... you\'re pretty good at this. Let\'s try another!')
        move_on = input('Type Anything Here To Advance:')
        
        level_3()
        
    else:
        print('Oops... not quite! Try Again!')
        try_again = input('Type Anything Here To Try Again:')
        
        level_2()
        
###LEVEL 3 FUNCTION 
def level_3():
    
    correct_answer = '54'
    prompt = 'Level 3... I am greater than the number of states in the US, but less than the number of seconds in a minute, and my ones digit is one more than the number of sides on a triangle.'
    
    print(prompt)
    
    player_answer = input('Type Your Answer Here:')
    
    if player_answer == correct_answer:
        print('Amazing! You have guessed correctly once again!')
        move_on = input('Type Anything Here To Advance:')
        
        level_4()
        
    else:
        print('Sorry, not the right answer...')
        try_again = input('Type Anything Here To Try Again:')
        
        level_3()
        
###LEVEL 4 FUNCTION 
def level_4():
    
    correct_answer = '6'
    prompt = 'Level 4... I am the squareroot of a number that is one greater than the amount of tenticles an octopus has multiplied by the number of fingers I would have on my right hand if one was bitten off by a shark.'
    
    print(prompt)
    
    player_answer = input('Type Your Answer Here:')
    
    if player_answer == correct_answer:
        print('Sheesh! You are good at this! Do you think you can beat the final level?')
        move_on = input('Type Anything Here To Advance:')
        
        level_5()
        
    else:
        print('Nope! I will give you a hint.. I am not 12. Try Again!')
        try_again = input('Type Anything Here To Try Again:')
        
        level_4()
        
###LEVEL 5 FUNCTION
def level_5():
    
    correct_answer = '75'
    prompt = 'Level 5... Alright, are you ready? I am a 2 digit number between 60 and 80, if you add 2 to my ones digit, you will get my tens digit, but I am not a multiple of 2.'
    
    print(prompt)
    
    player_answer = input('Type Your Answer Here:')
    
    if player_answer == correct_answer:
        print('Wonderful! You have passed all the levels! You really are so smart! :)')
        play_again = input('Type Anything Here To Start The Game Over:')
        
        Welcome_To_The_Game()
        
    else:
        print('Noooo but you are so close to finishing! Hint... 5 + 2 = 7.')
        try_again = input('Type Anything Here To Try Again:')
        
        level_5()
