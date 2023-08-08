# PyWordle

PyWordle is a command-line focused port of the popular online word puzzle game, Wordle. This program uses the Rich library to format and color text.

Each round, the player must guess a five letter word chosen at random. For each attempted guess, the user is given clues based on where the letter may sit in the word. These clues will either suggest that a letter is correctly placed in the word, incorrectly placed but in the word, or simply not in the word. When guessing, the number of clues given for a specific letter depends on how many times that letter appears. If the player does not guess the word in, at most, six turns, the round is over.  
 
## Credit

New York Time's ["Wordle"](https://www.nytimes.com/games/wordle)

Kinkelin's ["WordleCompetition"](https://github.com/Kinkelin/WordleCompetition)