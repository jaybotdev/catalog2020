import tkinter as tk
import os
import random
import time
def answer1():
        title = input("What would you like to name the file? ")
        file = open(title + ".txt", "x")
        print("The file has been created.")

def answer2():
    title = input("What file would you like edit? Note, this will delete all data in the file. ")
    text = input("What would you like to write? ")
    file = open(title + ".txt", "w")
    print(file)
    with open(title + ".txt", "w") as f:
        f.write(text)

def answer3():
    title = input("What file would you like to append data to? ")
    text = input("What would you like to write? ")
    file = open(title + ".txt", "a")
    print(file)
    with open(title + ".txt", "a") as f:
        f.write("\n" + text)

def answer4():
    bruhe = input("What is the name of the file you would like to read?")
    file = open(bruhe + ".txt", "rb")
    prina = file.read()
    file.close()
    print(prina)

def answer5():
    title = input("What file would you like to delete? ")
    os.remove(title + ".txt")
    print("The file has been deleted.")

#def answer6():
#    joke = random.randint(1, 5)
#    if joke == "1":
#        print("A bear walks into a bar and says, “Give me a whiskey… and a cola.”")
#        time.sleep(2)
#        print("“Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure. I was born with them.”")
#    if joke == "2":
#        print("Did you hear about the claustrophobic astronaut?")
#        time.sleep(2)
#        print("He just needed a little space.")
#    if joke == "3":
#        print("What does a nosy pepper do?")
#        time.sleep(2)
#        print("Gets jalapeño business!")
#    if joke == "4":
#        print("What do you call a parade of rabbits hopping backwards?")
#        time.sleep(2)
#        print("A receding hare-line.")
#    if joke == "5":
#        print("What did the left eye say to the right eye?")
#        time.sleep(2)
#        print("Between you and me, something smells.")
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.title("Catalog 2020")

button = tk.Button(frame,
                    text = "Make New File",
                    command=answer1)
button.pack(side=tk.LEFT)

button2 = tk.Button(frame, 
                    text = "Edit File", 
                    command = answer2)
button2.pack(side=tk.LEFT)
button3 = tk.Button(frame, 
                    text = "Append Data", 
                    command = answer3)
button3.pack(side=tk.LEFT)
button4 = tk.Button(frame, 
                    text = "Read File", 
                    command = answer4)
button4.pack(side=tk.LEFT)
button5 = tk.Button(frame, 
                    text = "Delete File", 
                    command = answer5)
button5.pack(side=tk.LEFT)
#button6 = tk.Button(frame, 
 #                   text = "Tell me a Joke", 
  #                  command = answer6)
#button6.pack(side=tk.LEFT)
buttonquit = tk.Button(frame, 
                text="QUIT", 
                fg="red",
                command=quit)
buttonquit.pack(side=tk.LEFT)
root.mainloop()