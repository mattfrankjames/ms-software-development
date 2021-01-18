# import the math library
import math

# input for balls needed
numberOfBalls = int(input('How many bowling balls will be manufactured? '))
# diameter of each ball
ballDiameter = float(input('What is the diameter of each ball in inches? '))

ballRadius = float(ballDiameter / 2)
# core volume in inches cubed
coreVolume = int(input('What is the core volume in inches cubed? '))
# calculate the amount of core filler needed for each ball
fillerVolume = (4/3) * (math.pi * (ballRadius ** 3))
# get the filler amount per ball
fillerAmountPerBall = fillerVolume - coreVolume
# Multiply the amount of core filler by the number of balls
print(fillerAmountPerBall * numberOfBalls)