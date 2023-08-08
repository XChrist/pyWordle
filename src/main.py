from rich.console import Console
import words

word_list_guess = words.WordList()
word_list_valid = words.WordList()
word_list_guess.importFromFile("word_lists/guess.txt")
word_list_valid.importFromFile("word_lists/valid.txt")

console = Console()
console.clear()
console.set_window_title("pyWordle")

console.print("\nWelcome to [bold]pyWordle[/] written by XChrist on [link=https://www.github.com/XChrist]Github[/].")
console.print("Valid words were sourced from Kinkelin's [link=https://github.com/Kinkelin/WordleCompetition]Wordle AI Repo[/].")
console.print("The official game can be found [link=https://www.nytimes.com/games/wordle]here[/].\n")
console.print("[bold]Tutorial[/]")
console.print("Each round, a random five letter word will be chosen.")
console.print("You must guess this word using clues given each turn.")
console.print("You are allowed only six turns to guess the word.\n")
console.print("If a letter is highlighted:")
console.print("[on green]GREEN[/]\tThat letter is correctly placed.")
console.print("[on yellow]YELLOW[/]\tThat letter is in the word but placed incorrectly.\n")
console.print("You can quit anytime by entering \"quit\" or \"exit\"\n")

round_number = 0
round_word: str
round_active: bool
game_active = True
turn_number: int
total_wins = 0
total_losses = 0
input_active: bool

while game_active:
    
    if word_list_guess.count() < 1:
        console.print(f"\nYou've guessed every word! Go outside! Interact with others! Take a shower!\n")
        break
    
    round_number += 1
    round_word = word_list_guess.random()
    round_active = True
    turn_number = 0
    show_word = False
    
    console.print(f"~~~ ROUND {round_number} ~~~\n")
    
    while round_active:
        
        turn_number += 1
        if turn_number == 6:
            round_active = False
            show_word = True
            total_losses += 1
        
        input_active = True
        
        while input_active:
            user_input = input("> ").strip().lower()
            if user_input in ("exit", "quit", "end"):
                game_active = False
                break
            if len(user_input) != 5:
                console.print("\nGuess must be a 5 letter word.\n")
            elif not word_list_valid.has(user_input):
                console.print("\nThis word is not valid.\n")
            else:
                input_active = False
        
        if not game_active:
            break
        
        comparison = words.compare(user_input, round_word)
        
        console.print()
        
        for index, letter in enumerate(user_input):
            formatting = "none"
            char_comparison = comparison[index]
            if char_comparison == words.WordComparison.valid:
                formatting = "on green"
            elif char_comparison == words.WordComparison.exists:
                formatting = "on yellow"

            console.print(f"[{formatting}]{letter}[/]", end=" ")

        console.print("\n")
        
        if user_input == round_word:
            console.print(f"You guessed the word, [bold]{round_word}[/], in {str(turn_number)} turn(s)!")
            round_active = False
            total_wins += 1
    
    if show_word:
        console.print(f"\nThe word was: [bold]{round_word}[/]!\n")
        word_list_guess.remove(round_word)

console.print(f"\nGame finished with {total_wins} wins and {total_losses} losses.\n")