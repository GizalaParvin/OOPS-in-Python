import tkinter as tk

def draw_shapes(canvas):
    # Straight line
    canvas.create_line(10, 10, 200, 200, fill="blue", width=3)
    
    # Polyline
    canvas.create_line(10, 10, 50, 100, 100, 10, fill="red", width=2)
    
    # Dashed line
    canvas.create_line(10, 50, 200, 50, fill="green", width=2, dash=(5, 2))
    
    # Rectangle
    canvas.create_line(100, 100, 200, 100, 200, 200, 100, 200, 100, 100, fill="black", width=2)
    
    # Square
    canvas.create_line(250, 100, 350, 100, 350, 200, 250, 200, 250, 100, fill="blue", width=2)
    
    # Triangle
    canvas.create_line(150, 250, 100, 350, 200, 350, 150, 250, fill="red", width=2)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

draw_shapes(canvas)

root.mainloop()
