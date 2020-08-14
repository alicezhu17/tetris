from graphics import *
from time import *
from random import *
from math import * 

fallen = []

class Game():
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.win = GraphWin("Tetris", self.cols * 30, self.rows * 30)
        self.current_shape = None
        self.key = None
        self.win.bind_all('<Key>',self.key_pressed)
        self.game_over = False
        
    def key_pressed(self,event):
        self.key=event.keysym
    
    def handle_keypress(self):
        if self.key == "Left" and self.current_shape.can_move(-1,0,game):
            self.current_shape.moveit(-1,0)
            self.key = None
        if self.key == "Right" and self.current_shape.can_move(1,0,game):
            self.current_shape.moveit(1,0)
            self.key = None
        if self.key == "Down" and self.current_shape.can_move(0,2,game):
            self.current_shape.moveit(0,2)
            self.key = None
        if self.key == "Up":
            self.current_shape.rotate()
            self.key = None
    
    def add_drop_shape(self,shape_letter,center):
        shape_dict = {"I":I_shape, "J":J_shape,"L":L_shape,"O":O_shape,"S":S_shape,"T":T_shape,"Z":Z_shape}
        shape = shape_dict[shape_letter](center)
        shape.drawit(self.win)
        self.current_shape = shape
        while shape.can_move(0,1, game) == True:
            shape.moveit(0,1)
            if shape.can_move(0,1,game):
                self.handle_keypress()
                sleep(.02)
            if shape.can_move(0,1,game):
                self.handle_keypress()
                sleep(.02)
            if shape.can_move(0,1,game):
                self.handle_keypress()
                sleep(.02)
            if shape.can_move(0,1,game):
                self.handle_keypress()
                sleep(.02)
            if shape.can_move(0,1,game):
                self.handle_keypress()
                sleep(.02)
            if shape.can_move(0,1,game):
                self.handle_keypress()
                sleep(.02)
            if shape.can_move(0,1,game):
                self.handle_keypress()
                sleep(.02)
            if shape.can_move(0,1,game):
                self.handle_keypress()
                sleep(.02)
            if shape.can_move(0,1,game):
                self.handle_keypress()
                sleep(.02)
            if shape.can_move(0,1,game):
                self.handle_keypress()
                sleep(.02)
        fallen.extend(shape.blocks)
        full_list = self.full() 
        self.undraws(full_list)
        self.moverow(full_list)
    
    def full(self):
        full_list = []
        for i in range(self.rows):
            counter = 0          
            for block in fallen:
                if block.y == i:
                    counter += 1
            if counter == self.cols:
                full_list.append(i)
        return full_list
    
    def undraws(self, full_list): 
        to_delete = []
        for item in fallen:
            if item.y in full_list:
                to_delete.append(item)
        for item in to_delete:
            item.undraw()
            fallen.remove(item)
    
    def moverow(self,full_list):
        for r in full_list:
            for item in fallen:
                if item.y < r:
                    item.moveit(0,1)
    
    def gameover(self,fallen):
            for blocks in fallen:
                if blocks.y == 0:
                    self.game_over = True
                    break 
                else:
                    self.game_over = False
            return self.game_over

            
class Block(Rectangle):
    def __init__(self, pt1, col):
        self.pt1 = pt1
        self.col = col
        self.x = pt1.x
        self.y = pt1.y
        self.x2 = self.x + 1
        self.y2 = self.y + 1
        Rectangle.__init__(self, Point(self.x * 30, self.y * 30),Point(self.x2 * 30, self.y2 * 30))
        self.setFill(col)
        self.point = Point(self.x, self.y)
    
    def drawit(self,win):
        self.draw(win)  
    
    def moveit(self, dx, dy):
        self.move(dx * 30,dy * 30)
        self.x = self.x + dx
        self.y = self.y + dy
    
    def can_move(self, dx, dy, game):
        if self.x + dx >= game.cols or self.x + dx < 0:
            return False
        if self.y + dy >= game.rows: 
            return False
        for item in fallen:
            if item.x == self.x + dx and item.y == self.y + dy:
                return False
        else:
            return True
   
         
class Shape(object):
    def __init__(self, list1, col):
        self.block1 = Block(list1[0], col)
        self.block2 = Block(list1[1], "black")
        self.block3 = Block(list1[2], col)
        self.block4 = Block(list1[3], col)
        self.blocks = [self.block1, self.block2, self.block3, self.block4]
        self.center_block = self.blocks[1]
    def drawit(self,win):
        self.block1.drawit(win)
        self.block2.drawit(win)
        self.block3.drawit(win)
        self.block4.drawit(win)
    def moveit(self, dx, dy):
        self.block1.moveit(dx,dy)
        self.block2.moveit(dx,dy)
        self.block3.moveit(dx,dy)
        self.block4.moveit(dx,dy)
    def can_move(self, dx,dy, game):
        for item in self.blocks:
            if item.can_move(dx,dy,game) == False:
                return False
        return True
    def rotate(self):
