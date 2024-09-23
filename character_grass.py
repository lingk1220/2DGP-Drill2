from pico2d import *
import math




open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400, 30)
character.draw_now(400, 90)


x = 400
y = 90
i = 0
j = -1
r = 300
t = -90
s = 4
while (1):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)


    if(i <= 3):
  
        if(i == 0):
            if(x < 700):
                x = x + s
            else:
                i = 1
                
        if(i == 1):
            if(x > 400):
                x = x - s * math.cos(60 / 360 * 2 * math.pi)
                y = y + s * math.sin(60 / 360 * 2 * math.pi)
            else:
                i = 2
                
        if(i == 2):
            if(x > 100):
                x = x - s * math.cos(60 / 360 * 2 * math.pi)
                y = y - s * math.sin(60 / 360 * 2 * math.pi)
            else:
                i = 3             

        if(i == 3):
            if(x < 400):
                x = x + s
            else:
                i = -1            
                j = 0

    if(j == 0):
        if(t < 270):
            x = 400 + r * math.cos(t / 360 * 2 * math.pi)
            y = 90 + r + r * math.sin(t / 360 * 2 * math.pi)
            t = t + 1
        else:
            t = -90
            j = -1
            i = 0


    delay(0.01)

close_canvas()
