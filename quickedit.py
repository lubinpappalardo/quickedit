import os
import tkinter.font as tkFont
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageOps, ImageFilter, ImageTk
from rembg import remove
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

#---------------------------------------COLORS AND THEME---------------------------------------

light_bg_color = "white"
dark_bg_color = "#1E1E1E"
light_text_color = "black"
dark_text_color = "white"
light_active_color = "#e8e8e8"
dark_active_color = "#0a0a0a"
dark_bg_button_color = "#373737"
light_active_color_fg = "black"
dark_active_color_fg = "white"
light_theme = "Light theme"
dark_theme = "Dark theme"

def toggle_theme():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    bg_color = dark_bg_color if is_dark_mode else light_bg_color
    text_color = dark_text_color if is_dark_mode else light_text_color
    active_color = dark_active_color if is_dark_mode else light_active_color
    active_color_fg = dark_active_color_fg if is_dark_mode else light_active_color_fg
    theme = light_theme if is_dark_mode else dark_theme
    root.config(bg=bg_color)
    frame.config(bg=bg_color)
    left_side.config(bg=bg_color)
    right_side.config(bg=bg_color)
    bottom_left_side.config(bg=bg_color)
    bottom_right_side.config(bg=bg_color)
    save_button.config(bg=bg_color, fg=text_color, activebackground=active_color, activeforeground=active_color_fg)
    browsing_box.config(bg=bg_color)
    title.config(bg=bg_color, fg=text_color)
    image.config(bg=bg_color)
    small_image.config(bg=bg_color)
    input_path_entry.config(bg=bg_color, fg=text_color)
    browse_button.config(bg=bg_color, fg=text_color, activebackground=active_color, activeforeground=active_color_fg)
    reset_button.config(bg=bg_color, fg=text_color, activebackground=active_color, activeforeground=active_color_fg)
    remove_bg_button.config(bg=bg_color, fg=text_color, activebackground=active_color, activeforeground=active_color_fg)
    invert_colors_button.config(bg=bg_color, fg=text_color, activebackground=active_color, activeforeground=active_color_fg)
    desaturate_button.config(bg=bg_color, fg=text_color, activebackground=active_color, activeforeground=active_color_fg)
    flip_button.config(bg=bg_color, fg=text_color, activebackground=active_color, activeforeground=active_color_fg)
    rotate_button.config(bg=bg_color, fg=text_color, activebackground=active_color, activeforeground=active_color_fg)
    rotate_entry.config(bg=bg_color, fg=text_color)
    filter_button.config(bg=bg_color, fg=text_color, activebackground=active_color, activeforeground=active_color_fg)
    filter_options.config(bg=bg_color, fg=text_color)
    status_label.config(bg=bg_color, fg=text_color)

#---------------------------------------IMAGE EDIT FUNCTIONS AND BROWSE FILES---------------------------------------

