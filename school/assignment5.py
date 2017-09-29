import simplegui

ballX = 10
ballY = 28
ballXvel = 2
guyX = 400
guyY = 400
guyVel = 2

def draw(canvas):
    global ballX
    global ballY
    global ballXvel
    
    global guyX
    global guyY
    global guyVel
    
    guyX += guyVel
    
    if (guyX >= 450):
        guyVel = -guyVel
    
    if (guyX <= 350):
        guyVel = -guyVel
    
    ballXvel += 0.01
    
    ballX += ballXvel
    ballY += 0.6 / ballXvel
    canvas.draw_line((0, 40), (450, 80), 2, "White")
    canvas.draw_line((50, 180), (500, 140), 2, "White")
    canvas.draw_line((0, 220), (450, 260), 2, "White")
    canvas.draw_line((50, 340), (500, 300), 2, "White")
    canvas.draw_line((50, 340), (50, 500), 2, "White")
    canvas.draw_polygon([(guyX + 20, guyY - 20), (guyX, guyY), (guyX - 20, guyY - 20)], 1, "White")
    canvas.draw_polygon([(guyX - 20, guyY - 20), (guyX - 20, guyY - 20), (guyX - 20, guyY - 80), (guyX + 20, guyY - 80)], 1, "White")
    canvas.draw_polygon([(guyX - 25, guyY - 11), (guyX - 50, guyY - 10), (guyX - 90, guyY - 60), (guyX, guyY - 80)], 1, "White")
    canvas.draw_polygon([(guyX + 20, guyY + 70), (guyX, guyY + 90), (guyX + 20, guyY - 20)], 1, "White")
    canvas.draw_polygon([(guyX - 50, guyY + 20), (guyX, guyY + 10), (guyX + 10, guyY - 70)], 1, "White")

    
    if (ballX <= 600):
        canvas.draw_circle((ballX, ballY), 9, 1, "White", "White")
        canvas.draw_circle((ballX + 50, ballY + 5), 9, 1, "White", "White")
        canvas.draw_circle((ballX + 100, ballY + 10), 9, 1, "White", "White")
        canvas.draw_circle((ballX + 150, ballY + 15), 9, 1, "White", "White")
        canvas.draw_circle((ballX + 200, ballY + 20), 9, 1, "White", "White")
        canvas.draw_circle((ballX + 250, ballY + 25), 9, 1, "White", "White")

def startForLoops():
    for i in range (0, 5):
        print("This loop is pure vanity. It has looped " + str(i) + " times")
    for i in range (0, 10):
        print("This loop is the second pure vanity loop. It has looped " + str(i) + " times")

startForLoops()
frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)
frame.start()
