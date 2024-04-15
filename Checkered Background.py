import tkinter as tk
SIZE = 20
root = tk.Tk()

canvas = tk.Canvas(root)
canvas.pack()

color = 'white'

for y in range(8):

    for x in range(8):
        x1 = x*SIZE
        y1 = y*SIZE
        x2 = x1 + SIZE
        y2 = y1 + SIZE
        canvas.create_rectangle((x1, y1, x2, y2), fill=color)
        if color == 'white':
            color = 'Pink'
        else:    
            color = 'white'

    if color == 'white':
        color = 'Pink'
    else:    
        color = 'white'

root.mainloop()  