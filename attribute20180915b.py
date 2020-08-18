import numpy as np
import pickle

with open("data/lfw_attributes.pickle", "rb") as f:
    rv = pickle.load(f)
print(rv.keys())

attributes = rv["attributes"]
attrList = rv['list']

print("# len(attributes) = ", len(attributes))
print(attributes)

N = len(attrList)
print("# len(attrList) = ", N)

for a in attributes[1:]:
    val = np.empty(N)
    for i in range(N):
        val[i] = attrList[i][a]
    print(a, np.min(val), np.median(val), np.max(val))

aname = "Male"
#aname = "Smiling"
#aname = "No Eyewear"
#aname = "Mustache"

print(aname)

val = np.empty(N)
for i in range(N):
    val[i] = attrList[i][aname]

i = np.argmin(val)
fname = attrList[i]["person"].replace(" ", "_") + "_{0:04d}".format(attrList[i]["imagenum"])
print(fname, attrList[i][aname])
i = np.argmin(np.abs(val))
fname = attrList[i]["person"].replace(" ", "_") + "_{0:04d}".format(attrList[i]["imagenum"])
print(fname, attrList[i][aname])
i = np.argmax(val)
fname = attrList[i]["person"].replace(" ", "_") + "_{0:04d}".format(attrList[i]["imagenum"])
print(fname, attrList[i][aname])

print(np.sum(val >= 0), np.sum(val < 0))