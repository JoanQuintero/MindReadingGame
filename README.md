# MindReadingGame

Specification for Mind Reading Game
1.      The program will play a game between two players  
a.	The game is called Mind Reading  
b.	The game will have an input range from 1 to 10  
c.	Player 2 will be the Mind Readee  
        i. His job is to input a number for the Mind Reader to attempt at guessing.    
d.	Player 1 will be the Mind Reader  
i.	His job is to attempt to guess the Mind Readee’s inputs.  
2.	The users (or players) will get to pick the position they wish to play the game.  
a.	The program will ask the user for an input  
i.	The input will have two choices (#1 for Mind Reader, #2 for Mind Readee)  
1.	Once players have chosen; information will show the:  
i.	 instructions about each position is displayed.  
ii.	rules about the game  
3.	The game will address a question specifically towards each player   
i.	The first question will be asked to the Mind Readee  
1.	Example: “What is your desired input?”  
2.	And the player must enter a number from 1 to 10.  
3.	If the input is an integer out of range, the program will appear stating “The number is not within the given options” and the program will ask the mind readee for an input again. After 5 consistent mistakes, the game will end and portray the player’s intentions as not wanting to play the game.  
4.	Once player 2 chooses a number within the range, it becomes player 1 turn. However, to prevent the input from being seen, the program will print about 15 – 20 spaces to avoid a leak.  
ii.	The second question will be asked to the Mind Reader  
1.	He will get only one chance to input a number from 1 to 10  
2.	5 chances will be given to the Mind Reader if input guess is less than 1 and more than 10 …. Something like: if 10 < guess < 1: etc  

4.	BEHIND THE SCENES  

i.	The game will have a function that will count the amount of input from the Mind Readee   
ii.	The game will also count the amount of input from the Mind Reader  
iii.	A formula will determine how many times the Mind Reader got the correct guess and from that the program will determine to what percent the Mind Reader is able to read the Mind Readee’s mind.  
