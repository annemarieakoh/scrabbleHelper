# scrabbleHelper
A simple program to provide the user with a printed list of all possible words that can be played based on a certain target word in Scrabble.<br />
scrabbleHelper asks the user to enter their scrabble rack as a series of space-separated lowercase letters. The user is then asked to enter the target word they're trying to make. This is formatted as a number of dashes "-" to represent unknown letters, and actual known letters.<br />
For example, the user's Scrabble rack is:<br />
    p g a o n c n
And it is known that there is a playable word on the Scrabble board:
    --t--
From the above, this is a 5-letter word with known tile "t" in the middle, and 4 other unknown tiles.
scrabbleHelper will output:
    Valid Solutions:
    acton - 7
    cotan - 7
    octan - 7
    anton - 5
    notan - 5
as all the possible words that can be made (and their Scrabble scores) that satisfy the conditions of the target word. Note that possible words are selected from words.txt which is a textfile of all English words. Depending on the Scrabble game, different dictionaries may be used.

As for blank tiles within the Scrabble rack, the user will represent them with a dash, "-".
For example,
    Enter your Scrabble rack separated by a single space: - a k e d r s

In traditional Scrabble games, the value of a blank tile is always 1, regardless of the letter it's used as. scrabbleHelper currently treats the blank tile score as the score of the letter it is used as. Repeated solutions have also been displayed in the blank-tile cases - this has yet to be fixed.
 
