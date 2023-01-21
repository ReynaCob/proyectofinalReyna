import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from flask import Flask
app = Flask(__name__)
@app.route("/")
def main():
    #Aqui va su código

    img = cv.imread('RX.jpg',0)
    laplacian = cv.Laplacian(img,cv.CV_64F)
    sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=15)
    sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
    plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])



    Fi3 = cv.imread ( 'Figure_1.jpg' , 0)
    imageOut = Fi3[60:220,280:480]
    cv2.imshow('Imagen de entrada',image)
    cv2.imshow('Imagen de salida',imageOut)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    plt.show()
    return  Fi3