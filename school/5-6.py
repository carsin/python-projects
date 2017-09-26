import simplegui
import math

# Global Variables
width = 600
height = 600
face1 = False
face2 = False
face3 = False
face4 = False

# Event Handlers

def toggle_face1():
    global face1
    face1 = not face1
    
def toggle_face2():
    global face2
    face2 = not face2
     
def toggle_face3():
    global face3
    face3 = not face3
    
def toggle_face4():
    global face4
    face4 = not face4
     
def draw(canvas):
    if face1:
        # face
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "Yellow", "Yellow")
        # eyes
        canvas.draw_circle((width/4, height/3), 50, 10, "Black", "Black")
        canvas.draw_circle((width/1.5, height/3), 50, 10, "Black", "Black")
        # mouth
        canvas.draw_circle((width/2, height/1.5), 50, 10, "Black", "Black")
    if face2:
        # face
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "Yellow", "Yellow")
        # eyes
        canvas.draw_circle((width/4, height/3), 50, 10, "Black", "Black")
        canvas.draw_circle((width/1.5, height/3), 50, 10, "Black", "Black")
        # mouth
        canvas.draw_circle((width/2, height/1.5), 50, 10, "Black", "Black")
        canvas.draw_circle((width/2, height/1.5 - 50), 50, 10, "Yellow", "Yellow")
    if face3:
        # face
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "Yellow", "Yellow")
        # eyes
        canvas.draw_circle((width/4, height/3), 50, 10, "Black", "Black")
        canvas.draw_circle((width/1.5, height/3), 50, 10, "Black", "Black")
        # mouth
        canvas.draw_circle((width/2, height/1.5), 50, 10, "Black", "Black")
        canvas.draw_circle((width/2, height/1.5 + 50), 50, 10, "Yellow", "Yellow")
    if face4:
        # face
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "Yellow", "Yellow")
        # eyes
        canvas.draw_circle((width/4, height/3), 50, 10, "Black", "Black")
        canvas.draw_circle((width/1.5, height/3), 50, 10, "Black", "Black")
        # mouth
        canvas.draw_line([width/2 - 50, height/1.5], [width/2 + 50, height/1.5], 20, 'Black')

frame = simplegui.create_frame("Pictures", width, height) 

frame.set_draw_handler(draw)

frame.add_button("Suprise", toggle_face1, 100)
frame.add_button("Happy", toggle_face2, 100)
frame.add_button("Sad", toggle_face3, 100)
frame.add_button("Neutral", toggle_face4, 100)

frame.start()
