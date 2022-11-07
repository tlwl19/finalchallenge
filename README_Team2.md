## 32 x 32 Polarization Grid

Raspberry Pi Project on coding for a 32x32 grid that allows the user to change any grid box to different shades of grey.

## Features

**Grid:** 

A 32x32 grid that allows the user to interact with by clicking on them and changing the shade of grey to individual grids however they may like.

```
colour = 0
o = 3 

button = [[r for r in range(o)] for c in range(o)]
value = [[colour for r in range(o)] for c in range(o)]

for r in range(o):
    for c in range(o):
        button[r][c] = Button(frame1, bg="white", text="  ", font=('Arial',5), command=lambda m=r, l=c:red_pressed(m, l))
        button[r][c].grid(row=r, column=c) 
        value[r][c] = colour

```

**Shade Selections:** 

8 buttons for 8 different shades of grey for the user to pick any one they prefer.

```
colourblack = Button(frame2, text="Black", fg=('white'), bg=('grey1'), font=(200), command=lambda m=90:choose_colour(m))
colourblack.grid(row=0, column=1)
```

**All White Button:** 

Changes the shade of the whole grid to white.
```
colourRed = Button(frame3, text="All white", bg=('white'), font=(200), command=seq)
colourRed.grid(row=0, column=0)
```

**All Black Button:** 

Changes the shade of the whole grid to black.
```
colourGreen = Button(frame3, text="All Black", fg=('white'), bg=('black'), font=(200), command=seq2)
colourGreen.grid(row=0, column=1)
```

**X Pattern Button:** 

Changes the whole grid into a cross pattern.

**Sequence Button:** 

Changes the whole grid into a specific sequence of shades.

**Send Image Button:** 

## Setting Up The Code