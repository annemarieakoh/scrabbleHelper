from pathlib import Path
import os

'''
take in:
- list of usuable letters (scrabble rack)
    - use dashes to represent blank tiles
- word to be completed (target)
    - put dashes in place of unknown letters
- word list (dictionary) of all possible words on a single line each

e.g. scrabbleHelper(['r', 'g', 'p', 'e', 't', 'a', 'z'], "--p---ed", "words.txt")

'''


scrabbleScores = [['a',1],['b',3],['c',3],['d',2],['e',1],['f',4],['g',2],['h',4],
                  ['i',1],['j',8],['k',5],['l',1],['m',3],['n',1],['o',1],['p',3],
                  ['q',10],['r',1],['s',1],['t',1],['u',1],['v',4],['w',4],['x',8],
                  ['y',4],['z',10]]


def scrabbleHelper(rack, target, dictionary):
    "rack is a list of characters, target is a string"
    
    "make one large string of rack and known letters"
    usable = rack
    for char in target:
        if  char != '-':
            usable += char

    "sort it"
    usable.sort()


    "open dictionary specified by user"
    path = Path(dictionary)
    if not path.is_file():
        print("File","'",dictionary,"'","not found.")
        return
    if os.path.getsize(dictionary) == 0:
        print("File '",dictionary,"' empty.")
        return
    with open(dictionary, "r") as dic:
        words = dic.readlines()
        words = [word.strip() for word in words]
    dic.close()

    
    "sort english words of same length and check if subset or equal to"
    words = [word for word in words if len(word) == len(target)]
    solutions = []
    invalid = []
    for word in words:
        copy = []
        for ch in word:
            copy += [ch]
        copy.sort()
        if subset(copy, usable):
            '''list of indicies of known letters in target'''
            known = [i for i in range(len(target)) if target[i] != '-']
            for index in known:
                if word[index] != target[index]:
                    invalid += [word]
            solutions += [word]

    solutions = [word for word in solutions if word not in invalid]
    "append word score to each solution then sort solutions based on score value"
    solutions = [wordWithScore(word, scrabbleScores, usable) for word in solutions]

    solutions = sortSolutions(solutions)
    printSolutions(solutions)
    return

def printSolutions(sols):
    if len(sols) == 0:
        print("No valid solutions based on the given word list.")
    else:
        print("Valid Solutions:")
        for sol in sols:
            print(sol)
    return

def scrabbleHelperBlankTile(rack, target, dictionary):
    '''mimics scrabbleHelper to do all the possibilities with the blank tile being each of the 26 letters'''

    path = Path(dictionary)
    if not path.is_file():
        print("File","'",dictionary,"'","not found.")
        return
    if os.path.getsize(dictionary) == 0:
        print("File '",dictionary,"' empty.")
        return
    with open(dictionary, "r") as dic:
        words = dic.readlines()
        words = [word.strip() for word in words]
    dic.close()

    rack.sort()

    allSolutions = []
    
    for i in range(ord('a'), ord('z')+1): #all 26 possibilities of letters
        newRack = [chr(i)] + rack[1:]
        usable = newRack
        for char in target:
            if  char != '-':
                usable += char
        usable.sort()

        words = [word for word in words if len(word) == len(target)]
        solutions = []
        invalid = []
        for word in words:
            copy = []
            for ch in word:
                copy += [ch]
            copy.sort
            if subset(copy, usable):
                known = [i for i in range(len(target)) if target[i] != '-']
                for index in known:
                    if word[index] != target[index]:
                        invalid += [word]
                solutions += [word]
                
        solutions = [wordWithScore(word, scrabbleScores, usable) for word in solutions if word not in invalid]
        allSolutions += solutions

    allSolutions = sortSolutions(allSolutions)
    printSolutions(allSolutions)
    return
    

def subset(copy, usable):
    '''manually checks if copy list is a subset or equal to usable list'''
    for ch in copy:
        if ch in usable:
            usable = removeIndex(ch, usable)
        else:
            return False
    return True


def removeIndex(ch, usable):
    '''removes first occurrence of ch in list usable'''
    for i in range(len(usable)):
         if usable[i] == ch:
            if i == 0:
                usable = usable[1:]
                return usable
            elif i == (len(usable)-1):
                usable = usable[:-1]
                return usable
            else:
                usable = usable[:i] + usable[i+1:]
                return usable

def wordWithScore(word, scrabbleScores, usable):
    '''appends the scrabble score to the word'''
    score = 0
    for ch in word:
        if ch not in usable: #meaning we must be on a blank tile
            score += 1 #so the tile value is automatically just 1
        #NEED TO ACCOUNT FOR THE CASE WHERE THE BLANK TILE IS USED AS ANOTHER OF THE AVAILABLE TILES
        else:
            score += letterScore(ch, scrabbleScores)
    return word + " - " + str(score)

def letterScore(ch, scrabbleScores):
    '''return score value of letter ch'''
    for score in scrabbleScores:
        if score[0] == ch:
            return score[1]
        

def sortSolutions(sols):
    '''sorts the list of words in solutions based on their word score - highest score first'''
    unique = list(set(sols))
    if len(unique) in [0, 1]:
        return unique
    for i in range(1, len(unique)):
        curr = unique[i]
        word, score_str = curr.rsplit(' - ', 1)  # split by the last occurrence of " - "
        key = int(score_str)  # convert the score part to an integer
        j = i - 1
        while j >= 0:
            prev_word, prev_score_str = unique[j].rsplit(' - ', 1)
            prev_score = int(prev_score_str)
            if key > prev_score:
                unique[j + 1] = unique[j]
                j -= 1
            else:
                break
        unique[j + 1] = curr
    return unique


while(True):
    board = input("Enter your Scrabble rack separated by a single space: ")
    target = input("Enter your target word: ")
    rack = board.split()
    if '-' in rack:
        scrabbleHelperBlankTile(rack, target, "words.txt")
    else:
        scrabbleHelper(rack, target, "words.txt")
    print("\n")

