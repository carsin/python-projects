import simplegui
import random

def getRandomColor():
    return "RGB(" + str(random.randint(0, 255)) + ", " + str(random.randint(0, 255)) + ", " + str(random.randint(0, 255)) + ")"

def draw_handler(canvas):
    for i in range (0, 1000):
        canvas.draw_point((random.randint(0, 600), random.randint(0, 600)), getRandomColor())

frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()
