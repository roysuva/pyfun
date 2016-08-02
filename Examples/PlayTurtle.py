import sys, os
import turtle, math

# clear screen
turtle.reset()
turtle.bgcolor((1,1,1)) # (1,1,1)=> 'white'

# Set pencolor, shape 
turtle.pencolor('black')
turtle.shape('turtle')


# Make a triangular flower
phi = 60
angles = [phi]*int(360/phi) # list of repeated number
dist = list(range(0,200,20))
dist.sort(reverse=True)
turtle.speed(10)
turtle.left(90)

for y in angles:
    
    theta = 180-((180-y)/2)    
    ct = len(dist)
    
    for x in dist:
        turtle.color((1,ct/len(dist),0))
        turtle.begin_fill()
        turtle.fd(x)
        turtle.right(theta)

        x_mid = math.sin(math.radians(y)) * x / math.sin(math.radians((180-y)/2))
        turtle.fd(x_mid)
        turtle.right(theta)

        turtle.fd(x)
        turtle.end_fill()
        turtle.right(180-phi)
        
        ct -= 1
        
    turtle.right(phi)


    
    

