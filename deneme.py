import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import fonksiyon as fnc
import cv2

def stretch_image(event):
	global resized_tk

	# size 
	width = event.width
	height = event.height

	# create an image
	resized_image = image_original.resize((width, height))
	resized_tk = ImageTk.PhotoImage(resized_image)

	# place on the canvas
	canvas.create_image(0,0,image = resized_tk, anchor = 'nw')

def fill_image(event):
	global resized_tk

	# current ratio 
	canvas_ratio = event.width / event.height

	# get coordinates 
	if canvas_ratio > image_ratio: # canvas is wider than the image
		width = int(event.width) 
		height = int(width / image_ratio)
	else: # canvas is narrower than the image
		height = int(event.height)
		width = int(height * image_ratio) 

	resized_image = image_original.resize((width, height))
	resized_tk = ImageTk.PhotoImage(resized_image)
	canvas.create_image(
		int(event.width / 2),
		int(event.height / 2),
		anchor = 'center',
		image = resized_tk)

def show_full_image(event):
	global resized_tk
	# current ratio 
	canvas_ratio = event.width / event.height

	# get coordinates 
	if canvas_ratio > image_ratio: # canvas is wider than the image
		height = int(event.height)
		width = int(height * image_ratio) 
	else: # canvas is narrower than the image
		width = int(event.width) 
		height = int(width / image_ratio)



	resized_image = image_original.resize((width, height))
	resized_tk = ImageTk.PhotoImage(resized_image)
	canvas.itemconfig(image_container,image= resized_tk)

# exercise:
# create a third scaling behaviour to always show the full image without cutting off parts

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Images')

# grid layout
window.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
window.rowconfigure(0, weight = 1)
# import an image 
image_original = Image.open('Resimler/kameraman.jpg')
image_ratio = image_original.size[0] / image_original.size[1]
print(image_ratio)
image_tk = ImageTk.PhotoImage(image_original)

python_dark = Image.open('Resimler/python_dark.png').resize((30,30))
python_dark_tk = ImageTk.PhotoImage(python_dark)

img_ctk = ctk.CTkImage(
	light_image = Image.open('Resimler/python_dark.png'),
	dark_image = Image.open('Resimler/python_light.png'))

def a_clicked():

	abc_image = Image.open('Resimler/bubbles.png')
	abc_image_tk = ImageTk.PhotoImage(abc_image)
	canvas.itemconfig(image_container, image = abc_image_tk)
	canvas.imgref = abc_image_tk
	# grayscale_image = fnc.convert_to_grayscale(image_original)
	# image_tk = ImageTk.PhotoImage(grayscale_image)
	# image_original = python_dark
	# canvas.bind('<Configure>', show_full_image)
	

# widget
# label = ttk.Label(window, text = 'bubbles', image = image_tk)
# label.pack()
button_frame = ttk.Frame(window)
button = ttk.Button(button_frame, text = '   A button', image = python_dark_tk, compound = 'left', command=a_clicked)
button.pack(pady = 10)


button_ctk = ctk.CTkButton(button_frame, text = 'A button', image = img_ctk, compound = 'left')
button_ctk.pack(pady = 10)

button_frame.grid(column = 0, row = 0, sticky = 'nsew')



# canvas -> image
canvas = tk.Canvas(window, bd = 0, highlightthickness = 0, relief = 'ridge')
canvas.grid(column = 1, columnspan = 3, row = 0, sticky = 'nsew')
image_container = canvas.create_image( 0, 0, anchor = 'nw')
#canvas.bind('<Configure>', show_full_image)

# run
window.mainloop()