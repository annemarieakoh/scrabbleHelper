# scrabbleHelper
A simple program to provide the user with a printed list of all possible words that can be played based on a certain target word in Scrabble.<br />
scrabbleHelper asks the user to enter their scrabble rack as a series of space-separated lowercase letters. The user is then asked to enter the target word they're trying to make. This is formatted as a number of dashes "-" to represent unknown letters, and actual known letters.<br />
For example, the user's Scrabble rack is:<br />
    p g a o n c n<br />
And it is known that there is a playable word on the Scrabble board:<br />
    --t--<br />
From the above, this is a 5-letter word with known tile "t" in the middle, and 4 other unknown tiles.<br />
scrabbleHelper will output:<br />
    Valid Solutions:<br />
    acton - 7<br />
    cotan - 7<br />
    octan - 7<br />
    anton - 5<br />
    notan - 5<br />
as all the possible words that can be made (and their Scrabble scores) that satisfy the conditions of the target word. Note that possible words are selected from words.txt which is a textfile of all English words. Depending on the Scrabble game, different dictionaries may be used.<br />

As for blank tiles within the Scrabble rack, the user will represent them with a dash, "-".<br />
For example,<br />
    Enter your Scrabble rack separated by a single space: - a k e d r s<br />
<br />
In traditional Scrabble games, the value of a blank tile is always 1, regardless of the letter it's used as. scrabbleHelper recognizes this and treats the blank tile score as 1. However, what has yet to be accounted for are the instances of a blank tile used as a letter that already exists in the user's Scrabble rack. All Valid Solutions will still be computed, but the scores won't necessarily be accurate.<br />
For example, the user's Scrabble rack is:<br />
    - d e c a h<br />
And the target word is:<br />
    -ached<br />
The output will be:<br />
Valid Solutions:<br />
cached - 14<br />
bached - 14<br />
But the score for "cached" should be 12 because the extra "c" (from the blank tile" should have a value of 1, not of 3 (original score of a "c" tile).
