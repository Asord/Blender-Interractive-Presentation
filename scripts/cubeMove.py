from bge import logic
from bpy import data

cont = logic.getCurrentController()
#own  = cont.owner

move = cont.actuators["move"]

pressup =    cont.sensors["up"]
pressdown =  cont.sensors["down"]
pressleft =  cont.sensors["left"]
pressright = cont.sensors["right"]

speed =     move.dLoc[1]
direction = move.dRot[1]

if pressup.positive:     speed += 0.05
elif pressdown.positive: speed -= 0.05

if pressleft.positive:    direction += 0.025
elif pressright.positive: direction -= 0.025

move.dLoc = [0.0, speed,       0.0]
move.dRot = [0.0,   0.0, direction]
cont.activate(move)
cont.activate(direction)

data.objects["car"].data.vertices[0].co.x += 1.0