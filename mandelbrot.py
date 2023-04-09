import tkinter as tk

# Define the function to calculate the Mandelbrot set
def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < 255:
        z = z*z + c
        n += 1
    if n == 255:
        return "#FFFFFF" # black if in the set
    else:
        return "#" + "{0:02x}{1:02x}{2:02x}".format(n, n, n) # gray scale based on iteration count

# Define the parameters of the Mandelbrot set


xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 500, 500

# Create the Tkinter window and canvas
window = tk.Tk()
canvas = tk.Canvas(window, width=width, height=height, bg="#FFFFFF")
canvas.pack()

# Draw the Mandelbrot set on the canvas
for x in range(width):
    for y in range(height):
        c = complex(xmin + (xmax - xmin) * x / width, ymin + (ymax - ymin) * y / height)
        color = mandelbrot(c)
        canvas.create_line(x, y, x+1, y+1, fill=color)

# Start the Tkinter event loop
window.mainloop()
