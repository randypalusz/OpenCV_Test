import numpy as np
import cv2
from matplotlib import pyplot as plt
import time


def showbgr(image):
    b = image.copy()
    g = image.copy()
    r = image.copy()
    b[:, :, 1] = 0
    b[:, :, 2] = 0
    g[:, :, 0] = 0
    g[:, :, 2] = 0
    r[:, :, 0] = 0
    r[:, :, 1] = 0
    cv2.imshow('blue', b)
    cv2.imshow('green', g)
    cv2.imshow('red', r)
    return


def split(image):
    b = image[:, :, 0]
    g = image[:, :, 1]
    r = image[:, :, 2]
    return b, g, r


def showallborders(im, bw=30):
    bc = [255, 0, 0]

    # Convert image from BGR (OpenCV format) to RGB (for use with matplotlib)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

    replicate = cv2.copyMakeBorder(im, bw, bw, bw, bw, cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(im, bw, bw, bw, bw, cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(im, bw, bw, bw, bw, cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(im, bw, bw, bw, bw, cv2.BORDER_WRAP)
    constant = cv2.copyMakeBorder(im, bw, bw, bw, bw, cv2.BORDER_CONSTANT, value=bc)

    plt.subplot(231), plt.imshow(im, 'gray'), plt.title('ORIGINAL'), plt.axis('off')
    plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE'), plt.axis('off')
    plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT'), plt.axis('off')
    plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101'), plt.axis('off')
    plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP'), plt.axis('off')
    plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT'), plt.axis('off')

    plt.show()

    return


def showblend(im1, im2):
    for i in range(101):
        alpha = i*0.01
        beta = 1-alpha
        result = cv2.addWeighted(im1, alpha, im2, beta, gamma=0)
        cv2.waitKey(1)
        cv2.imshow('Blend Result', result)
    return



