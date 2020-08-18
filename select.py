import numpy as np
import pickle
import cv2

### reading the pickle file
#
with open('data/lfw_attributes.pickle', 'rb') as f:
    rv = pickle.load(f)
print(rv.keys())

attributes = rv['attributes']
attrList = rv['list']

Nimg = len(attrList)
print("# Nimg = ", Nimg)

### chossing the first image for each person
#
nameDict = {}
Nperson = 0
indexList = []
for i in range(Nimg):
    a = attrList[i]
    if not a['person'] in nameDict:
        nameDict[a['person']] = i
        Nperson += 1
        indexList.append(i)

print("# Nperson = ", Nperson)

### splitting L & T
#
np.random.seed(0)
indexArray = np.array(indexList)
np.random.shuffle(indexArray)
indexL = indexArray[:4000]
indexT = indexArray[4000:]

### saving
#
lty = 70
height = 128
ltx = 76
width = 96

for i, idx in enumerate(indexL):
    name = attrList[idx]['person'].replace(' ', '_')
    fnSrc = 'data/lfw-deepfunneled/' + name + '/' + name + '_0001.jpg'
    print(i, idx, fnSrc)
    img = cv2.imread(fnSrc)
    print(img.shape)
    img2 = img[lty:lty+height, ltx:ltx+width, :]
    fnDst = f'data/lfw-selected/L/img{i:04d}.png'
    cv2.imwrite(fnDst, img2)

for i, idx in enumerate(indexT):
    name = attrList[idx]['person'].replace(' ', '_')
    fnSrc = 'data/lfw-deepfunneled/' + name + '/' + name + '_0001.jpg'
    print(i, idx, fnSrc)
    img = cv2.imread(fnSrc)
    print(img.shape)
    img2 = img[lty:lty+height, ltx:ltx+width, :]
    fnDst = f'data/lfw-selected/T/img{i:04d}.png'
    cv2.imwrite(fnDst, img2)

print(len(indexL), len(indexT))