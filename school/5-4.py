import simplegui

def draw_handler(canvas):
    canvas.draw_polygon([(100, 100), (100, 200), (200, 200), (200, 100)], 5, "White")
    canvas.draw_polygon([(75, 100), (150, 50), (225, 100)], 5, "White")

frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()
