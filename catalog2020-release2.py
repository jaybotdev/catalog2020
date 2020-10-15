import tkinter as tk
import os
class Root(tk.Tk):
    james = tk.Tk
    frame = tk.Frame()
    def __init__(self):
        super().__init__() 
        frame = tk.Frame(self)
        frame.pack()


        button = tk.Button(frame,
                    text = "Make New File",
                    command=self.answer1)
        button.pack(side=tk.LEFT)

        button2 = tk.Button(frame, 
                    text = "Edit File", 
                    command = self.answer2)
        button2.pack(side=tk.LEFT)

        button3 = tk.Button(frame, 
                    text = "Append Data", 
                    command = self.answer3)
        button3.pack(side=tk.LEFT)

        button4 = tk.Button(frame, 
                    text = "Read File", 
                    command = self.answer4)
        button4.pack(side=tk.LEFT)

        button5 = tk.Button(frame, 
                    text = "Delete File", 
                    command = self.answer5)
        button5.pack(side=tk.LEFT)

        buttonquit = tk.Button(frame, 
                text="QUIT", 
                fg="red",
                command=quit)
        buttonquit.pack(side=tk.LEFT)


        self.L1 = tk.Label(self, text="File Name")
        self.L1.pack(side = tk.LEFT)

        self.E1 = tk.Entry(self, bd =5)
        self.E1.pack(side = tk.LEFT)


        self.L2 = tk.Label(self, text="Text to Edit")
        self.L2.pack( side = tk.RIGHT)

        self.E2 = tk.Entry(self, bd =5)
        self.E2.pack(side = tk.RIGHT)

        self.title("Catalog 2020")

    def answer1(self):
        title = self.E1.get()
        text = self.E1.get()
        file = open(title + ".txt", "x")
        print("The file has been created.")
        file.close

    def answer2(self):
        title = self.E1.get()
        text = self.E2.get()
        file = open(title + ".txt", "w")
        with open(title + ".txt", "w") as f:
            f.write(text)

    def answer3(self):
        title = self.E1.get()
        text = self.E2.get()
        file = open(title + ".txt", "a")
        with open(title + ".txt", "a") as f:
            f.write("\n" + text)

    def answer4(self):
        title = self.E1.get()
        text = self.E2.get()
        file = open(title + ".txt", "rb")
        prina = file.read()
        file.close()
        priina = prina.decode()
        print(priina)

    def answer5(self):
        title = self.E1.get()
        text = self.E2.get()
        os.remove(title + ".txt")
        print("The file has been deleted.")
if __name__ == '__main__':
    john = tk.Tk()
    run = Root()
    john.mainloop()