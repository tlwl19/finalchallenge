# <u>**32 x 32 Pixel-Tint GUI**</u>

The 32x32 Pixel-Tint system GUI explores the phenomena of light leveraging on electromechanical systems that manipulate polarization to synergize pixelized art forms. 

![](images/overall.png)

The 32x32 Pixel-Tint GUI allows the user to choose from an array of 8 different shades of grey and the preset patterns to the squares within the 32x32 grid. The "Send Image!" button outputs a total of 1024 buttons of the colour value according to the preset patterns that are chosen. 

<br>

## **Hardware** 
1. Single Board Computer: Raspberry Pi 4 Model B
2. Operating System: Raspbian Buster Full

<br>

## **Installation** 
<br>
Take Note: Only to update Raspberry Pi on the first intial boot

<font size = "4">1. Update the Raspberry Pi</font> 

```
sudo apt update
sudo apt upgrade
```
<font size = "4">2. Configure Raspberry Pi</font> 

<font size = "3"> **Enable SSH** </font>

SSH is a network protocol that gives users, particularly system administrators, a secure way to access a computer over an unsecured network. To enable SSH type the following:

```
sudo raspi-config
```
Select `3 Interface Options` <br>
Select `P2 SSH` <br>
Select ***Enable SSH***

<br>

<font size = "3"> **Enable Virtual Network Computing (VNC)** </font>
<br>
VNC is a cross-platform screen sharing system that was created to remotely control another computer. To enable VNC type the following:
```
sudo raspi-config
```
Select `3 Interface Options` <br>
Select `P3 VNC` <br>
Select ***Enable VNC***







## <u>Features</u>

## **Grid:** 

![](images/32grid.png)

A 32x32 grid that allows the user to interact with by clicking on them and changing the shade of grey to individual squares however they may like.

<br>

## **Shade Selections:** 

![](images/shades.png)

8 buttons for 8 different shades of grey for the user to pick any colour they prefer.

<br>

## Sample Outcome:
![](images/shades_outcome.png)

<br>

## **All White Button:** 

![](images/allwhitebutton.png)

All White button changes the shade of the whole grid to white.

<br>

## Sample Outcome:
![](images/allwhite_outcome.png)

<br>

## **All Black Button:** 

![](images/allblackbutton.png)

All Black button changes the shade of the whole grid to black.

<br>

## Sample Outcome:

![](images/allblack_outcome.png)

<br>

## **X Pattern Button:** 

![](images/xpatternbutton.png)

X Pattern button changes the whole grid into a cross pattern.

<br>

## Sample Outcome:

![](images/xpattern_outcome.png)

<br>

## **Sequence Button:** 

![](images/sequencebutton.png)

Sequence button changes the whole grid into a specific sequence of shades. Our sequence of colour goes from white to black.

<br>

## Sample Outcome:

![](images/sequence_outcome.png)

<br>

## **Send Image Button:** 

![](images/sendimagebutton.png)

To generate a List of List in which the output consists of 32 rows and 32 columns of values.

<br>

## Sample Outcome:

![](images/sendimage_outcome.png)

<br>

# <u>How The Code Works</u>

## **Grid:** 

> A 32x32 grid that allows the user to interact with by clicking on the buttons and changing the shade of grey on individual buttons however they may like.

<br>

>what to write

```
values = [0,20,30,40,50,60,70,90]
```

<br>

>We have assigned the default value of the colour to 0.
This colour variable is to assign the button's background colour and its angle to 0, and also to make the individual squares in the grid white by default.

```
colour = 0
```

<br>

>what to write

```
def red_pressed(r, c): 
    global colour
    if colour == 0:
        button[r][c].config(bg='grey99') 
        value[r][c] = colour
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
```

<br>

>"o" represents the number of rows and columns we would want in our grid. In this case, we want 32 rows and 32 columns in our grid.



```
o = 32
```
>Afterwards, we created a `for loop` in which both rows and columns will be generated.<br> 
The "button" variable is for us to be able to interact with the individual squares as buttons within the 32x32 grid.<br> 
The "value" variable is to store the angle value of the corresponding grid according to the colour selected<br>r = rows<br>c = columns
```
button = [[r for r in range(o)] for c in range(o)]
value = [[colour for r in range(o)] for c in range(o)]

for r in range(o):
    for c in range(o):
        button[r][c] = Button(frame1, bg="white", text="  ", font=('Arial',5), command=lambda m=r, l=c:red_pressed(m, l))
        button[r][c].grid(row=r, column=c) 
        value[r][c] = colour

```


