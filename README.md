# MindReadingGame by Joan S. Quintero

## Specification for Mind Reading Game

**1.      The program will play a game between two players**

<ul>
        <li>The game is called Mind Reading</li>
        <li>The game will have an input range from 1 to 10</li>
        <li>Player 2 will be the Mind Readee</li>
        <ul>
                <li>Player 2's task is to input a number for the Mind Reader to attempt at guessing</li>
        </ul>
        <li>Player 1 will be the Mind Reader</li>
        <ul>
                <li>Player 1's task is to attempt to guess the Mind Readee’s inputs.</li>
        </ul>
</ul>

**2.	The users (or players) will get to pick the position they wish to play the game.** 

<ul>
        <li>The program will ask the user for an input</li>
        <ul>
                <li>The input will have two choices (#1 for Mind Reader, #2 for Mind Readee)</li> 
                <ul>
                        <li>Once players have chosen; information will show the:</li> 
                        <ul>
                                <li>instructions about each position is displayed.</li>  
                                <li>rules about the game</li>  
                        </ul>
                </ul>
        </ul>
</ul>

**3.	The game will address a question specifically towards each player**   
<ul>
        <li>The first question will be asked to the Mind Readee</li>
        <ul>
                <li>Example: “What is your desired input?”</li>  
                <li>And the player must enter a number from 1 to 10.</li>  
                <li>If the input is an integer out of range, the program will appear stating “The number is not within the given options” and the program will ask the mind readee for an input again. After 5 consistent mistakes, the game will end and portray the player’s intentions as not wanting to play the game.</li>  
                <li>Once player 2 chooses a number within the range, it becomes player 1 turn. However, to prevent the input from being seen, the program will print about 15 – 20 spaces to avoid a leak.</li>  
        </ul>
        <li>The second question will be asked to the Mind Reader</li>  
        <ul>
                <li>He will get only one chance to input a number from 1 to 10</li>  
                <li>5 chances will be given to the Mind Reader if input guess is less than 1 and more than 10 …. Something like: if 10 < guess < 1: etc</li>
        </ul>
</ul>

**4.	BEHIND THE SCENES**  

<ul>
        <li>The game will have a function that will count the amount of input from the Mind Readee</li>   
        <li>The game will also count the amount of input from the Mind Reader</li>  
        <li>A formula will determine how many times the Mind Reader got the correct guess and from that the program will determine to what percent the Mind Reader is able to read the Mind Readee’s mind.</li>
<ul>
