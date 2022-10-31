from tkinter import *


# Function to choose colour
def choose_colour(button_pressed):
    global colour
    colour = button_pressed
    print("Colour choice is {}".format(colour))
# Functions to print "Button Pressed" Results
def red_pressed(r, c):
    global colour
    if colour == 0:
        button[r][c].config(bg='white')
    elif colour == 1:
        button[r][c].config(bg='#DCDCDC')
    elif colour == 2:
        button[r][c].config(bg='#BEBEBE')
    elif colour == 3:
        button[r][c].config(bg='#989898')
    elif colour == 4:
        button[r][c].config(bg='#696969')
    elif colour == 5:
        button[r][c].config(bg='#404040')
    elif colour == 6:
        button[r][c].config(bg='#101010')
    else:
        button[r][c].config(bg='black') 
    print("Button Pressed is RED!")

def seq():
    for r in range(o):
        for c in range(o):
            button[r][c].config(bg='white')

def seq2():
    for r in range(o):
        for c in range(o):
            button[r][c].config(bg='black')

def seq3():
    for r in range(o):
        for c in range(o):
            if r == c:
                button[r][c].config(bg='black')
            elif r + c == o-1:
                button[r][c].config(bg='black')
            elif r != 0 and r != o-1:
                if o%2 == 0:
                    if c != o/2 and c != (o/2)-1:
                        button[r][c].config(bg='#989898')
                    else:
                        button[r][c].config(bg='white')
                else:
                    if c != (o-1)/2:
                        button[r][c].config(bg='#989898')
                    else:
                        button[r][c].config(bg='white')    
            else:
                button[r][c].config(bg='white')
            #00 01 02 03 04
            #10 11 12 13 14
            #20 21 22 23 24
            #30 31 32 33 34
            #40 41 42 43 44

def seq4():
    colours = ['white','#DCDCDC','#BEBEBE','#989898','#696969','#404040','#101010','black']
    global colour
    for r in range(o):
        for c in range(o): 
            button[r][c].config(bg=colours[c])


# Main GUI Windows
main = Tk()
main.title("Tutorial 2 Sample")

#frame = Frame(main)
#frame.grid()

frame1 = Frame(main)
frame1.grid(row=0, column=0)

frame2 = Frame(main)
frame2.grid(row=0, column=1)

frame3 = Frame(main)
frame3.grid(row=1 , column=0, columnspan=2)

# Colour Section (Using Button Widget)
colour = 0
o = 3 #o represent the number of row & column

#grid0 = Button(main, bg=('white') , command=red_pressed , height=2, width=2)
#grid0.grid(column=0, row=0)

#grid0 = Button(main, bg=('white') , command=red_pressed , height=2, width=2)
#grid0.grid(column=0, row=0)

#button = [[r for r in range(3)] c for c in range(3)]
button = [[r for r in range(o)] for c in range(o)]
for r in range(o):
    for c in range(o):
        button[r][c] = Button(frame1, bg="white", text="   ", font=('Arial',21), command=lambda m=r, l=c:red_pressed(m, l))
        button[r][c].grid(row=r, column=c)
        

colourRed = Button(frame3, text="All white", bg=('white'), font=(200), command=seq)
colourGreen = Button(frame3, text="All Black", fg=('white'), bg=('black'), font=(200), command=seq2)
colourBlue = Button(frame3, text="X Pattern", bg=('gold'), font=(200), command=seq3)
colourGold = Button(frame3, text="Sequence", bg=('pink'), font=(200), command=seq4)
colourOrange = Button(frame3, text="Send Image!", bg=('white'), font=(200))
colourRed.grid(row=0, column=0)
colourGreen.grid(row=0, column=1)
colourBlue.grid(row=0, column=2)
colourGold.grid(row=0, column=3)
colourOrange.grid(row=1, columnspan=2, column=1)

colourgrey = Button(frame2, text="White", bg=('white'), font=(200), command=lambda m=0:choose_colour(m))
colourgrey1 = Button(frame2, text="Grey1", bg=('#DCDCDC'), font=(200), command=lambda m=1:choose_colour(m))
colourgrey2 = Button(frame2, text="Grey2", bg=('#BEBEBE'), font=(200), command=lambda m=2:choose_colour(m))
colourgrey3 = Button(frame2, text="Grey3", bg=('#989898'), font=(200), command=lambda m=3:choose_colour(m))
colourgrey4 = Button(frame2, text="Grey4", fg=('white'), bg=('#696969'), font=(200), command=lambda m=4:choose_colour(m))
colourgrey5 = Button(frame2, text="Grey5", fg=('white'), bg=('#404040'), font=(200), command=lambda m=5:choose_colour(m))
colourgrey6 = Button(frame2, text="Grey6", fg=('white'), bg=('#101010'), font=(200), command=lambda m=6:choose_colour(m))
colourblack = Button(frame2, text="Black", fg=('white'), bg=('black'), font=(200), command=lambda m=7:choose_colour(m))
colourgrey.grid(row=0, column=1)
colourgrey1.grid(row=1, column=1)
colourgrey2.grid(row=2, column=1)
colourgrey3.grid(row=3, column=1)
colourgrey4.grid(row=4, column=1)
colourgrey5.grid(row=5, column=1)
colourgrey6.grid(row=6, column=1)
colourblack.grid(row=7, column=1)

main.mainloop()