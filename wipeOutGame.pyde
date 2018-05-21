# 5-12-18 started at 1:30PM stopped at 1:50 -- when i outlined diffrent project ideas and chose my project
# 5-15-18 started at 1:38PM stoped at 1:50
# 5-17-18 started at 12:53PM stopped at 2:05
# 5-21-18 started at 1:00PM stopped at 2:15
# Total time spent working on project: 32 minutes

from Blocks import Blocks
def setup():
    size(500,500)

myBlocks = [[Blocks(random(0,280),20+(x*20),20+(y*20)) for x in range(24)]for y in range(24)]
    
def draw():
    background(255)
    for x in range(24):
        for y in range(24):
            myBlocks[x][y].display()
            if mousePressed:
                myBlocks[x][y].click()

#    for a in range(myblock.length):
#         myAsteroids[a]= Asteroid (random(1, 10), random(1, 10), random(1, 10), random (1, 100), random (1, 3))
# def draw():
#     for a in range(myblock.length):
#         myAsteroids[a].fall()
#         myAsteroids[a].display()
