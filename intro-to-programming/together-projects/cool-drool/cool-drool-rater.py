import graphics as g

ratingsFile = None
# handle FileNotFoundError
while True:
    inFileName = input('What file would you like to assess? ')
    try: 
    # do the thing here
        ratingsFile = open( inFileName, 'r' )
        break
    except FileNotFoundError:
        print('{0} was not found'.format(inFileName))

firstLine = ratingsFile.readline()
firstLineTokens = firstLine.split(',')
movieTitle = firstLineTokens[1]

totalRatings = 0
totalRatingsAboveCool = 0


for line in ratingsFile:
    ratings = line.split(',')
    for rating in ratings:
        numericRating = int(rating)
        totalRatings += 1
        if numericRating >= 6:
            totalRatingsAboveCool += 1
coolPct = totalRatingsAboveCool/totalRatings
print('MovieTitle: {}'.format(movieTitle))
print('Total number of ratings: {}'.format(totalRatings))
print('Cool percentage: {}'.format(coolPct))

ratingImageFile = ''
rating = ''
if totalRatings < 10:
    rating = 'Too soon to rule'
    ratingImageFile = 'tooSoonToRule.gif'
elif coolPct >= .6:
    rating = 'COOL'
    ratingImageFile = 'cool.gif'
else:
    rating = 'Drool'
    ratingImageFile = 'drool.gif'

win = g.GraphWin('COOl or DROOL rater', 400, 400)
titleText = g.Text(g.Point(200, 25), movieTitle)
titleText.draw(win)
ratingImage = g.Image(g.Point(200,200), ratingImageFile)
ratingImage.draw(win)
ratingPctText = g.Text(g.Point(200, 350), '{0:0.0f}% {1}'.format(coolPct * 100, rating))
ratingPctText.draw(win)