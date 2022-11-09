from tkinter import *
# Variable to define the axis angle
values = [0,20,30,40,50,60,70,90]
# Function to choose colour
def choose_colour(button_pressed):
    global colour #value of the colour selected
    colour = button_pressed

# Functions to print "Button Pressed" Results
def red_pressed(r, c): 
    global colour
    if colour == 0:
        button[r][c].config(bg='grey99') #to configure the background colour of the grid selected with the selected colour
        value[r][c] = colour #assign the grid's angle value based on the colour selected
    elif colour == 20:
        button[r][c].config(bg='grey88')
        value[r][c] = colour
    elif colour == 30:
        button[r][c].config(bg='grey77')
        value[r][c] = colour
    elif colour == 40:
        button[r][c].config(bg='grey66')
        value[r][c] = colour
    elif colour == 50:
        button[r][c].config(bg='grey44')
        value[r][c] = colour
    elif colour == 60:
        button[r][c].config(bg='grey33')
        value[r][c] = colour
    elif colour == 70:
        button[r][c].config(bg='grey11')
        value[r][c] = colour
    else:
        button[r][c].config(bg='grey1') 
        value[r][c] = colour

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
            if r == c or r+c == o-1: #black x pattern 
                button[r][c].config(bg='grey1')
                value[r][c] = values[7]
            else: 
                button[r][c].config(bg='grey99') #white background
                value[r][c] = values[0]

def seq4():
    global colours, colour, values
    colours = ['grey99','grey88','grey77','grey66','grey44','grey33','grey11','grey1']
    p = -1 #variable for colour list 
    for r in range(o):
        for c in range(o):
            p = p+1
            if p > len(colours)-1:
                p = 0
            button[r][c].config(bg=colours[p])
            value[r][c] = values[p]

def seq5():
    global colour, colours, values
    print(value)

# Main GUI Windows
main = Tk()
main.title("Tutorial 2 Sample")

frame1 = Frame(main) #frame for grid
frame1.grid(row=0, column=0)

frame2 = Frame(main) #frame for colour selection button
frame2.grid(row=0, column=1)

frame3 = Frame(main) #frame for fixed pattern/sequence and send image button
frame3.grid(row=1 , column=0, columnspan=2)

# Colour Section (Using Button Widget)
colour = 0 #default value of the colour selected
o = 32 #defining the number of row & column on the grid

#32 x 32 button grid
button = [[r for r in range(o)] for c in range(o)] #variable to store and define the button's row and column 
value = [[colour for r in range(o)] for c in range(o)] #variable to store and define the button's axis angle based on the buttons' colour

for r in range(o):
    for c in range(o):
        button[r][c] = Button(frame1, bg="white", text="  ", font=('Arial',5), command=lambda m=r, l=c:red_pressed(m, l)) # red_pressed to pass down the row and column value to configure the button's colour and axis angle
        button[r][c].grid(row=r, column=c) 
        value[r][c] = colour #assigning the buttton's axis angle based on the corresponding colour
        
#pattern/sequence/send image button
colourRed = Button(frame3, text="All white", bg=('white'), font=(200), command=seq)
colourGreen = Button(frame3, text="All Black", fg=('white'), bg=('black'), font=(200), command=seq2) #fg for font colour bg for background colour
colourBlue = Button(frame3, text="X Pattern", bg=('gold'), font=(200), command=seq3)
colourGold = Button(frame3, text="Sequence", bg=('pink'), font=(200), command=seq4)
colourOrange = Button(frame3, text="Send Image!", bg=('white'), font=(200), command=seq5) #send the value of the corresponding axis angle on the format of list of list
colourRed.grid(row=0, column=0)
colourGreen.grid(row=0, column=1)
colourBlue.grid(row=0, column=2)
colourGold.grid(row=0, column=3)
colourOrange.grid(row=1, columnspan=2, column=1)

#colour selection button
colourgrey = Button(frame2, text="White", bg=('grey99'), height=1 , width=4 , font=(200), command=lambda m=0:choose_colour(m))
colourgrey1 = Button(frame2, text="Grey1", bg=('grey88'), height=1 , width=4 , font=(200), command=lambda m=20:choose_colour(m))
colourgrey2 = Button(frame2, text="Grey2", bg=('grey77'), height=1 , width=4 , font=(200), command=lambda m=30:choose_colour(m))
colourgrey3 = Button(frame2, text="Grey3", bg=('grey66'), height=1 , width=4 , font=(200), command=lambda m=40:choose_colour(m))
colourgrey4 = Button(frame2, text="Grey4", fg=('white'), bg=('grey55'), height=1 , width=4 , font=(200), command=lambda m=50:choose_colour(m))
colourgrey5 = Button(frame2, text="Grey5", fg=('white'), bg=('grey33'), height=1 , width=4 , font=(200), command=lambda m=60:choose_colour(m))
colourgrey6 = Button(frame2, text="Grey6", fg=('white'), bg=('grey11'), height=1 , width=4 , font=(200), command=lambda m=70:choose_colour(m))
colourblack = Button(frame2, text="Black", fg=('white'), bg=('grey1'), height=1 , width=4 , font=(200), command=lambda m=90:choose_colour(m))
colourgrey.grid(row=0, column=1)
colourgrey1.grid(row=1, column=1)
colourgrey2.grid(row=2, column=1)
colourgrey3.grid(row=3, column=1)
colourgrey4.grid(row=4, column=1)
colourgrey5.grid(row=5, column=1)
colourgrey6.grid(row=6, column=1)
colourblack.grid(row=7, column=1)

main.mainloop()