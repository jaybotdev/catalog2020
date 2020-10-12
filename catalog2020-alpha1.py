import os
while True:
    answer = input('''
    Welcome to Catalog 2020 1.0, a Graeson Brickner project!
    Select 1 option by typing the number and pressing enter
    1. Create new catalog entry.
    2. Append data to the end of the file.
    3. Read an entry
    4. Delete an entry
    5. Exit the program ''')
    if answer == "1":
        title = input("What would you like to name the file? ")
        file = open(title + ".txt", "x")
        print("The file has been created.")
        file.close
    elif answer == "2":
        title = input("What file would you like to append data to? ")
        text = input("What would you like to append? ")
        file = open(title + ".txt", "a+")
        file.write("\n" + text)
        print("The file has been edited.")
        file.close
    elif answer == "3":
        bruhe = input("What is the name of the file you would like to read?")
        file = open(bruhe + ".txt", "rb")
        prina = file.read()
        file.close()
        print(prina)
    elif answer == "4":
        title = input("What file would you like to delete? ")
        os.remove(title + ".txt")
        print("The file has been deleted.")
        file.close
    elif answer == "5":
        break