"""
Эта программа создаёт файл, в который записывает данные. 
Она может искать пользователя в файле по любым из данных и редактировать любые данные.
После каждого создания пользователя или обновления информации о нём она автоматически "освежает" файл.
Варианты с одинаковыми пользователями сознательно игнорировал, поскольку Александр сказал, что это не часть задачи.

Algorithm:
1. Creating new users
2. Searching users by any data in json file
    a. Edit
        ...name/number/location
    b. Delete
    (auto updating)
3. All data
"""


import json

def print_menu():
    print()
    print('1. Create new user')
    print('2. Find user by info')
    print('3. Show data')
    print('4. Quit')
    print()

def difference (list1, list2):
    list_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
    return list_dif


filename = "myfile.json"
myfile = open(filename)

try:
    book = json.load(myfile)
except json.decoder.JSONDecodeError:
        book = []

user = {
    'first_name': '',
    'last_name': '',
    'phone': '',
    'city': ''
}

print_menu()

try:
    while True:
            command = input("Enter the command: ")
            if command == "1":
                first_name = input("Enter first name: ").capitalize()
                last_name = input("Enter last name: ").capitalize()
                phone = input("Enter phone number: ")
                city = input('Enter city: ').capitalize()
                user['first_name'] = first_name
                user['last_name'] = last_name
                user['phone'] = phone
                user['city'] = city
                book.append(user.copy())
                try:
                    with open(filename, 'w') as myfile:
                        file_content = (json.load(myfile)).copy()
                        new_to_update = (difference(file_content, book)).copy()
                        file_content.extend(new_to_update)
                        json.dump(file_content, myfile, indent=4)
                        print("Updated!")
                        print_menu()
                except Exception:
                    with open (filename, 'w') as myfile:
                        json.dump(book, myfile, indent=4)
                        print("Recorded!")
                print("New person has been created!")
                print_menu()
            elif command == "2":
                info = input("Please, write here any information about the user (first name/ last name/ number/ city): ").capitalize()
                try:
                    with open(filename, 'r') as myfile:
                        file_content = (json.load(myfile)).copy()
                        for i in file_content:
                            if i['first_name'] == info:
                                print(f"\n{i['first_name']}", f" {i['last_name']}: {i['city']}, {i['phone']}")
                                current_user = i
                            if i['last_name'] == info:
                                print(f"\n{i['first_name']}", f" {i['last_name']}: {i['city']}, {i['phone']}")
                                current_user = i
                            if i['phone'] == info:
                                print(f"\n{i['first_name']}", f" {i['last_name']}: {i['city']}, {i['phone']}")
                                current_user = i
                            if i['city'] == info:
                                print(f"\n{i['first_name']}", f" {i['last_name']}: {i['city']}, {i['phone']}")
                                current_user = i
                        index_of_user = file_content.index(current_user)
                    choice = input("\n1. Edit\n2. Delete\n3. Back\n")
                    if choice == '1':
                        with open(filename, 'r') as myfile:
                            file_content = (json.load(myfile)).copy()
                            edit = input('\n1. Edit name\n2. Edit phone number\n3. Edit city\n')
                            if edit == '1':
                                edit = input('\n1. Edit first name\n2. Edit last name\n')
                                if edit == '1':
                                    new_name = input("Enter new first name: ").capitalize().strip()
                                    (file_content[index_of_user])['first_name'] = new_name
                                elif edit == '2':
                                    new_name = input("Enter new last name: ").capitalize().strip()
                                    (file_content[index_of_user])['last_name'] = new_name
                            elif edit == '2':
                                new_number = input("Please, write here new number: ").strip()
                                (file_content[index_of_user])['phone'] = new_number
                            elif edit == '3':
                                new_city = input("Enter new city: ").capitalize().strip()
                                (file_content[index_of_user])['city'] = new_city
                        with open(filename, 'w') as myfile:
                            json.dump(file_content, myfile, indent=4)  

                    elif choice == '2':
                        index_of_user = file_content.index(current_user)
                        del file_content[index_of_user]
                        print(f"\n{i['first_name']}", f" {i['last_name']} deleted!")
                        with open(filename, 'w') as myfile:
                            json.dump(file_content, myfile, indent=4)
                except NameError:
                    print("I can't find.")
                print_menu()


            elif command == "3":
                try:
                    with open(filename, 'r') as myfile:
                        file_content = (json.load(myfile)).copy()
                        if file_content == []:
                            print('=( empty')
                        else:
                            print("Users:\n")
                            for x in file_content:
                                print(f"{x['first_name']}", f" {x['last_name']}: {x['city']}, {x['phone']}")
                        print_menu()
                except json.decoder.JSONDecodeError:
                    print("Book is empty at the moment!")
                    print_menu()

            elif command == "4": 
                print('See you!')
                break
            else: 
                print('See you!')
                break
except Exception as e:
    print('Unexpected error.')
finally:
    print('Bye!')
