class Book:
    
    ### Private Methods ###
    
    def __init__(self, path):
        self.__path = path
        self.__content = self.get_content()
        self.__words = self.__content.split()
        self.__characters = self.__get_characters()
        self.__letters = self.__get_letters()
        self.__letter_breakdown = self.__get_letter_breakdown()

    def __get_characters(self):
        characters = []
        for word in self.__words:
            uppercase_word = word.upper()
            characters += list(uppercase_word)
        return characters
    
    def __get_letters(self):
        letters = []
        for character in self.__characters:
            if character.isalpha():
                letters.append(character)
        return letters


    def __get_letter_breakdown(self):
        letter_breakdown = {}
        for letter in self.__letters:
            if letter in letter_breakdown:
                letter_breakdown[letter] += 1
            else:
                letter_breakdown[letter] = 1
        return letter_breakdown

    ### Public Methods ###

    def get_content(self):
        with open(self.__path) as book:
            return book.read()
    
    def generate_report(self):
        print(f"\n--- Word & Character Report for Book Located at '{self.__path}' ---\n")
        print("Word Count:")
        print(f"There are about {len(self.__words)} total words in the provided text.\n")
        print("Character Count:")
        print(f"There are {len(self.__characters)} total characters in the provided text while {len(self.__letters)} of them are in the alphabet. The following is a breakdown of these characters and their associated counts.\n")
        breakdown = self.__letter_breakdown.items()
        for letter, instances in sorted(breakdown):
            print(f"- {letter} was used {instances} times.")
        print()

book = Book("books/frankenstein.txt")
book.generate_report()
