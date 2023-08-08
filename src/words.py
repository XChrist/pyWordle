import enum
import random

class WordComparison (enum.Enum):
    invalid = 1 
    valid = 2
    exists = 3

class WordList:
    words: list[str]
    
    def __init__(self) -> None:
        pass
    
    def importFromFile(self, file_name: str) -> None:
        file = open(file_name, "r")
        file_data = file.read().split('\n')
        for line in file_data:
            if len(line) != 5:
                raise BaseException(f"Invalid line length in {file_name}:\"{line}\"")
        self.words = file_data
        file.close()
    
    def has(self, word: str) -> bool:
        return word in self.words
    
    def remove(self, word: str) -> None:
        self.words.remove(word)
    
    def random(self) -> str:
        return random.choice(self.words)
    
    def count(self) -> int:
        return len(self.words)
    
def compare(input_word: str, model_word: str) -> list[WordComparison]:
    results = list()
    used_chars = dict()
    for index, input_char in enumerate(input_word):
        model_char = model_word[index]
        char_count = used_chars.get(input_char)
        if input_char in model_word:
            if char_count and char_count >= model_word.count(input_char):
                results.append(WordComparison.invalid)
            elif not char_count or (char_count and char_count < model_word.count(input_char)):
                if input_char == model_char:
                    results.append(WordComparison.valid)
                else:
                    results.append(WordComparison.exists)
        elif input_char not in model_word:
            results.append(WordComparison.invalid)
        if input_char in model_word:
            if input_char not in used_chars.keys(): used_chars[input_char] = 0
            used_chars[input_char] += 1
    return results