def browse_file():
    global img, img_width
    default_dir = os.path.expanduser("~/Pictures")
    file_path = filedialog.askopenfilename(
        initialdir=default_dir,
        title="Select a file",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    input_path_entry.delete(0, 'end')
    input_path_entry.insert(0, file_path)

    output_path = r"{}".format(file_path.replace("/", "\\"))
    img = Image.open(output_path)
    aspect_ratio = img.size[1] / img.size[0]  # calculate aspect ratio
    new_width = img_width
    new_height = int(new_width * aspect_ratio)
    resized_img = img.resize((new_width, new_height), Image.ANTIALIAS) 
    img_tk = ImageTk.PhotoImage(resized_img) 
    root.img_tk = img_tk
    image.config(image=img_tk)

    new_width = 100
    new_height = int(new_width * aspect_ratio)
    resized_img = img.resize((new_width, new_height), Image.ANTIALIAS) 
    small_img_tk = ImageTk.PhotoImage(resized_img) 
    root.small_img_tk = small_img_tk
    small_image.config(image=small_img_tk)
    

def save():
    global output_path, output
    output.save(output_path)
    status_label.configure(text="File saved as " + output_path)
    file_path = status_label.cget("text")[14:]
    os.startfile(file_path)

def reset():
    global output, output_path
    output, output_path = None, None
    input_path = input_path_entry.get()
    img = Image.open(input_path)
    aspect_ratio = img.size[1] / img.size[0]  # calculate aspect ratio
    new_width = img_width
    new_height = int(new_width * aspect_ratio)
    resized_img = img.resize((new_width, new_height), Image.ANTIALIAS) 
    img_tk = ImageTk.PhotoImage(resized_img) 
    root.img_tk = img_tk
    image.config(image=img_tk)

def remove_bg():
    global img, img_width, output, output_path
    input_path = input_path_entry.get()
    name = input_path.split(".")
    filename = name[0]
    if output == None:
        output_path = rf'{filename} - removed_bg.png'
        input = Image.open(input_path)
        output = remove(input)
    else:
        output = remove(output)
        output_path = rf'{filename} - edited.png'

    img = output
    aspect_ratio = img.size[1] / img.size[0]  # calculate aspect ratio
    new_width = img_width
    new_height = int(new_width * aspect_ratio)
    resized_img = img.resize((new_width, new_height), Image.ANTIALIAS) 
    img_tk = ImageTk.PhotoImage(resized_img) 
    root.img_tk = img_tk
    image.config(image=img_tk)

def grayscale():
    global img, img_width, output, output_path
    input_path = input_path_entry.get()
    name = input_path.split(".")
    filename = name[0]
    if output == None:
        output_path = rf'{filename} - grayscale.png'
        input = Image.open(input_path)
        output = ImageOps.grayscale(input)
    else:
        output = ImageOps.grayscale(output)
        output_path = rf'{filename} - edited.png'

    img = output
    aspect_ratio = img.size[1] / img.size[0]  # calculate aspect ratio
    new_width = img_width
    new_height = int(new_width * aspect_ratio)
    resized_img = img.resize((new_width, new_height), Image.ANTIALIAS) 
    img_tk = ImageTk.PhotoImage(resized_img) 
    root.img_tk = img_tk
    image.config(image=img_tk)

def invert_colors():
    global img, img_width, output, output_path
    input_path = input_path_entry.get()
    name = input_path.split(".")
    filename = name[0]
    if output == None:
        output_path = rf'{filename} - inverted_colors.png'
        input = Image.open(input_path)
        output = ImageOps.invert(input)
    else:
        output = ImageOps.invert(output)
        output_path = rf'{filename} - edited.png'

    img = output
    aspect_ratio = img.size[1] / img.size[0]  # calculate aspect ratio
    new_width = img_width
    new_height = int(new_width * aspect_ratio)
    resized_img = img.resize((new_width, new_height), Image.ANTIALIAS) 
    img_tk = ImageTk.PhotoImage(resized_img) 
    root.img_tk = img_tk
    image.config(image=img_tk)

def flip():
    global img, img_width, output, output_path
    input_path = input_path_entry.get()
    name = input_path.split(".")
    filename = name[0]
    if output == None:
        output_path = rf'{filename} - flip.png'
        im = Image.open(input_path)
        output = im.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        output = output.transpose(Image.FLIP_LEFT_RIGHT)
        output_path = rf'{filename} - edited.png'

    img = output
    aspect_ratio = img.size[1] / img.size[0]  # calculate aspect ratio
    new_width = img_width
    new_height = int(new_width * aspect_ratio)
    resized_img = img.resize((new_width, new_height), Image.ANTIALIAS) 
    img_tk = ImageTk.PhotoImage(resized_img) 
    root.img_tk = img_tk
    image.config(image=img_tk)

def rotate():
    global img, img_width, output, output_path
    input_path = input_path_entry.get()
    degree = float(rotate_entry.get())
    name = input_path.split(".")
    filename = name[0]
    if output == None:
        output_path = rf'{filename} - rotate.png'
        input = Image.open(input_path)
        output = input.rotate(degree)
    else:
        output = output.rotate(degree)
        output_path = rf'{filename} - edited.png'

    img = output
    aspect_ratio = img.size[1] / img.size[0]  # calculate aspect ratio
    new_width = img_width
    new_height = int(new_width * aspect_ratio)
    resized_img = img.resize((new_width, new_height), Image.ANTIALIAS) 
    img_tk = ImageTk.PhotoImage(resized_img) 
    root.img_tk = img_tk
    image.config(image=img_tk)

def apply_filter():
    global img, img_width, output, output_path
    input_path = input_path_entry.get()
    filter_option = variable.get()
    name = input_path.split(".")
    filename = name[0]
    apply = getattr(ImageFilter, filter_option)
    if output == None:
        output_path = rf'{filename} - filter {filter_option}.png'
        input = Image.open(input_path)
        output = input.filter(apply)
    else:
        output_path = rf'{filename} - edited.png'
        output = output.filter(apply)

    img = output
    aspect_ratio = img.size[1] / img.size[0]  # calculate aspect ratio
    new_width = img_width
    new_height = int(new_width * aspect_ratio)
    resized_img = img.resize((new_width, new_height), Image.ANTIALIAS) 
    img_tk = ImageTk.PhotoImage(resized_img) 
    root.img_tk = img_tk
    image.config(image=img_tk)
    
#---------------------------------------SETUP---------------------------------------

is_dark_mode = True
bg_color = dark_bg_color
text_color = dark_text_color
active_color = dark_active_color
active_color_fg = dark_active_color_fg
bg_button_color = dark_bg_button_color
theme = light_theme

global img, img_width, output, output_path
img = None
img_width = 400
output = None
output_path = None

root = Tk()
root.title("Quick image edit")
root.config(bg=dark_bg_color)
root.minsize(980, 650)
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "quickedit.ico")
root.iconbitmap(icon_path)

