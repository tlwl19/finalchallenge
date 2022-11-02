from tkinter import *

values = [0,20,30,40,50,60,70,90]
# Function to choose colour
def choose_colour(button_pressed):
    global colour
    colour = button_pressed
    print("Colour choice is {}".format(colour))
# Functions to print "Button Pressed" Results
def red_pressed(r, c):
    global colour
    if colour == 0:
        button[r][c].config(bg='grey99')
        value[r][c] = 0
    elif colour == 20:
        button[r][c].config(bg='grey88')
        value[r][c] = 20
    elif colour == 30:
        button[r][c].config(bg='grey77')
        value[r][c] = 30
    elif colour == 40:
        button[r][c].config(bg='grey66')
        value[r][c] = 40
    elif colour == 50:
        button[r][c].config(bg='grey44')
        value[r][c] = 50
    elif colour == 60:
        button[r][c].config(bg='grey33')
        value[r][c] = 60
    elif colour == 70:
        button[r][c].config(bg='grey11')
        value[r][c] = 70
    else:
        button[r][c].config(bg='grey1') 
        value[r][c] = 90
    #print("Button Pressed is RED!")

def seq():
    global values
    for r in range(o):
        for c in range(o):
            button[r][c].config(bg='grey99')
            value[r][c] = values[0]

def seq2():
    global values
    for r in range(o):
        for c in range(o):
            button[r][c].config(bg='grey1')
            value[r][c] = values[7]

def seq3():
    global values
    for r in range(o):
        for c in range(o):
            if r == c or r+c == o-1:
                button[r][c].config(bg='grey1')
                value[r][c] = values[7]
            else:
                button[r][c].config(bg='grey99')
                value[r][c] = values[0]
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
            # else:
            #     button[r][c].config(bg='grey99')
            #     value[r][c] == 0
            #00 01 02 03 04
            #10 11 12 13 14
            #20 21 22 23 24
            #30 31 32 33 34
            #40 41 42 43 44
    

def seq4():
    global w, colours, colour, values
    colours = ['grey99','grey88','grey77','grey66','grey44','grey33','grey11','grey1']
    #colours = ['white','#DCDCDC','#BEBEBE','#989898','#696969','#404040','#101010','black']
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
                value[r][c] = values[p]
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
                value[r][c] = values[p]
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
                value[r][c] = values[p]
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
                value[r][c] = values[p]
                #print (p)  

def seq5():
    global w, colour, colours, values
    # for r in range(o):
    #     for c in range(o):
            # if colour == 0:
            #     value[r][c] = 0
            # elif colour == 20:
            #     value[r[c]] = 20
            # elif colour == 30:
            #     value[r][c] = 30
            # elif colour == 40:
            #     value[r][c] = 40 
            # elif colour == 50:
            #     value[r][c] = 50
            # elif colour == 60:
            #     value[r][c] = 60  
            # elif colour == 70:
            #     value[r][c] = 70
            # else:
            #     value[r][c] = 90
    print(value)
    
    

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
o = 5 #o represent the number of row & column

#grid0 = Button(main, bg=('white') , command=red_pressed , height=2, width=2)
#grid0.grid(column=0, row=0)

#grid0 = Button(main, bg=('white') , command=red_pressed , height=2, width=2)
#grid0.grid(column=0, row=0)

#button = [[r for r in range(3)] c for c in range(3)]
button = [[r for r in range(o)] for c in range(o)]
value = [[colour for r in range(o)] for c in range(o)]

for r in range(o):
    for c in range(o):
        #button[r][c] = Button(frame1, bg="white", text="   ", font=('Arial',21), command=lambda m=r, l=c:red_pressed(m, l))
        button[r][c] = Button(frame1, bg="white", text="  ", font=('Arial',5), command=lambda m=r, l=c:red_pressed(m, l))
        button[r][c].grid(row=r, column=c)
        value[r][c] = colour
        

colourRed = Button(frame3, text="All white", bg=('white'), font=(200), command=seq)
colourGreen = Button(frame3, text="All Black", fg=('white'), bg=('black'), font=(200), command=seq2)
colourBlue = Button(frame3, text="X Pattern", bg=('gold'), font=(200), command=seq3)
w = [0]
colourGold = Button(frame3, text="Sequence", bg=('pink'), font=(200), command=seq4)
colourOrange = Button(frame3, text="Send Image!", bg=('white'), font=(200), command=seq5)
colourRed.grid(row=0, column=0)
colourGreen.grid(row=0, column=1)
colourBlue.grid(row=0, column=2)
colourGold.grid(row=0, column=3)
colourOrange.grid(row=1, columnspan=2, column=1)

colourgrey = Button(frame2, text="White", bg=('grey99'), font=(200), command=lambda m=0:choose_colour(m))
colourgrey1 = Button(frame2, text="Grey1", bg=('grey88'), font=(200), command=lambda m=20:choose_colour(m))
colourgrey2 = Button(frame2, text="Grey2", bg=('grey77'), font=(200), command=lambda m=30:choose_colour(m))
colourgrey3 = Button(frame2, text="Grey3", bg=('grey66'), font=(200), command=lambda m=40:choose_colour(m))
colourgrey4 = Button(frame2, text="Grey4", fg=('white'), bg=('grey55'), font=(200), command=lambda m=50:choose_colour(m))
colourgrey5 = Button(frame2, text="Grey5", fg=('white'), bg=('grey33'), font=(200), command=lambda m=60:choose_colour(m))
colourgrey6 = Button(frame2, text="Grey6", fg=('white'), bg=('grey11'), font=(200), command=lambda m=70:choose_colour(m))
colourblack = Button(frame2, text="Black", fg=('white'), bg=('grey1'), font=(200), command=lambda m=90:choose_colour(m))
colourgrey.grid(row=0, column=1)
colourgrey1.grid(row=1, column=1)
colourgrey2.grid(row=2, column=1)
colourgrey3.grid(row=3, column=1)
colourgrey4.grid(row=4, column=1)
colourgrey5.grid(row=5, column=1)
colourgrey6.grid(row=6, column=1)
colourblack.grid(row=7, column=1)

main.mainloop()