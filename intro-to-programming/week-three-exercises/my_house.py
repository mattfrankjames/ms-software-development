import graphics as g

def main():
    win = g.GraphWin('My House', 300, 300)
    win.setBackground(g.color_rgb(0, 255, 255))
    win.setCoords(0, 0, 10, 7)
    
    roofCenter = g.Point(5, 5)
    houseCornerRight = g.Point(8,3)
    
    roof = g.Polygon(g.Point(2, 3), roofCenter, houseCornerRight)
    roof.setFill(g.color_rgb(181, 101, 29))
    roof.draw(win)
    
    houseBase = g.Rectangle(g.Point(2, 0), houseCornerRight)
    houseBase.setFill(g.color_rgb(200, 0, 0))
    houseBase.draw(win)
    
    windowLeft = g.Rectangle(g.Point(3, 1), g.Point(4, 2))
    windowLeft.setFill(g.color_rgb(255, 255, 255))
    windowLeft.draw(win)
    
    door = g.Rectangle(g.Point(5, 0), g.Point(7, 2))
    door.setFill(g.color_rgb(101, 67, 33))
    door.draw(win)
    
    label = g.Text(g.Point(5, 6), 'This is my house')
    label.draw(win)
    
    treeTrunkLeft = g.Line(g.Point(1, 0), g.Point(1, 5))
    treeTrunkLeft.draw(win)
    
    treeTrunkRight = g.Line(g.Point(9, 0), g.Point(9, 5))
    treeTrunkRight.draw(win)
    
    treeTop = g.Circle(g.Point(1, 5.5), .5)
    treeTop.setFill(g.color_rgb(50, 205, 50))
    treeTop.draw(win)
    
    treeTopClone = treeTop.clone()
    treeTopClone.move(8, 0)
    treeTopClone.draw(win)
    
    win.getMouse()
    label.setText('You clicked the window!')
                  
main()