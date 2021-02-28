from random import *

def getValues():
    writeFileName = input('Enter the drawing file name to create: ')
    numShapes = int(input('Enter the number of shapes to make: '))
    return writeFileName, numShapes               

def setShapeToDraw():
    if (random() < .5):
        return 'Rectangle'
    else:
        return 'Circle'
    
def setPointOrRadius():
    basePoint = []
    nextPoint = []
    radius = 0
    for index in range(2):
        basePoint.append(randrange(50, 450))
        nextPoint.append(randrange(50, 450))
    shape = setShapeToDraw()
    if(shape == 'Circle'):
        radius = randrange(10, 200)
        return shape, basePoint, radius
    else:
        return shape, basePoint, nextPoint 

def setColorString():
    colorStops = []
    for stop in range(3):
        colorStops.append(randrange(65, 255))
    stopOne, stopTwo, stopThree = colorStops[0:3]
    return stopOne, stopTwo, stopThree

def writeShapeFile(num, file):
    writeFile = open(file, 'w')
    
    for shape in range(num):
        shapeToDraw, basePoint, geoInfo = setPointOrRadius()
        pointValOne, pointValTwo = basePoint[0:2]
        colorStopOne, colorStopTwo, colorStopThree = setColorString()
        if (shapeToDraw == 'Rectangle'):
            pointValThree, pointValFour = geoInfo[0:2]
            print('{0}; {1}, {2}; {3}, {4}; {5}, {6}, {7}'.format(shapeToDraw, pointValOne, pointValTwo, pointValThree, pointValFour, colorStopOne, colorStopTwo, colorStopThree), file=writeFile)
        else:
            print('{0}; {1}, {2}; {3}; {4}, {5}, {6}'.format(shapeToDraw, pointValOne, pointValTwo, geoInfo, colorStopOne, colorStopTwo, colorStopThree), file=writeFile)
    writeFile.close()
def main():

    writeFileName, numShapes = getValues()

    writeShapeFile(numShapes, writeFileName)

main()