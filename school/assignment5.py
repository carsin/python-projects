import simplegui

ballX = 10
ballY = 30

def draw(canvas):
    global ballX
    global ballY
    canvas.draw_line((0, 40), (450, 80), 2, "White")
    canvas.draw_line((50, 180), (500, 140), 2, "White")
    canvas.draw_line((0, 220), (450, 260), 2, "White")
    canvas.draw_line((50, 340), (500, 300), 2, "White")
    canvas.draw_line((50, 340), (50, 500), 2, "White")
    canvas.draw_circle((ballX, ballY), 9, 1, "White", "White")

frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)
frame.start()
