import simplegui
x = 0

def draw_handler(canvas):
    global x
    x += 1
    canvas.draw_circle((x, 50), 10, 10, "White", "White")
    canvas.draw_circle((x - 50, 50), 10, 10, "White", "White")
    canvas.draw_line((x - 25, 70), (x - 25, 100), 12, "White")
    canvas.draw_line((x - 50, 100), (x - 25, 120), 12, "White")
    canvas.draw_line((x - 25, 120), (x + 10, 100), 12, "White")

frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()
