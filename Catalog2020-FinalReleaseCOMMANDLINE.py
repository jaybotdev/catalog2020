import os
import random
import time
while True:
    answer = input('''
    
      /$$$$$$            /$$             /$$                   /$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$ 
     /$$__  $$          | $$            | $$                  /$$__  $$/$$$_  $$/$$__  $$/$$$_  $$
    | $$  \__/ /$$$$$$ /$$$$$$   /$$$$$$| $$ /$$$$$$  /$$$$$$|__/  \ $| $$$$\ $|__/  \ $| $$$$\ $$
    | $$      |____  $|_  $$_/  |____  $| $$/$$__  $$/$$__  $$ /$$$$$$| $$ $$ $$ /$$$$$$| $$ $$ $$
    | $$       /$$$$$$$ | $$     /$$$$$$| $| $$  \ $| $$  \ $$/$$____/| $$\ $$$$/$$____/| $$\ $$$$
    | $$    $$/$$__  $$ | $$ /$$/$$__  $| $| $$  | $| $$  | $| $$     | $$ \ $$| $$     | $$ \ $$$
    |  $$$$$$|  $$$$$$$ |  $$$$|  $$$$$$| $|  $$$$$$|  $$$$$$| $$$$$$$|  $$$$$$| $$$$$$$|  $$$$$$/
     \______/ \_______/  \___/  \_______|__/\______/ \____  $|________/\______/|________/\______/ 
                                                     /$$  \ $$                                    
                                                    |  $$$$$$/                                    
                                                     \______/                                     

    Welcome to Catalog 2020 1.0, a Graeson Brickner project!
    Select 1 option by typing the number and pressing enter
    1. Create new catalog entry.
    2. Delete data in a file and re-write.
    3. Append data to the end of a file.
    4. Read an entry
    5. Delete an entry
    6. Jokes!
    7. Exit the program ''')
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
        joke = random.randint(1, 5)
        if joke == "1":
            print("A bear walks into a bar and says, “Give me a whiskey… and a cola.”")
            time.sleep(2)
            print("“Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure. I was born with them.”")
        if joke == "2":
            print("Did you hear about the claustrophobic astronaut?")
            time.sleep(2)
            print("He just needed a little space.")
        if joke == "3":
            print("What does a nosy pepper do?")
            time.sleep(2)
            print("Gets jalapeño business!")
        if joke == "4":
            print("What do you call a parade of rabbits hopping backwards?")
            time.sleep(2)
            print("A receding hare-line.")
        if joke == "5":
            print("What did the left eye say to the right eye?")
            time.sleep(2)
            print("Between you and me, something smells.")
    elif answer == "7":
        break
