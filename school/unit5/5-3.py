import simplegui

def draw_handler(canvas):
    canvas.draw_polygon([(0, 0), (0, 100), (100, 100), (100, 0)], 2, "White")
    canvas.draw_polygon([(20, 20), (20, 80), (80, 80), (80, 20)], 2, "White")
    canvas.draw_polygon([(40, 40), (40, 60), (60, 60), (60, 40)], 2, "White")

frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()