h1_font_path = "Poppins-Bold.ttf"
h1 = tkFont.Font(family="Poppins", size=24, name=h1_font_path)
p_font_path = "Poppins-Regular.ttf"
p = tkFont.Font(family="Poppins", size=10, name=p_font_path)

#---------------------------------------LAYOUT OF THE APP---------------------------------------

frame = Frame(root, bg=bg_color)
frame.grid(row=0, column=0)

title = Label(frame, text="Quick image edit", font=h1, bg=bg_color, fg=text_color)
title.grid(row=0, column=1, pady=20, sticky="ew")

left_side = Frame(frame, bg=bg_color, highlightthickness=2, relief="solid", highlightbackground="#545454")
left_side.grid(row=1, column=0, padx=5, pady=5, sticky="n")

middle_side = Frame(frame, bg=bg_color)
middle_side.grid(row=1, column=1, padx=5, sticky="n")

right_side = Frame(frame, bg=bg_color)
right_side.grid(row=1, column=2, sticky="en")

bottom_left_side = Frame(frame, bg=bg_color)
bottom_left_side.grid(row=2, column=0, columnspan=2, sticky="w")

bottom_right_side = Frame(frame, bg=bg_color, width=100)
bottom_right_side.grid(row=2, column=2)

# Create a label to display the status message
status_label = Label(bottom_left_side, text="", bg=bg_color, fg=text_color, cursor="hand2")
status_label.grid(row=0, column=0, padx=5, pady=5)
def open(event):
    file_path = status_label.cget("text")[14:]
    os.startfile(file_path)
status_label.bind("<Button-1>", open)

save_button = Button(bottom_right_side, text="SAVE", relief="raised", width=22, activebackground=active_color, activeforeground=active_color_fg, command=save, bg="#4472c4", fg=text_color)
save_button.grid(row=0, column=0, sticky="e")

#------------------------ LEFT SIDE------------------------

#preview the image
image_path = os.path.join(script_dir, "quickedit.ico")
img = Image.open(image_path)
aspect_ratio = img.size[1] / img.size[0]  # calculate aspect ratio
new_width = 100
new_height = int(new_width * aspect_ratio)
resized_img = img.resize((new_width, new_height), Image.ANTIALIAS) 
small_img_tk = ImageTk.PhotoImage(resized_img) 
small_image = Label(left_side, image=small_img_tk, borderwidth=0, highlightthickness=0, bg=bg_color)
small_image.grid(row=0, column=0, sticky="n")

#------------------------MIDDLE SIDE------------------------

# Create a label and entry field for input file path
browsing_box = Frame(middle_side, bg=bg_color, width=img_width)
browsing_box.grid(row=2, column=0, sticky="w")
browse_button_width = 15
browse_button = Button(browsing_box, text="Choose file", font=p, relief="raised", width=browse_button_width, activebackground=active_color, activeforeground=active_color_fg, command=browse_file, bg=bg_button_color, fg=text_color)
browse_button.grid(row=0, column=0, padx=(0, 5), pady=5)
input_path_entry = Entry(browsing_box, width=46, bg=bg_color, fg=text_color, font=p)
input_path_entry.grid(row=0, column=1, padx=0, pady=5)

