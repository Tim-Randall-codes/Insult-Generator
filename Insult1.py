from tkinter import *
import random
root = Tk()

def engine():
    output.delete(1.0, END)
    ran1 = random.randint(1, 6)
    if ran1 == 1:
        output.insert(END, "You are ")
    elif ran1 == 2:
        output.insert(END, "Your mother is ")
    elif ran1 == 3:
        output.insert(END, "Your dad is ")
    elif ran1 == 4:
        output.insert(END, "Your sister is ")
    elif ran1 == 5:
        output.insert(END, "Your dog is ")
    elif ran1 == 6:
        output.insert(END, "Your brother is ")
    ran2 = random.randint(1, 9)
    if ran2 == 1:
        output.insert(END, "an otter ")
    elif ran2 == 2:
        output.insert(END, "an accountant ")
    elif ran2 == 3:
        output.insert(END, "a ketamine user ")
    elif ran2 == 4:
        output.insert(END, "a Walmart customer ")
    elif ran2 == 5:
        output.insert(END, "a UFC fan ")
    elif ran2 == 6:
        output.insert(END, "a raver ")
    elif ran2 == 7:
        output.insert(END, "an antimasker ")
    elif ran2 == 8:
        output.insert(END, "a teen mum ")
    elif ran2 == 9:
        output.insert(END, "a tiktok user ")
    ran3 = random.randint(1, 9)
    if ran3 == 1:
        output.insert(END, "who lives in Florida.")
    elif ran3 == 2:
        output.insert(END, "who has face tattoos.")
    elif ran3 == 3:
        output.insert(END, "with body odor.")
    elif ran3 == 4:
        output.insert(END, "with a greasy blonde mullet.")
    elif ran3 == 5:
        output.insert(END, "who wears a maga hat.")
    elif ran3 == 6:
        output.insert(END, "with a septum ring.")
    elif ran3 == 7:
        output.insert(END, "who is a disappointment.")
    elif ran3 == 8:
        output.insert(END, "who listens to Smash Mouth.")
    elif ran3 == 9:
        output.insert(END, "who binges on the Bachelorette.")
    
        

root.title("Insult Generator!")

welcome = Label(root, text="Press the button for an insult")
welcome.grid(row=0, column=0, sticky=W)

welcome2 = Label(root, text="If you are not insulted yet, press again!")
welcome2.grid(row=1, column=0, sticky=W)

output = Text(root, width=50, height=10, wrap=WORD)
output.grid(row=3, column=0, sticky=W)

b = Button(root, text="Click for insult", command=engine)
b.grid(row=2, column=0, sticky=W)

qb = Button(root, text="Quit", command=root.quit)
qb.grid(row=2, column=1, sticky=W)

root.mainloop()
