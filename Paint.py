import tkinter as tk
import tkinter.filedialog as filedialog
from tkinter import colorchooser
from tkinter import *
from PIL import ImageGrab
from django.utils.termcolors import background

root = tk.Tk()
root.title("My First Paint App")
root.geometry("1000x700")

canvas = tk.Canvas(root, bg="white", width=600, height=600)
canvas.pack(pady=10) #padding is the spacing between the designs
brush_color = "black"

brush_size = tk.IntVar(value=5)
eraser_size = tk.IntVar(value=5 )

#background_color = ("white")

is_eraser = tk.BooleanVar(value=False)

def paint(event):
    size = brush_size.get()
    color = brush_color
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill=color, width=size, outline=brush_color)

canvas.bind("<B1-Motion>", paint)

def choose_brush_color():
    global brush_color
    color = colorchooser.askcolor(title="Choose Brush Color")[1]
    if color[1]:
        brush_color = color

def choose_background_color():
    color = colorchooser.askcolor(title="Choose Background Color")[1]
    if color[1]:
        canvas.config(bg=color)

slider = tk.Scale(root, from_=1, to=50, orient=HORIZONTAL, variable=brush_size)
slider.pack()
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

color_frame = tk.Frame(root)
color_frame.pack(pady=10)

color_button = tk.Button(color_frame, text="Choose Color", command=choose_brush_color)
color_button.pack(side=LEFT , padx=10)

background_color_button = tk.Button(color_frame, text="Choose Background Color", command=choose_background_color)
background_color_button.pack(side=LEFT , padx=10)

brush_size_scale = tk.Scale(root, from_=1, to=50, orient=HORIZONTAL, variable=brush_size)

#adding eraser tool
def use_brush():
    is_eraser.set(False)

def use_eraser():
    is_eraser.set(False)

def clear_canvas():
    canvas.delete("all")
    canvas.config(bg="white")

def save_canvas():
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x+canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    file_path = filedialog.asksaveasfilename(defaultextension = ".png",filetypes=[("PNG files","*.png")])

brush_slider = tk.Scale(root, from_=1, to=50, orient=HORIZONTAL, label="Eraser Size", variable = eraser_size)
brush_slider.pack()


eraser_btn = tk.Scale(root, from_=1, to = 50 , orient=HORIZONTAL)











root.mainloop()
