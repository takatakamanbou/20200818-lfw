import numpy as np
import cv2

fn = 'data/lfw-selected/L/img0000.png'
img = cv2.imread(fn)
h, w, c = img.shape
print(w, h, c)

X = np.empty((4000, h, w, c))

for i in range(4000):
    fn = f'data/lfw-selected/L/img{i:04d}.png'
    X[i, ::] = cv2.imread(fn)

img = np.mean(X, axis=0)
cv2.imwrite('meanL.png', img)


X = np.empty((1721, h, w, c))

for i in range(1721):
    fn = f'data/lfw-selected/T/img{i:04d}.png'
    X[i, ::] = cv2.imread(fn)

img = np.mean(X, axis=0)
cv2.imwrite('meanT.png', img)
