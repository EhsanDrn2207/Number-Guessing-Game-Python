import random

print("Welcome to number guessing game.")

def assign_top_number():
    while True:
        try:
            top_number = input("Enter a top number for range number: ")
            print("-" * 20)
            if top_number.isalpha():
                print("Please enter a positive number.")
                print("-" * 20)

            elif int(top_number) <= 0:
                print("Please enter a positive number.")
                print("-" * 20)
            else:
                return int(top_number)
        
        except ValueError:
            print("Please enter a positive number.")
            print("-" * 20)


def random_number(top_number:int):
    answer = random.randint(0, top_number)
    counter = 0
    while True:
        try:
            user_input = int(input("Guess the number: "))
            if user_input == answer:
                print("You got it.")
                break
                
            elif user_input > answer:
                print("the number is less than you guess.")
                print("-" * 20)
                counter += 1
            
            else:
                print("the number is more than your guess.")
                print("-" * 20)
                counter += 1
                
        except ValueError:
            print("Please enter number.")
            print("-" * 20)
    
    return counter, answer
            
with open("file1.txt", "+a") as file:
    top_number = assign_top_number()
    guesses, number = random_number(top_number=top_number)
    print("You got it in", guesses, "guesses.")
    file.write(f"\nanwser: {number}, guesses: {guesses}\n")
    file.write("-" * 20)
