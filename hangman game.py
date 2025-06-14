import random
class Graphics(object):
    def __init__(self):
        super().__init__()
        
    def display(self, stage):
        stages = [self.default, self.mistakeOne, self.mistakeTwo, self.mistakeThree, self.mistakeFour, self.mistakeFive, self.mistakeSix, self.over]
        stages[min(stage, 6)]()
        
    def default(self):
        default = ("""
    ____
    |/   |
    |   
    |    
    |    
    |    
    |
    |_____ \n""")
        print(default)
        
    def mistakeOne(self):
        mistakeOne = ("""
    ____
    |/   |
    |   (_)
    |    
    |    
    |    
    |
    |_____ \n""")
        print(mistakeOne)

    def mistakeTwo(self):
        mistakeTwo = ("""
    ____
    |/   |
    |   (_)
    |    |
    |    |
    |    
    |
    |_____ \n""")
        print(mistakeTwo)
        
    def mistakeThree(self):
        mistakeThree = ("""
    ____
    |/   |
    |   (_)
    |   \|
    |    |
    |    
    |
    |_____ \n""")
        print(mistakeThree)
        
    def mistakeFour(self):
        mistakeFour = ("""
    ____
    |/   |
    |   (_)
    |   \|/ 
    |    |
    |    
    |
    |_____ \n""")
        print(mistakeFour)
        
    def mistakeFive(self):
        mistakeFive = ("""
    ____
    |/   |
    |   (_)
    |   \|/ 
    |    |
    |   /  
    |
    |_____ \n""")
        print(mistakeFive)
        
    def mistakeSix(self):
        mistakeSix = ("""
    ____
    |/   |
    |   (_)
    |   \|/ 
    |    |
    |   / \ 
    |
    |_____ \n""")
        print(mistakeSix)
        
    def over(self):
        over = ("""
    ____
    |/   |
    |   (_)
    |   /|\  
    |    |
    |   / \ 
    |
    |_____ \n""")
        print(over)
        
class GameStats(object):
    def __init__(self):
        super().__init__()
        self.totalTries = 0
        self.wrongTries = 0
        
    def getTries(self, correct):
        self.totalTries += 1
        if not correct:
            self.wrongTries += 1
        
dictionary = {
            "easy": ["programming", "beautiful", "computer", "science"],
            "medium": ["category", "altitude", "banger", "project"],
            "difficult": ["rhythm", "zephyr", "poutpourri", "serendipitous"]} 

def getMode():
    keepGoing = True
    while keepGoing:
        mode = input("""Which mode would you like to play?
        Easy
        Medium
        Difficult\n""").strip().lower()
        if mode in dictionary:
            return mode
        else:
            print("Please enter a valid mode from the list (Easy, Medium, or Difficult)")
    
def chooseWord(mode):
    return random.choice(dictionary[mode])

def printWord(word, guessedLetters):
    return ' '.join([letter if letter in guessedLetters else '_' for letter in word])

def hangman():
    g = Graphics()
    s = GameStats()
    mode = getMode()
    word = chooseWord(mode)
    guessedLetters = set()
    maxWrong = 6
    
    print("Hangman\n")
    g.display(0)
    
    while s.wrongTries < maxWrong:
        print("\n Your word to guess:", printWord(word, guessedLetters))
        guess = input("Enter a letter: ").lower()
        
        if not guess.isalpha():
            print("Please enter a single alphabet letter.")
        elif len(guess) != 1:
            print("Please enter a single alphabet letter.")
        if guess in guessedLetters:
            print("You have already guessed that letter.")
        
        guessedLetters.add(guess)
        
        if guess in word:
            s.getTries(correct=True)
        else:
            s.getTries(correct=False)
            g.display(s.wrongTries)
            
        if all(letter in guessedLetters for letter in word):
            print(f"\nCongrats, you got it. The word was {word}")
            return
        
    print(f"\nYou lost. The word was {word}")
    g.over()
    
def main():
    hangman()
    
    
if __name__ == "__main__":
    main()