#        print( "center", "x:", self.center_block.x, "y:", self.center_block.y)
        for block in self.blocks:
#            print( "rotate", "x:", block.x, "y:", block.y)
            if block.x == self.center_block.x + 1 and block.y == self.center_block.y:
                if block.can_move(-1,1, game):
#                    print( 1)
                    block.moveit(-1,1)
            elif block.x == self.center_block.x and block.y == self.center_block.y + 1:
                if block.can_move(-1,-1, game):
#                    print( 2)
                    block.moveit(-1,-1)
            elif block.x == self.center_block.x - 1 and block.y == self.center_block.y:
                if block.can_move(1,-1, game):
#                    print( 3)
                    block.moveit(1,-1)
            elif block.x == self.center_block.x and block.y == self.center_block.y - 1:
                if block.can_move(1,1, game):
#                    print( 4)
                    block.moveit(1,1)
            elif block.x == self.center_block.x + 2 and block.y == self.center_block.y:
                if block.can_move(-2,2, game):
#                    print( 5)
                    block.moveit(-2,2)
            elif block.x == self.center_block.x and block.y == self.center_block.y + 2:
                if block.can_move(-2,-2, game):
#                    print( 6)
                    block.moveit(-2,-2)
            elif block.x == self.center_block.x - 2 and block.y == self.center_block.y:
                if block.can_move(2,-2, game):
#                    print( 7)
                    block.moveit(2,-2)
            elif block.x == self.center_block.x and block.y == self.center_block.y - 2:
                if block.can_move(2,2, game):
#                    print( 8)
                    block.moveit(2,2)
            elif block.x == self.center_block.x + 1 and block.y == self.center_block.y - 1 :
                if block.can_move(0,2, game):
#                    print( 9)
                    block.moveit(0,2)
            elif block.x == self.center_block.x + 1 and block.y == self.center_block.y + 1:
                if block.can_move(-2,0, game):
#                    print( 10)
                    block.moveit(-2,0)
            elif block.x == self.center_block.x - 1 and block.y == self.center_block.y + 1:
                if block.can_move(0,-2, game):
#                    print( 11)
                    block.moveit(0,-2)
            elif block.x == self.center_block.x -1 and block.y == self.center_block.y - 1:
                if block.can_move(2,0, game):
#                    print( 12)
                    block.moveit(2,0)

class  I_shape(Shape):
   def  __init__(self,  center):
     coords  =  [Point(center.x  -  1,  center.y),
                 Point(center.x  ,  center.y),
                 Point(center.x  +  1,  center.y),
                 Point(center.x  +  2,  center.y)]
     Shape.__init__(self,  coords,  "blue")
     self.center_block = self.blocks[1]

class J_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x  -  1,  center.y),
                    Point(center.x  ,  center.y),
                    Point(center.x  +  1,  center.y),
                    Point(center.x + 1, center.y + 1)]
        Shape.__init__(self,coords, "orange")
        self.center_block = self.blocks[1]

class L_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x  -  1,  center.y),
                    Point(center.x  ,  center.y),
                    Point(center.x  +  1,  center.y),
                    Point(center.x - 1, center.y + 1)]
        Shape.__init__(self,coords, "cyan")
        self.center_block = self.blocks[1] 

class O_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x  -  1,  center.y),
                    Point(center.x  ,  center.y),
                    Point(center.x,  center.y + 1),
                    Point(center.x -1 , center.y + 1)]
        Shape.__init__(self,coords, "red")
        self.center_block = self.blocks[1]
    def rotate(self):
        pass

class S_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x  -  1,  center.y + 1),
                    Point(center.x  ,  center.y),
                    Point(center.x,  center.y + 1),
                    Point(center.x + 1 , center.y)]
        Shape.__init__(self,coords, "green")
        self.center_block = self.blocks[1]

class T_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x  -  1,  center.y),
                    Point(center.x  ,  center.y),
                    Point(center.x + 1,  center.y),
                    Point(center.x, center.y + 1)]
        Shape.__init__(self,coords, "yellow")
        self.center_block = self.blocks[1]

class Z_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x  -  1,  center.y),
                    Point(center.x  ,  center.y),
                    Point(center.x,  center.y + 1),
                    Point(center.x + 1, center.y + 1)]
        Shape.__init__(self,coords, "magenta")
        self.center_block = self.blocks[1]


game = Game(12,20)
shape_letter_list = ["I","J","L","O","S","T","Z"]

while game.gameover(fallen) == False:
    a = choice(shape_letter_list)
    game.add_drop_shape(a, Point(5,0))
    
game.win.mainloop()
