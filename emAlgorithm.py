import numpy as np
import random

'''Data
H T T T H T T H T H 0.4
H H H H T H H H H H 0.9
H T H H H H H T H H 0.8
H T T T T T H H T T 0.3
T H H H T H H H T H 0.7'''
data = [0.4,0.9,0.8,0.3,0.7]


def emalgorithm(data):
    ateta = random.uniform(0,1)
    bteta = random.uniform(0,1)
    hiddenList = []
    while(matrixchanged(hiddenList)):
    # Growing list instead of replacing it makes it really large and inefficient. If you actually want to use this
    # algorithm more than once, do yourself a favour and adjust it accordingly
        hiddenList.append(estep(data, ateta, bteta))
        hiddenList.append(estep(data, bteta, ateta))
        ateta, bteta = mstep(data, hiddenList)
    # Last two lines of List are the resembling for the final hidden matrix
    hiddenMatrix = np.asarray(hiddenList[-2],hiddenList[-1])
    return hiddenMatrix

def matrixchanged(hiddenList):
    if len(hiddenList) < 4:
        return True
    elif hiddenList[-1] == hiddenList[-3] and hiddenList[-2] == hiddenList[-4]:
        return False
    else:
        return True

def estep(data, teta, tetak):
    hiddenList = []
    for datapoint in data:
        hiddenprob = calcHiddenprob(datapoint, teta, tetak)
        hiddenList.append(hiddenprob)
    return hiddenList

def calcHiddenprob(datapoint, teta, tetak):
    return np.exp(-((datapoint - teta)**2) / (2 * (tetak**2))) / (np.sqrt(2 * np.pi) * tetak)

def mstep(data, hiddenList):
    anumerator = 0
    bnumerator = 0
    aList = hiddenList[-2]
    bList = hiddenList[-1]
    adenominator = sum(aList)
    bdenominator = sum(bList)
    for i in range(len(data)):
        anumerator += data[i] * aList[i]
        bnumerator += data[i] * bList[i]
    ateta = anumerator / adenominator
    bteta = bnumerator / bdenominator
    return ateta, bteta

hiddenMatrix = emalgorithm(data)
np.set_printoptions(threshold=np.inf)
print(hiddenMatrix)