#preview the image
image_path = os.path.join(script_dir, "quickedit.ico")
img = Image.open(image_path)
aspect_ratio = img.size[1] / img.size[0]  # calculate aspect ratio
new_width = img_width
new_height = int(new_width * aspect_ratio)
resized_img = img.resize((new_width, new_height), Image.ANTIALIAS) 
img_tk = ImageTk.PhotoImage(resized_img) 
image = Label(middle_side, image=img_tk, borderwidth=0, highlightthickness=0, bg=bg_color)
image.grid(row=3, column=0)


#------------------------RIGHT SIDE------------------------

# Create a button to remove the background
reset_button = Button(right_side, text="Reset", font=p, width=20, relief="raised", activebackground=active_color, activeforeground=active_color_fg, command=reset, bg=bg_button_color, fg=text_color)
reset_button.grid(row=1, column=1, padx=5, pady=5)

# Create a button to remove the background
remove_bg_button = Button(right_side, text="Remove Background", font=p, width=20, relief="raised", activebackground=active_color, activeforeground=active_color_fg, command=remove_bg, bg=bg_button_color, fg=text_color)
remove_bg_button.grid(row=2, column=1, padx=5, pady=5)

# Create a button to invert colors
invert_colors_button = Button(right_side, text="Invert Colors", font=p, width=20, relief="raised", activebackground=active_color, activeforeground=active_color_fg, command=invert_colors, bg=bg_button_color, fg=text_color)
invert_colors_button.grid(row=3, column=1, padx=5, pady=5)

# Create a button to desaturate
desaturate_button = Button(right_side, text="Desaturate", font=p, width=20, relief="raised", activebackground=active_color, activeforeground=active_color_fg, command=grayscale, bg=bg_button_color, fg=text_color)
desaturate_button.grid(row=4, column=1, padx=5, pady=5)

# Create a button to flip
flip_button = Button(right_side, text="Flip", font=p, width=20, relief="raised", activebackground=active_color, activeforeground=active_color_fg, command=flip, bg=bg_button_color, fg=text_color)
flip_button.grid(row=5, column=1, padx=5, pady=5)

# Create a button to rotate
def clear_placeholder(event):
    rotate_entry.delete(0, END)
rotate_button = Button(right_side, text="Rotate", font=p, width=20, relief="raised", activebackground=active_color, activeforeground=active_color_fg, command=rotate, bg=bg_button_color, fg=text_color)
rotate_button.grid(row=6, column=1, padx=5, pady=5)
rotate_entry = Entry(right_side, font=p, width=20, bg=bg_color, fg=text_color)
rotate_entry.grid(row=7, column=1, padx=5, pady=(5, 10))
rotate_entry.bind("<FocusIn>", clear_placeholder)
rotate_entry.insert(0, "Enter angle to rotate...")

# Create a button to filter
filter_button = Button(right_side, text="Filter", font=p, width=20, relief="raised", activebackground=active_color, activeforeground=active_color_fg, command=apply_filter, bg=bg_button_color, fg=text_color)
filter_button.grid(row=8, column=1, padx=5, pady=5)
choices = ["BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE", "EMBOSS", "FIND_EDGES", "SHARPEN", "SMOOTH", "SMOOTH_MORE"]
variable = StringVar(right_side)
variable.set('Choose your filter')
filter_options = OptionMenu(right_side, variable, *choices)
filter_options.config(width=15, relief="raised", font=p, borderwidth=2, highlightthickness=0, activebackground=active_color, activeforeground=active_color_fg, bg=bg_color, fg=text_color)
filter_options.grid(row=9, column=1, padx=5, pady=(5, 10))


# center the frame horizontally and vertically
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# center the frame both horizontally and vertically
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

#---------------------------------------MENU BAR---------------------------------------

def quit():
  root.destroy()

def link():
  url = "https://github.com/txoriurdina/quickedit"
  os.system("start " + url)

# create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# create a file menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=browse_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# create a view menu
view_menu = Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Theme", command=toggle_theme)
menu_bar.add_cascade(label="View", menu=view_menu)

# create a help menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=link)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.mainloop()
