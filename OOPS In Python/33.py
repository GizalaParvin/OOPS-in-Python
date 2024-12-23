# # class Animal:
# #     def speak(self):
# #         print("This is the generic sound an animal")
        
# # class Dog(Animal):
# #     def speak(self):
# #         print("Woof")
# # class Cat(Animal):
# #     def speak(self):
# #         print("MEow")
# # dog = Dog()
# # dog.speak()
# # cat = Cat()
# # cat.speak()

# #Data Overloading 
# class Person:
#     def __init__(self,name,age = None):
#         self.name = name 
#         self.age = age
#     @classmethod
#     def from_birth_year(cls,name,birth_year):
#         current_year = 2024
#         age = current_year - birth_year
#         return cls(name,age)
# person1 = Person("Alice")
# person2 = Person("Bob",30)
# person3 = Person.from_birth_year("Charlie",1990)

# print("person 1:",person1.name,person1.age)
# print("person 2:",person2.name,person2 .age)
# print("person 3:",person3.name,person3 .age)

# #Exception Raise try,except,finally 
# # try:
# #     x = 10/0
# # except ZeroDivisionError:
# #     print()
# # finally:
    
# #     print("Finally Block  excuted.")

# # print()
import random

class GuessWordGame:
    def __init__(self, words):
        self.words = words
        self.secret_word = random.choice(words)
        self.guesses = []
        self.max_attempts = 7
    
    def display_word(self):
        display = ''
        for letter in self.secret_word:
            if letter in self.guesses:
                display += letter
            else:
                display += '_'
        return display
    
    def make_guess(self, letter):
        self.guesses.append(letter)
        if letter not in self.secret_word:
            self.max_attempts -= 1
    
    def is_game_over(self):
        if self.max_attempts <= 0:
            return True
        if '_' not in self.display_word():
            return True
        return False

# Example usage:
words = ["apple", "banana", "cherry", "orange", "grape"]
game = GuessWordGame(words)

print("Welcome to Guess the Word Game!")
print("Guess the word:", game.display_word())

while not game.is_game_over():
    guess = input("Enter a letter: ").lower()
    game.make_guess(guess)
    print("Current progress:", game.display_word())
    
if '_' not in game.display_word():
    print("Congratulations! You guessed the word correctly:", game.secret_word)
else:
    print("Sorry, you're out of attempts. The word was:", game.secret_word)



















