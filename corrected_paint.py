import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import ImageGrab

# Create main window
root = tk.Tk()
root.title("Drawing App - Complete")
root.geometry("600x600")

# Global Variables
brush_color = "black"
background_color = "white"
brush_size = tk.IntVar(value=5)
eraser_size = tk.IntVar(value=10)
is_eraser = tk.BooleanVar(value=False)

# Canvas
canvas = tk.Canvas(root, bg=background_color, width=600, height=350)
canvas.pack(pady=10)

# Drawing function
def paint(event):
    color = background_color if is_eraser.get() else brush_color
    size = eraser_size.get() if is_eraser.get() else brush_size.get()
    x1, y1 = event.x - size, event.y - size
    x2, y2 = event.x + size, event.y + size
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)

canvas.bind("<B1-Motion>", paint)

# Tool Functions
def choose_brush_color():
    global brush_color
    color = colorchooser.askcolor(title="Choose Brush Color")[1]
    if color:
        brush_color = color

def choose_background_color():
    global background_color
    color = colorchooser.askcolor(title="Choose Background Color")[1]
    if color:
        background_color = color
        canvas.config(bg=color)

def use_brush():
    is_eraser.set(False)

def use_eraser():
    is_eraser.set(True)

def clear_canvas():
    canvas.delete("all")
    canvas.config(bg=background_color)

def save_canvas():
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if file_path:
        ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)

# UI Elements
tk.Scale(root, from_=1, to=50, orient="horizontal", label="Brush Size", variable=brush_size).pack()
tk.Scale(root, from_=1, to=50, orient="horizontal", label="Eraser Size", variable=eraser_size).pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Brush Color", command=choose_brush_color).pack(side="left", padx=5)
tk.Button(btn_frame, text="Background Color", command=choose_background_color).pack(side="left", padx=5)
tk.Button(btn_frame, text="Use Brush", command=use_brush).pack(side="left", padx=5)
tk.Button(btn_frame, text="Use Eraser", command=use_eraser).pack(side="left", padx=5)
tk.Button(btn_frame, text="Clear Canvas", command=clear_canvas).pack(side="left", padx=5)
tk.Button(btn_frame, text="Save Image", command=save_canvas).pack(side="left", padx=5)

root.mainloop()