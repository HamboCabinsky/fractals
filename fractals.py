import random

class Sierpinski:
    def __init__(self, c, width, height):
        self.canvas = c
        self.triangles = [c.create_polygon(width/2,0,0,height,width,height,fill="red")]
        self.triangle_verts = [(width/2,0,0,height,width,height)]

    def step(self):
        while self.triangles:
            self.canvas.delete(self.triangles.pop())
            
        new_verts = []
        while self.triangle_verts:
            points = self.triangle_verts.pop()
            
            top = (points[0],points[1])
            left = (points[2],points[3])
            right = (points[4],points[5])
            
            #get midpoints
            TL = ((top[0]+left[0])/2,(top[1]+left[1])/2)
            TR = ((top[0]+right[0])/2,(top[1]+right[1])/2)
            LR = ((left[0]+right[0])/2, left[1])

            #make new triangles
            tri1 = self.canvas.create_polygon(top[0],top[1],TL[0],TL[1],TR[0],TR[1],fill="red")
            new_verts += [(top[0],top[1],TL[0],TL[1],TR[0],TR[1])]
            tri2 = self.canvas.create_polygon(TL[0],TL[1],left[0],left[1],LR[0],LR[1],fill="yellow")
            new_verts += [(TL[0],TL[1],left[0],left[1],LR[0],LR[1])]
            tri3 = self.canvas.create_polygon(TR[0],TR[1],LR[0],LR[1],right[0],right[1],fill="blue")
            new_verts += [(TR[0],TR[1],LR[0],LR[1],right[0],right[1])]
            self.triangles += [tri1,tri2,tri3]

        self.triangle_verts += new_verts

class Barnsley:
    def __init__(self, c, x, y, s):
        self.canvas = c
        self.points = [c.create_oval(x,y,x+3,y+3,fill="red")]
        self.curr_point = (0,0)
        self.origin = (x,y)
        self.size = s

    def step(self, num_iter):
        oX = self.origin[0]
        oY = self.origin[1]
        while num_iter > 0:
            roll = random.random()
            new_point = None
            if roll < .73:
                new_point = (0.85*self.curr_point[0]+0.04*self.curr_point[1], -.04*self.curr_point[0]+0.85*self.curr_point[1] + 48*self.size)
                self.points += [self.canvas.create_oval(oX+new_point[0], oY-new_point[1], oX+new_point[0]+3, oY-new_point[1]+3,fill="green")]
            elif roll > .73 and roll < .76:
                new_point = (0, 0.16*self.curr_point[1])
                self.points += [self.canvas.create_oval(oX+new_point[0], oY-new_point[1], oX+new_point[0]+3, oY-new_point[1]+3,fill="red")]
            elif roll > .76 and roll < .89:
                new_point = (-.15*self.curr_point[0]+0.28*self.curr_point[1],0.26*self.curr_point[0]+0.24*self.curr_point[1]+48*self.size)
                self.points += [self.canvas.create_oval(oX+new_point[0], oY-new_point[1], oX+new_point[0]+3, oY-new_point[1]+3,fill="yellow")]
            else:
                new_point = (0.2*self.curr_point[0] - 0.26*self.curr_point[1], 0.23*self.curr_point[0]+0.2*self.curr_point[1]+13.2*self.size)
                self.points += [self.canvas.create_oval(oX+new_point[0], oY-new_point[1], oX+new_point[0]+3, oY-new_point[1]+3,fill="blue")]
            self.curr_point = new_point
            num_iter -= 1
