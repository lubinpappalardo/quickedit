import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageOps
from rembg import remove

# Define color schemes
light_bg_color = "white"
dark_bg_color = "#1E1E1E"
light_text_color = "black"
dark_text_color = "white"
light_active_color = "#e8e8e8"
dark_active_color = "#363636"
light_active_color_fg = "black"
dark_active_color_fg = "white"
light_theme = "Light theme"
dark_theme = "Dark theme"

# Define toggle function to switch between light and dark modes
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
    title.config(bg=bg_color, fg=text_color)
    input_path_entry.config(bg=bg_color, fg=text_color)
    browse_button.config(bg=bg_color, fg=text_color, activebackground=active_color, activeforeground=active_color_fg)
    remove_bg_button.config(bg=bg_color, fg=text_color, activebackground=active_color, activeforeground=active_color_fg)
    invert_colors_button.config(bg=bg_color, fg=text_color, activebackground=active_color, activeforeground=active_color_fg)
    desaturate_button.config(bg=bg_color, fg=text_color, activebackground=active_color, activeforeground=active_color_fg)
    status_label.config(bg=bg_color, fg=text_color)
    toggle_button.config(text=theme, bg=bg_color, fg=text_color, activebackground=active_color, activeforeground=active_color_fg)

def browse_file():
    # Open a file dialog
    default_dir = os.path.expanduser("~/Pictures") # path to default images directory
    file_path = filedialog.askopenfilename(
        initialdir=default_dir,
        title="Select a file",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    # Insert selected file path in the entry field
    input_path_entry.delete(0, 'end')
    input_path_entry.insert(0, file_path)

def remove_bg():
    # Get input and output paths from the entry fields
    input_path = input_path_entry.get()
    name = input_path.split(".")
    filename = name[0]
    output_path = f'{filename} - removed_bg.png'

    input = Image.open(input_path)

    output = remove(input)
    output.save(output_path)
    status_label.configure(text="File saved as " + output_path)


def desaturate():
    input_path = input_path_entry.get()
    name = input_path.split(".")
    filename = name[0]
    output_path = f'{filename} - desaturated.png'
    print(input_path)
    input = Image.open(input_path)
    print(input)
    output = ImageOps.grayscale(input)
    output.save(output_path)
    status_label.config(text="File saved as " + output_path)

def invert_colors():
    input_path = input_path_entry.get()
    name = input_path.split(".")
    filename = name[0]
    output_path = f'{filename} - inverted_colors.png'

    input = Image.open(input_path)
    output = ImageOps.invert(input)
    output.save(output_path)
    status_label.config(text="File saved as " + output_path)
    
# Set dark mode as default
is_dark_mode = True
bg_color = dark_bg_color
text_color = dark_text_color
active_color = dark_active_color
active_color_fg = dark_active_color_fg
theme = light_theme

root = Tk()
root.title("Quick image edit")
root.config(bg=dark_bg_color)
root.minsize(500, 400)
#root.iconbitmap(os.path.abspath("quickedit.ico"))

frame = Frame(root, bg=bg_color)
frame.grid(row=0, column=0, padx=5, pady=5)

title = Label(frame, text="Quick image edit", font=("Arial", 24), bg=bg_color, fg=text_color)
title.grid(row=0, column=1, padx=5, pady=20, sticky="ew")

# Create a label and entry field for input file path
browse_button = Button(frame, text="Choose file", relief="raised", activebackground=active_color, activeforeground=active_color_fg, command=browse_file, bg=bg_color, fg=text_color)
browse_button.grid(row=1, column=1, padx=5, pady=(5,20))
input_path_entry = Entry(frame, width=25, bg=bg_color, fg=text_color)
input_path_entry.grid(row=1, column=1, padx=5, pady=(60,20))

# Create a button to remove the background
remove_bg_button = Button(frame, text="Remove Background", width=20, relief="raised", activebackground=active_color, activeforeground=active_color_fg, command=remove_bg, bg=bg_color, fg=text_color)
remove_bg_button.grid(row=2, column=1, padx=5, pady=5)
# Create a button to invert colors
invert_colors_button = Button(frame, text="Invert Colors", width=20, relief="raised", activebackground=active_color, activeforeground=active_color_fg, command=invert_colors, bg=bg_color, fg=text_color)
invert_colors_button.grid(row=3, column=1, padx=5, pady=5)
# Create a button to desaturate
desaturate_button = Button(frame, text="Desaturate", width=20, relief="raised", activebackground=active_color, activeforeground=active_color_fg, command=desaturate, bg=bg_color, fg=text_color)
desaturate_button.grid(row=4, column=1, padx=5, pady=5)

# Create a label to display the status message
status_label = Label(frame, text="", bg=bg_color, fg=text_color)
status_label.grid(row=5, column=1, padx=5, pady=5)

# Create a button to toggle between light and dark modes
toggle_button = Button(frame, text=theme, relief="raised", activebackground=active_color, activeforeground=active_color_fg, command=toggle_theme, bg=bg_color, fg=text_color)
toggle_button.grid(row=6, column=1, padx=5, pady=(5, 20))


# center the frame horizontally and vertically within the root window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# this will center the frame both horizontally and vertically within the root window
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

def do_nothing():
  pass

def quit():
  root.destroy()

def link():
  url = "https://github.com/txoriurdina"
  os.system("start " + url)

# create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# create a file menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# create a help menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=link)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.mainloop()
