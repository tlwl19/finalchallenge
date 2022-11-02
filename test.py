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
    #print("Button Pressed is RED!")

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
            if r == c or r+c == o-1:
                button[r][c].config(bg='black')
            #elif r + c == o-1:
                #button[r][c].config(bg='black')
            # elif r != 0 and r != o-1:
            #     if o%2 == 0:
            #         if c != o/2 and c != (o/2)-1:
            #             button[r][c].config(bg='#989898')
            #         else:
            #             button[r][c].config(bg='white')
            #     else:
            #         if c != (o-1)/2:
            #             button[r][c].config(bg='#989898')
            #         else:
            #             button[r][c].config(bg='white')
    # for r in range(0, o-1, 1):
    #     for c in range(0, int(r/2)+1, +1):
    #         button[r][c].config(bg='#696969')
            else:
                button[r][c].config(bg='white')
            #00 01 02 03 04
            #10 11 12 13 14
            #20 21 22 23 24
            #30 31 32 33 34
            #40 41 42 43 44

def seq4():
    global w, colours, colour
    colours = ['white','#DCDCDC','#BEBEBE','#989898','#696969','#404040','#101010','black']
    if len(w) > 4:
        w = [0]
    if len(w) == 2:
        p = -1
        w.append(0)
        for r in range(o):
            #if p > (len(colours)-1):
                #p = 0
            for c in range(o):
                p = p+1
                if p > len(colours)-1:
                    p = 0
                button[r][c].config(bg=colours[p])
                #print (p)
    elif len(w) == 3:
        p = len(colours)
        w.append(0)
        for r in range(o):
            #if p > (len(colours)-1):
                #p = 0
            for c in range(o):
                p = p-2
                if p < 1:
                    p = len(colours)-2
                button[r][c].config(bg=colours[p])
                #print (p)
    elif len(w) == 1:
        p = len(colours)
        w.append(0)
        for r in range(o):
            #if p > (len(colours)-1):
                #p = 0
            for c in range(o):
                p = p-1
                if p < 1:
                    p = len(colours)-1
                button[r][c].config(bg=colours[p])
                #print (p)     
    else:
        p = len(colours)
        w.append(0)
        for r in range(o):
            #if p > (len(colours)-1):
                #p = 0
            for c in range(o):
                p = p-2
                if p < 1:
                    p = len(colours)-1
                button[r][c].config(bg=colours[p])
                #print (p)  

# def seq4():
#     colours = ['white','#DCDCDC','#BEBEBE','#989898','#696969','#404040','#101010','black']
#         global colour
#         for r in range(o):
#             for c in range(o):
#                 if c > (len(colours)-1):
#                     c = 0
#                 button[r][c].config(bg=colours[c])

# def seq5():
#     colours = ['white','#DCDCDC','#BEBEBE','#989898','#696969','#404040','#101010','black']
#     p = -1
#     global colour
#     for r in range(o):
#         #if p > (len(colours)-1):
#             #p = 0
#         for c in range(o):
#             p = p+1
#             if p > len(colours)-1:
#                 p = 0
#             button[r][c].config(bg=colours[p])
#             print (p)

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
o = 32 #o represent the number of row & column

#grid0 = Button(main, bg=('white') , command=red_pressed , height=2, width=2)
#grid0.grid(column=0, row=0)

#grid0 = Button(main, bg=('white') , command=red_pressed , height=2, width=2)
#grid0.grid(column=0, row=0)

#button = [[r for r in range(3)] c for c in range(3)]
button = [[r for r in range(o)] for c in range(o)]
for r in range(o):
    for c in range(o):
        #button[r][c] = Button(frame1, bg="white", text="   ", font=('Arial',21), command=lambda m=r, l=c:red_pressed(m, l))
        button[r][c] = Button(frame1, bg="white", text="  ", font=('Arial',5), command=lambda m=r, l=c:red_pressed(m, l))
        button[r][c].grid(row=r, column=c)
        

colourRed = Button(frame3, text="All white", bg=('white'), font=(200), command=seq)
colourGreen = Button(frame3, text="All Black", fg=('white'), bg=('black'), font=(200), command=seq2)
colourBlue = Button(frame3, text="X Pattern", bg=('gold'), font=(200), command=seq3)
w = [0]
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