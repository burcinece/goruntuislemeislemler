# import numpy as np
# import io
# import cv2 as cv

# def binary_image(img):
#     if img is None:
#         print("Resim yüklenemedi.")
#         return None
#     else:
#         height, width = img.size[1] ,  img.size[0]
#         binaryimg = np.zeros((height, width), dtype=np.uint8)
#         for y in range(height):
#             for x in range(width):
#                 pixel = img.get((int(x), int(y)))
#                 if (pixel < 128): 
#                     binaryimg[y, x] = 0
#                 else:
#                     binaryimg[y, x] = 255
#         return binaryimg
    

#     # griye çevirme
# # def gray_image(img):
# #     if img is None:
# #         print("Resim yüklenemedi.")
# #         return None
# #     else:
# #         height, width = img.shape[:2]
# #         grayimg = np.zeros((height, width), dtype=np.uint8)
# #         for y in range(height):
# #             for x in range(width):
# #                 pixel = img[y, x]
# #                 gray_value = int((pixel[0] + pixel[1] + pixel[2]) / 3)
# #                 grayimg[y, x] = gray_value
# #     return grayimg

# def convert_to_grayscale(image):
#     grayscale_image = []
#     width, height = image.size
    
#     for y in range(height):
#         grayscale_row = []
#         for x in range(width):
#             # Piksel değerlerini al
#             r, g, b = image.getpixel((x, y))
#             # Grayscale dönüşüm formülü
#             luminance = int(0.299 * r + 0.587 * g + 0.114 * b)
#             grayscale_row.append((luminance, luminance, luminance))
#         grayscale_image.append(grayscale_row)


import cv2
import numpy as np

def gray_image(imgPath):
    img = cv2.imread(imgPath)
    if img is None:
        print("Resim yüklenemedi.")
        return None
    else:
        height, width = img.shape[:2]
        grayimg = np.zeros((height, width), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                pixel = img[y, x]
                gray_value = int(0.299 * pixel[2] + 0.587 * pixel[1] + 0.114 * pixel[0])
                grayimg[y, x] = gray_value
        return grayimg
    


def binary_image(imgPath):
    img = cv2.imread(imgPath)
    if img is None:
        print("Resim yüklenemedi.")
        return None
    else:
        height, width = img.shape[:2]
        binaryimg = np.zeros((height, width), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                pixel = img[y, x]
                if (pixel < 128).any():
                    binaryimg[y, x] = 0
                else:
                    binaryimg[y, x] = 255
        return binaryimg
    


def rotation_image(imgPath):
    img = cv2.imread(imgPath)
    if img is None:
        print("Resim yüklenemedi.")
        return None
    else:
        height, width = img.shape[:2]
        rotated_img = np.zeros((width, height, 3), dtype=np.uint8)  # 3 kanallı bir görüntü oluşturulur
        for y in range(height):
            for x in range(width):
                pixel = img[y, x]
                rotated_img[x, height - 1 - y] = pixel  # Burada her bir BGR bileşeni ayrı ayrı atanır
        return rotated_img


#grayimg=gray_image(img)