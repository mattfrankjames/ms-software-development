import graphics as g

def getColor( colorString ):
    tokens = colorString.split(',')
    if len(tokens) == 3:
        return g.color_rgb(int(tokens[0]), int(tokens[1]), int(tokens[2]))
    elif len(colorString) > 0:
        return colorString.strip()
    else:
        return 'white'
    
def getPoint( pointString ):
    x, y = pointString.split(',')
    return g.Point(int(x), int(y))

def getRadius( radiusString ):
    return int(radiusString)

def parseRectLine(line):
    shapeString, ulPointString, lrPointString, colorString = line.split(';')
    ulPt = getPoint(ulPointString)
    lrPt = getPoint(lrPointString)
    color = getColor(colorString)
    rectangle = g.Rectangle(ulPt, lrPt)
    rectangle.setFill(color)
    
    return rectangle

def parseCircleLine( line ):
    shapeString, centerString, radiusString, colorString = line.split(';')
    centerPt = getPoint (centerString)
    radius = getRadius(radiusString)
    color = getColor(colorString)
    circle = g.Circle(centerPt, radius)
    circle.setFill(color)
    
    return circle

def getShapeName(line):
    tokens = line.split(';')
    return tokens[0]

def getShapes(drawingFile):
    shapes = []
    lineNumber = 0
    for line in drawingFile:
        lineNumber = lineNumber + 1
        shapeName = getShapeName(line)
        shape = None
        if shapeName.casefold() == 'circle'.casefold():
            shape = parseCircleLine( line )
        elif shapeName.casefold() == 'rectangle'.casefold():
            shape = parseRectLine(line)
        else:
            raise ValueError( 'ERROR on line {0}: Invalid shape {1}'.format( lineNumber, shapeName ))
        shapes.append(shape)
    return shapes
def drawShapes(shapes):
    win = g.GraphWin('drawing', 500, 500)
    for shape in shapes:
        shape.draw(win)

def main():
    fileName = input('Enter thr drawing file name: ')
    
    drawingFile = open(fileName, 'r')
    
    shapes = getShapes(drawingFile)
    
    drawShapes(shapes)
    
main()
    