## **Shade Selections:** 

> 8 buttons for 8 different shades of grey for the user to pick whichever shade they prefer.It's for us to be able to select the different shades of grey of the individual squares within the 32x32 grid.

```
colourblack = Button(frame2, text="Black", fg=('white'), bg=('grey1'), font=(200), command=lambda m=90:choose_colour(m))
colourblack.grid(row=0, column=1)
```

## **All White Button:** 

> Changes the shade of the whole grid to white.
```
colourRed = Button(frame3, text="All white", bg=('white'), font=(200), command=seq)
colourRed.grid(row=0, column=0)

def seq():
    global values
    for r in range(o):
        for c in range(o):
            button[r][c].config(bg='grey99')
            value[r][c] = values[0]
```

## **All Black Button:** 

> Changes the shade of the whole grid to black.
```
colourGreen = Button(frame3, text="All Black", fg=('white'), bg=('black'), font=(200), command=seq2)
colourGreen.grid(row=0, column=1)

def seq2():
    global values
    for r in range(o):
        for c in range(o):
            button[r][c].config(bg='grey1')
            value[r][c] = values[7]
```

## **X Pattern Button:** 

> Displays a cross pattern on the grid.
```
colourBlue = Button(frame3, text="X Pattern", bg=('gold'), font=(200), command=seq3)
colourBlue.grid(row=0, column=2)

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
```

`r == c` is for the diagonal line from top left to bottom right of the 32x32 grid.

`r+c == o-1` is for the diagonal line from top right to bottom left of the 32x32 grid.

If either one of the arguments are true, `button[r][c].config(bg='grey1')` will change the colour of the individual squares to black.
<br>
`value[r][c] = values[7]` changes the value of the individual squares' (that fulfill either of the two arguments') angles to 90.

<br>

If neither are true, `button[r][c].config(bg='grey99')` will change the colour of the individual squares to white. 
<br>
`value[r][c] = values[0]` changes the value of the individual squares' (that fulfill neither of the two arguments') angles to 0.


<br>

## **Sequence Button:** 

> Changes the whole grid into a specific sequence of shades.
```
colourGold = Button(frame3, text="Sequence", bg=('pink'), font=(200), command=seq4)
colourGold.grid(row=0, column=3)
```
>Creates button to create a sequence pattern
```
def seq4():
    global colours, colour, values
    colours = ['grey99','grey88','grey77','grey66','grey44','grey33','grey11','grey1']
    p = -1 
    for r in range(o):
        for c in range(o):
            p = p+1
            if p > len(colours)-1:
                p = 0
            button[r][c].config(bg=colours[p])
            value[r][c] = values[p]
```
`colours = ['grey99','grey88','grey77','grey66','grey44','grey33','grey11','grey1']` defines the array of colors that will be displayed in this sequence pattern.
<br>

By making `p = -1` , we make it so that the very first square of the grid will start as white, the first color (`grey99`) in the array. 
<br>

`p = p+1` will continue the pattern within the grid by increasing the values within the array by an increment of 1, until it reaches the end of the colour array.
<br>

Once the first sequence within the grid reaches the end of the array (`grey1`), the line `p = 0` will ensure that the array will be reset to 0 (`grey99` or white). This is achieved by the if statement `if p > len(colours)-1`, where `len(colours)-1` will give the array value of 7 (8-1 = 7), and that the array value should not go beyond 7.
<br>

Afterwards, since we are only contiuing the sequence, there is no need to use `p = -1` as the next square after the first sequence will be white, thus `p = 0` is used after the if statement.

## **Send Image Button:** 

> To generate a List of List in which the output consists of 32 rows and 32 columns of values.
```
colourOrange = Button(frame3, text="Send Image!", bg=('white'), font=(200), command=seq5)
colourOrange.grid(row=1, columnspan=2, column=1)

def seq5():
    global colour, colours, values
    print(value)
```
