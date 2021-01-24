import graphics as g

def main():
    i = 1
    win = g.GraphWin('Gradient graph', 400, 400)
    win.setCoords(1, 0, 252, 252)
    win.setBackground('white')
    
    for i in range(1, 253):
        bar = g.Rectangle(g.Point(i, 0), g.Point(i + 1, 252))
        bar.setWidth(0)
        bar.setFill(g.color_rgb(0,i,0))
        bar.draw(win)
        print(i)
    
main()