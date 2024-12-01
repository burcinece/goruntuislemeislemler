import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import fonksiyon as fnc


width = 256
height = 256

def resizeImage(img):
	return img.resize((width, height))


def Change_Gray_Clicked():
	response = fnc.gray_image(image_original.filename)
	img = Image.fromarray(response)
	img_tk = ImageTk.PhotoImage(resizeImage(img))
	canvas.itemconfig(image_container, image = img_tk)
	canvas.imgref = img_tk


def Change_Binary_Clicked():
	response = fnc.binary_image(image_original.filename)
	img = Image.fromarray(response)
	img_tk = ImageTk.PhotoImage(resizeImage(img))
	canvas.itemconfig(image_container, image = img_tk)
	canvas.imgref = img_tk


def updateImage(img):
    resized_image = resizeImage(img)
    resized_image_tk = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(image_container, image = resized_image_tk)
    canvas.imgref = resized_image_tk


def Change_Rotation_Clicked():
	response = fnc.rotation_image(image_original.filename)
	img = Image.fromarray(response)
	img_tk = ImageTk.PhotoImage(resizeImage(img))
	canvas.itemconfig(image_container, image = img_tk)
	canvas.imgref = img_tk

python_dark = Image.open('Resimler/python_dark.png').resize((30,30))
image_original = Image.open('Resimler/bubbles.png')

img_ctk = ctk.CTkImage(
	light_image = Image.open('Resimler/python_dark.png'),
	dark_image = Image.open('Resimler/python_light.png'))


window = tk.Tk()
window.geometry('600x400')
window.title('Images')


canvas = tk.Canvas(window, bd = 0, highlightthickness = 0, relief = 'ridge')
canvas.grid(column = 1, columnspan = 3, row = 0, sticky = 'nsew')
image_container = canvas.create_image(50, 10, anchor = 'nw')

python_dark_tk = ImageTk.PhotoImage(python_dark)
button_frame = ttk.Frame(window)


button = ttk.Button(button_frame, text = 'Change Gray', image = python_dark_tk, compound = 'left' , command=Change_Gray_Clicked)
button.pack(pady = 10)

button_ctk = ctk.CTkButton(button_frame, text = 'Change Binary', image = img_ctk, compound = 'left' , command=Change_Binary_Clicked)
button_ctk.pack(pady = 10)

button = ttk.Button(button_frame, text = 'Change Rotation', image = python_dark_tk, compound = 'left' , command=Change_Rotation_Clicked)
button.pack(pady = 10)


button_frame.grid(column = 0, row = 0, sticky = 'nsew')


updateImage(image_original)
# run
window.mainloop()
