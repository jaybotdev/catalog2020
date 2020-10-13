import os
while True:
    answer = input('''
    Welcome to Catalog 2020 1.0, a Graeson Brickner project!
    Select 1 option by typing the number and pressing enter
    1. Create new catalog entry.
    2. Delete data in a file and re-write.
    3. Append data to the end of a file.
    4. Read an entry
    5. Delete an entry
    6. Exit the program ''')
    if answer == "1":
        title = input("What would you like to name the file? ")
        file = open(title + ".txt", "x")
        print("The file has been created.")
        file.close
    elif answer == "2":
        title = input("What file would you like edit? Note, this will delete all data in the file. ")
        text = input("What would you like to write? ")
        file = open(title + ".txt", "w")
        print(file)
        with open(title + ".txt", "w") as f:
            f.write(text)
    elif answer == "3":
        title = input("What file would you like to append data to? ")
        text = input("What would you like to write? ")
        file = open(title + ".txt", "a")
        print(file)
        with open(title + ".txt", "a") as f:
            f.write("\n" + text)
    elif answer == "4":
        bruhe = input("What is the name of the file you would like to read?")
        file = open(bruhe + ".txt", "rb")
        prina = file.read()
        file.close()
        print(prina)
    elif answer == "5":
        title = input("What file would you like to delete? ")
        os.remove(title + ".txt")
        print("The file has been deleted.")
        file.close
    elif answer == "6":
        break