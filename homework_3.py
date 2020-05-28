print("TASK 1")
word = input("Hi! Enter here a word: ").strip()
print(word[0:2] + word[-2:])

word = input("Hi! Enter here a word: ").strip()
if len(word) <= 2:
    print(word * 2)
    
empty = input("Enter here less than 2 characters: ").strip()
if len(empty) <2:
    print("Empty String")

    
    
print("\nTASK 2")
while True:
    number = input("Please, enter your number: ").strip()
    if number.isdigit() and len(number) == 10:
        print("Congratulations! Your number has been received.")
        break
    elif number.isalpha():
        print("Please, use numeral characters. Try again.")
    elif number.isdigit() == False:
        print("Please, enter ONLY numeral characters. Try again.")
    elif int(number) != 10:
        print("You have entered less or more than 10 numeral characters. Try again.")

        

print("\nTASK 3")
name = "anton"
users_name = input("Hi! Enter here Anton's name in upper- or downcase: ").strip()
if(users_name.lower()) == name:
    print("True! It's really his name.")
    print(users_name.lower())

    
    
print("\nTASK 2")
while True:
    number = input("Please, enter your number: ")
    if number.isdigit() and len(number) == 10:
        print("Congratulations! Your number has been received.")
        break
    elif number.isalpha():
        print("Please, use numeral characters. Try again.")
    elif number.isdigit() == False:
        print("Please, enter ONLY numeral characters. Try again.")
    elif int(number) != 10:
        print("You have entered less or more than 10 numeral characters. Try again.")

        

print("\nTASK 3")
name = "anton"
users_name = input("Hi! Enter here Anton's name in upper- or downcase: ")
if users_name.lower() == name:
    print("True! It's really his name.")
    print(users_name.lower())
