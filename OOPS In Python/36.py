# celcius_temprature = [0,20,37,100]
# map_result = list(map(lambda c : (c * 9/5) + 32,celcius_temprature))
# print(map_result)


# #filter 
# numbers = [1,5,5,8,86,9,3]
# filter_result = list(filter(lambda x : x %2 !=0,numbers))
# print(filter_result)

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Canvas Example")

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Draw a line
#canvas.create_line(10, 10, 50, 100 , 100 , 10 ,fill="red", width=2)
canvas.create_line(100, 100, 200, 100, 200, 200, 100, 200, 100, 100, fill="black", width=2)


# Start the Tkinter event loop
root.mainloop()


