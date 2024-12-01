from PIL import Image, ImageTk
import fonksiyon as fn


def ChangeGrayClicked(canvas , image_container , imgPath ):
	res = fn.gray_image(imgPath)
	img = Image.fromarray(res)
	img_tk = ImageTk.PhotoImage(img)
	canvas.itemconfig(image_container, image = img_tk)
	canvas.imgref = img_tk